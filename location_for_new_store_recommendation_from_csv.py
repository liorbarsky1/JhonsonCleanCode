import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def run_by_paramenters(city_number, parameter):
    df = pd.read_csv(r'C:\Users\Lior Barsky\Desktop\jhonsonclean\\JhonsonCleanApp\algorithms\outputs\city.csv', encoding="ISO-8859-8")
    # Make fake dataset
    # height = x-values, bars = ?
    clients_num = []
    count = 0
    if parameter == 'Number of Clients':
        for i in df['Number of Clients'].values:
            if count<city_number:
                count += 1
                clients_num.append(i)
    if parameter == 'Total Orders':
        for i in df['Total Orders'].values:
            if count<city_number:
                count += 1
                clients_num.append(i)
    if parameter == 'Total Orders Value':
        for i in df['Total Orders Value'].values:
            if count<city_number:
                count += 1
                clients_num.append(i)
    clients_bars = []
    count = 0
    for i in df['City Name'].values:
        if count<city_number:
            count += 1
            backwards_city_name = i[::-1]
            clients_bars.append(backwards_city_name)
    clients_bars = tuple(clients_bars)


    # Choose the position of each barplots on the x-axis (space=1,4,3,1)
    clients_y_pos = []
    z= 0
    for i in range(0, city_number):
        z = z+7
        clients_y_pos.append(z)

    plt.figure(1)
    plt.title(parameter)
    plt.bar(clients_y_pos, clients_num)
    # Create names on the x-axis
    plt.xticks(clients_y_pos, clients_bars)
    #try this later:
    #plt.plot(clients_bars)
    # Create bars

    #plt.plot(clients_y_pos, clients_num)

    #plt.show()
    #return plt.figure(1).show()
    #plt.savefig('location.png')
    fig = plt.figure(1)
    #fig.show()
    return  plt.figure(1)

def bar_chart_total_orders(city_number = 7):

    cities = []
    total_orders = []
    count = 0
    df = pd.read_csv(r'C:\Users\Lior Barsky\Desktop\jhonsonclean\\JhonsonCleanApp\algorithms\outputs\city.csv', encoding="ISO-8859-8")

    for i in df['City Name'].values:
        if count < city_number :
            count += 1
            backwards_city_name = i[::-1]
            cities.append(backwards_city_name)
    # bars are by default width 0.8, so we'll add 0.1 to the left coordinates
    # so that each bar is centered

    count = 0

    for i in df['Total Orders'].values:
        if count<city_number:
            count += 1
            total_orders.append(i)

    xs = [i + 0.1 for i, _ in enumerate(cities)]

    # plot bars with left x-coordinates [xs], heights [num_oscars]
    plt.figure(1)
    plt.bar(xs, total_orders)
    plt.ylabel("# Total orders")
    plt.title("How Many Orders Were Made From Each city?")

    # label x-axis with movie names at bar centers
    plt.xticks([i + 0.5 for i, _ in enumerate(cities)], cities)

    plt.show()
    return plt.figure(1)

def bar_chart_total_orders_value(city_number = 7):

    cities = []
    total_orders_value = []
    count = 0
    df = pd.read_csv(r'C:\Users\Lior Barsky\Desktop\jhonsonclean\\JhonsonCleanApp\algorithms\outputs\city.csv', encoding="ISO-8859-8")

    for i in df['City Name'].values:
        if count < city_number :
            count += 1
            backwards_city_name = i[::-1]
            cities.append(backwards_city_name)
    # bars are by default width 0.8, so we'll add 0.1 to the left coordinates
    # so that each bar is centered

    count = 0

    for i in df['Total Orders Value'].values:
        if count<city_number:
            count += 1
            total_orders_value.append(i)

    xs = [i + 0.1 for i, _ in enumerate(cities)]

    # plot bars with left x-coordinates [xs], heights [num_oscars]
    plt.figure(1)
    plt.bar(xs, total_orders_value)
    plt.ylabel("# Total Orders Value")
    plt.title("What is the Value of the Total Orders From Each City?")

    # label x-axis with movie names at bar centers
    plt.xticks([i + 0.5 for i, _ in enumerate(cities)], cities)

    plt.show()
    return plt.figure(1)

def bar_chart_clients_number(city_number = 7):

    cities = []
    clients_number = []
    count = 0
    df = pd.read_csv(r'C:\Users\Lior Barsky\Desktop\jhonsonclean\\JhonsonCleanApp\algorithms\outputs\city.csv', encoding="ISO-8859-8")

    for i in df['City Name'].values:
        if count < city_number :
            count += 1
            backwards_city_name = i[::-1]
            cities.append(backwards_city_name)
    # bars are by default width 0.8, so we'll add 0.1 to the left coordinates
    # so that each bar is centered

    count = 0

    for i in df['Number of Clients'].values:
        if count<city_number:
            count += 1
            clients_number.append(i)

    xs = [i + 0.1 for i, _ in enumerate(cities)]

    # plot bars with left x-coordinates [xs], heights [num_oscars]
    plt.figure(1)
    plt.bar(xs, clients_number)
    plt.ylabel("# Clients Number")
    plt.title("How Many Customers Are There From Each City?")

    # label x-axis with movie names at bar centers
    plt.xticks([i + 0.5 for i, _ in enumerate(cities)], cities)

    #plt.show()
    plt.savefig('client_number_per_city.png')

    return plt.figure(1)

#draw_graph_totle_order_value_by_city()
#draw_graph_totle_order_by_city()
#print(draw_graph_number_of_clients_by_city())

#run_by_paramenters(7, 'Total Orders')
#bar_chart_total_orders()
bar_chart_clients_number()
#bar_chart_total_orders_value()
