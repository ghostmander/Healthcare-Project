import pymysql
from dotenv import load_dotenv
import os
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))


host = os.getenv('AWS_HOSTNAME')
user = os.getenv('AWS_USERNAME')
password = os.getenv('AWS_PASSWORD')
database = os.getenv('AWS_DATABASE')

connection = pymysql.connect(
    host=host, user=user, passwd=password, database=database)
with connection:
    cur = connection.cursor()
    cur.execute("SHOW TABLES")
    tables = cur.fetchall()
    for table in tables:
        cur.execute(f"DESCRIBE {table[0]}")
        tableDesc = cur.fetchall()
        print("Table: ", table[0])
        print(f"+{'-'*30}+{'-'*30}+{'-'*10}+{'-'*10}+{'-'*10}+{'-'*30}+")
        print(
            f"| {'Field':29}| {'Type':29}| {'Null':9}| {'Key':9}| {'Default':9}| {'Extra':29}|")
        print(f"+{'-'*30}+{'-'*30}+{'-'*10}+{'-'*10}+{'-'*10}+{'-'*30}+")
        for col in tableDesc:
            print(
                f"| {col[0]:29}| {col[1]:29}| {col[2]:9}| {col[3]:9}| {'NULL' if col[4] is None else col[4]:9}| {col[5]:29}|")
        print(f"+{'-'*30}+{'-'*30}+{'-'*10}+{'-'*10}+{'-'*10}+{'-'*30}+\n")
