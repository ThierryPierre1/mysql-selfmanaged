# -*- coding: utf-8 -*-
"""mysql-selfmanaged

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DWwgWxdYwAObYMEryxW7IC52owB-eQzr
"""

from sqlalchemy import create_engine
import pandas as pd

MYSQL_HOSTNAME = '34.135.45.29' # you probably don't need to change this
MYSQL_USER = 'pierre'
MYSQL_PASSWORD = 'pierre718'
MYSQL_DATABASE = 'db1'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
connection_string

db = create_engine(connection_string)

db

query = 'select * from db1.UEFA;'
query

df = pd.read_sql(query, con=db)

df

real_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA-507-2022/main/descriptive/example1/data/test.csv')

real_df

real_df.to_sql('some_table', con=db, if_exists='replace')