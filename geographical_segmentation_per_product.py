import pandas as pd
import random
#global df
df = pd.read_csv(r'C:\Users\Lior Barsky\Documents\jhonsonC\outputs\productsegmentation.csv', encoding="ISO-8859-8")

def get_labels(city_number):
    global df
    labels = []
    count = 0
    for i in df['City Name'].values:
        if count < city_number:
            count += 1
            labels.append(i)
    return  labels

def get_values(parameter, city_number):
    global df
    count = 0
    values = []
    if parameter == 'Orders Quantity':
        for i in df['Orders Quantity'].values:
            if count<city_number:
                count += 1
                values.append(i)
    if parameter == 'Total Quantity':
        for i in df['Total Quantity'].values:
            if count<city_number:
                count += 1
                values.append(i)
    return values

def get_colors(city_number):
    colors = []
    for i in range(city_number):
        color = '#' + str(''.join([random.choice('0123456789ABCDEF') for x in range(6)]))
        colors.append(color)
    return colors

def run():
    labels = get_labels(10)
    values = get_values('Orders Quantity', 30)
    #values = get_values('Total Quantity', 10)
    color = get_colors(10)
    return labels, values, color

#print(run()[0])
