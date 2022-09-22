
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


def get_connection():
    return connection


def insert(table, columns, values):
    with connection:
        cur = connection.cursor()
        cur.execute(f"INSERT INTO {table} ({columns}) VALUES ({values})")
        connection.commit()


def select(table, columns, condition=None):
    with connection:
        cur = connection.cursor()
        cur.execute(
            f"SELECT {columns} FROM {table} {f'WHERE {condition}' if condition else ''}")
        return cur.fetchall()


def execute(query):
    with connection:
        cur = connection.cursor()
        cur.execute(query)
        return cur.fetchall()


def insert_anthropometric(values):
    with connection:
        cur = connection.cursor()
        cur.execute(
            f"INSERT INTO ANTHRO VALUES ({values})")
        connection.commit()


def insert_clinical(values):
    with connection:
        cur = connection.cursor()
        cur.execute(
            f"INSERT INTO CLINICAL_ASSESSMENT (PATIENT_ID, patient_name, patient_age, patient_gender, Bilateral_pitting_edma, Bitots_spots, Emaciation, Hair_Loss, Change_in_hair_color') VALUES ({values})")
        connection.commit()
