import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import pandas as pd
import numpy as np


try:
    connection = mysql.connector.connect(host = 'localhost',
                                         database = 'greencloudservice_dev_kisan19',
                                         user = 'root',
                                         password = 'afroz123')

    mycursor = connection.cursor()

    mysql_select_query = "SELECT * FROM analytics"
    mycursor.execute(mysql_select_query)
    rows = mycursor.fetchall()  # Fetches all rows with following entries

    mycursor.execute("SHOW columns FROM analytics")
    x = [column[0] for column in mycursor.fetchall()]  # Getting the Column_names

    df = pd.DataFrame([[ij for ij in i] for i in rows], columns=[x for x in x])  # Adding the columns and rows to the dataframe
    print(df)


    print("Record displayed !!")
    mycursor.close()

except mysql.connector.Error as error:
    print("Failed to display the record from analytics table {}".format(error))

finally:
    if(connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")

