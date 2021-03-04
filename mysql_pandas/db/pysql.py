import mysql.connector
from mysql.connector import Error
import pandas as pd 
import csv

class db_admin:
    
    def __init__(self, hostname, login_user, pass_user, databse):
        self.host = hostname
        self.login = login_user
        self.password = pass_user
        self.datab_name = databse
        
    def create_connection(self, exist):
        connection = None
        if exist:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.login,
                passwd=self.password,
                database=self.datab_name
            )
        else:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.login,
                passwd=self.password,
            )            
        print("Connection Created!")    
        return connection

    data = pd.read_csv ("home_data.csv")   
    def execute_query(self, connection, query, val):
        cursor = connection.cursor()
        cursor.fast_executemany = True
        try:
            if val is not None:
                cursor.executemany(
                    query,
                    list(val.itertuples(index=False, name=None))
                )
            else:
                cursor.execute(query) 
            connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
    
    def init_db(self):
        connection = self.create_connection(False)
        create_db_query = 'CREATE DATABASE ' + self.datab_name
        self.execute_query(connection, create_db_query, None)
    
    def init_query(self, query, val):
        connection = self.create_connection(True)
        self.execute_query(connection, query, val) # Execute query

def main():
    hostname = 'localhost'
    login_user = 'root'
    pass_user = '2311' #Put your password here
    databse = 'houses'
    ini = db_admin(hostname, login_user, pass_user, databse)
    ini.init_db()
    data = pd.read_csv ("home_data.csv")   
    df = pd.DataFrame(data, columns = ['id', 'date', 'price', 'grade', 'bedrooms', 'bathrooms', 'floors', 'waterfront', 'yr_built', 'condition'])

    create_table_house = """
    CREATE TABLE house (
    name_id INTEGER AUTO_INCREMENT PRIMARY KEY,  
    id BIGINT,
    date DATE,
    price integer,
    grade integer,
    bedrooms integer,
    bathrooms integer,
    floors integer,
    waterfront integer,
    yr_built integer,
    condition_house integer
    );
    """

    query = ("""INSERT INTO houses.house (id, date, price, grade, bedrooms, bathrooms, floors, waterfront, yr_built, condition_house)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""")
    ini.init_query(create_table_house, None)
    ini.init_query(query, df)

if __name__ == '__main__':
    main()
