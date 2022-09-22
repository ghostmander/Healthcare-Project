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
os.system('cls|clear')
with connection:
    cur = connection.cursor()
    while True:
        query = input(">> ")
        if query in ("?", "help", "HELP", "h", "H", "-h", "--help"):
            print(">> Type 'EXIT' to exit the console")
        if query == "EXIT":
            break
        else:
            try:
                cur.execute(query)
                connection.commit()
                print(cur.fetchall())
            except:
                print("Invalid Query")
