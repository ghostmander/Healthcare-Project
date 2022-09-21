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
        for column in tableDesc:
            print("\t", column)
        print('\n\n')
