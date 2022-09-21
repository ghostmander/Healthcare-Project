import pymysql
from dotenv import load_dotenv
import os
load_dotenv()

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
    print(f"List of Tables: [{', '.join([table[0] for table in tables])}]")
