import mysql.connector
import pandas as pd


def connectToDB():
    connection = mysql.connector.connect(host='localhost',
                                         database='johnson_clean',
                                         user='root',
                                         password='root')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
    return connection


def tableName(tableName, con):
    df = pd.read_sql('SELECT * FROM %s' % tableName, con)
    return df
