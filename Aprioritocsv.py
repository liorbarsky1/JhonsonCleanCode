import mysql.connector
from sqlalchemy import create_engine
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import networkx as nx
import matplotlib.pyplot as plt
from csv import writer

#global firstRun
firstRun = False
secondRun = False

def draw_graph(start_of_rules, end_of_rules):
    global firstRun
    global secondRun
    if (firstRun == True and start_of_rules == 0):
        return plt.figure(1)
    elif (secondRun == True and start_of_rules == 4):
        return plt.figure(1)
    elif (firstRun == False or secondRun == False or start_of_rules == 8 or start_of_rules == 12):
        plt.clf()
        cmap = plt.get_cmap("Pastel2")
        G1 = nx.DiGraph()

        color_map = []
        N = 50
        colors = plt.get_cmap("Pastel1")
        strs = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11', 'R12', 'R13', 'R14', 'R15']

        df = pd.read_csv(r'C:\Users\Lior Barsky\Desktop\jhonsonclean\\JhonsonCleanApp\algorithms\outputs\top-16-rules.csv', encoding ="ISO-8859-8")
        count = 0
        for i in range(start_of_rules,end_of_rules):
            count += 1
            G1.add_nodes_from(["R" + str(i)])

            a = frozenset([df.iloc[i,1]])
            b = list(a)[0]
            b_list = b.split(',')
            for product_name in b_list:
                product_name_b = product_name[::-1]
                G1.add_nodes_from([product_name_b])
                G1.add_edge(product_name_b, "R" + str(i), color=colors(count-1), weight=2)

            c = frozenset([df.iloc[i,2]])
            d = list(c)[0]
            d_list = d.split(',')
            for product_name in d_list:
                product_name_b = product_name[::-1]
                G1.add_nodes_from([product_name_b])
                G1.add_edge("R" + str(i), product_name_b, color=colors(count-1), weight=2)

        for node in G1:
            found_a_string = False
            for item in strs:
                if node == item:
                    found_a_string = True
            if found_a_string:
                color_map.append(cmap(2))
            else:
                color_map.append(cmap(3))

        edges = G1.edges()
        colors = [G1[u][v]['color'] for u, v in edges]
        weights = [G1[u][v]['weight'] for u, v in edges]

        pos = nx.spring_layout(G1, k=16, scale=1)
        nx.draw(G1, pos, edges=edges, node_color=color_map, edge_color=colors, width=weights, font_size=16,
                with_labels=False)

        for p in pos:  # raise text positions
            pos[p][1] += 0.07
        nx.draw_networkx_labels(G1, pos, horizontalalignment='center', font_family='sans-serif', font_size=6)

        if start_of_rules == 0:
            firstRun = True
        if start_of_rules == 4:
            print("[4,8] was running")
            secondRun = True
        #plt.show()
        plt.savefig(str(start_of_rules)+'apriori.png')
        return plt.figure(1)

def run():
    #Connect to database
    connection = mysql.connector.connect(host='localhost',
                                         database='johnson_str',
                                         user='root',
                                         password='Ll0503404646')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        #print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()


    # Loading the Data
    data = pd.read_sql('SELECT a.order_id ,a.customer_id, a.date_added ,b.name, b.product_id, b.quantity ,b.price, a.total'
                       ' FROM oc_order a join  (SELECT *  FROM oc_order_product) b  where a.order_id=b.order_id and year(date_added)>=2015 and customer_id != 0', connection)
    #data = pd.read_sql('SELECT * FROM oc_order', connection)
    data.head()

    # each basket represnt al  the purchases [from 2018 in this case] which made by specific client.
    baskets = (data.groupby(['customer_id', 'name'])['quantity'].sum().unstack().reset_index().fillna(0).set_index('customer_id'))

    # Defining the hot encoding function to make the data suitable
    # for the concerned libraries
    def hot_encode(x):
        if(x<= 0):
            return 0
        if(x>= 1):
            return 1

    # Encoding the datasets
    basket_encoded = baskets.applymap(hot_encode)
    baskets = basket_encoded

    # Building the model
    frq_items = apriori(baskets, min_support = 0.05, use_colnames = True)

    # Collecting the inferred rules in a dataframe
    rules = association_rules(frq_items, metric ="lift", min_threshold = 1)
    rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False])


    rules["antecedents"] = rules["antecedents"].apply(lambda x: list(x)[0]).astype("unicode")
    rules["consequents"] = rules["consequents"].apply(lambda x: list(x)[0]).astype("unicode")
    df = pd.DataFrame(rules)
    # saving the dataframe
    df.to_csv('apriori_rules.csv', encoding = "ISO-8859-8")

    draw_graph(0, 4)
    draw_graph(4, 8)

    #saving_rules_resule_on_csv(rules)
    return rules

#run()
draw_graph(0,8)
#draw_graph(0,4)
#draw_graph(4,8)
#draw_graph(8,12)
#draw_graph(12,16)
#understanding_how_to_read_csv(0,15)
