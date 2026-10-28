
# pip install -r requirements.txt

import pandas as pd

from sqlalchemy import create_engine 

def connect_database():
     try:
        engine=create_engine(url="mysql+mysqldb://root:root@localhost/food_delivery")
        # create_engine(url="mssql+pyodbc://root:root@localhost/food_delivery")
     except:
         return None,False
     else:
          return engine,True

def   connect_tables():
     try:
        engine,_=connect_database()
        if engine is not None:
          customers=pd.read_sql_query("select * from customers;",engine)
          menu_item=pd.read_sql_query("select * from menu_item;",engine)
          orders=pd.read_sql_query("select * from orders;",engine)
          rest=pd.read_sql_query("select * from Restaurants;",engine)
          delivery=pd.read_sql_query("select * from delivery;",engine)
     except:
         print("Table Name is incorrect..check once")
     else:
        return customers,menu_item,orders,rest,delivery

