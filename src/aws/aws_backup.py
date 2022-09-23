import pymysql
from dotenv import load_dotenv
import os
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))


host = os.getenv('AWS_HOSTNAME')
user = os.getenv('AWS_USERNAME')
password = os.getenv('AWS_PASSWORD')
database = os.getenv('AWS_DATABASE')

connection = pymysql.connect(
    host=host, user=user, passwd=password, database=database)
with connection:
    cur = connection.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS B_{database}")
    cur.execute(f"CREATE DATABASE B_{database}")
    connection.commit()
    cur.execute("SHOW TABLES")
    tables = cur.fetchall()
    for table in tables:
        cur.execute(
            f"CREATE TABLE B_{database}.B_{table[0]} like {database}.{table[0]}")
        cur.execute(
            f"INSERT INTO B_{database}.B_{table[0]} SELECT * FROM {database}.{table[0]}")
        connection.commit()
        print("Created Backup Table: ", f"B_{database}.B_{table[0]}")
