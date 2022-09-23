
import pymysql
from dotenv import load_dotenv
import os
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))


host = os.getenv('AWS_HOSTNAME')
user = os.getenv('AWS_USERNAME')
password = os.getenv('AWS_PASSWORD')
database = os.getenv('AWS_DATABASE')


def get_connection():
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database)
    return connection


def insert(table, columns, values):
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database)
    with connection:
        cur = connection.cursor()
        cur.execute(f"INSERT INTO {table} ({columns}) VALUES ({values})")
        connection.commit()


def select(table, columns, condition=None):
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database)
    with connection:
        cur = connection.cursor()
        cur.execute(
            f"SELECT {columns} FROM {table} {f'WHERE {condition}' if condition else ''}")
        return cur.fetchall()


def execute(query):
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database)
    with connection:
        cur = connection.cursor()
        cur.execute(query)
        return cur.fetchall()


def insert_anthropometric(values):
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database)
    with connection:
        cur = connection.cursor()
        cur.execute(
            f"INSERT INTO ANTHRO VALUES ({values})")
        connection.commit()


def insert_clinical(values):
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database)
    with connection:
        cur = connection.cursor()
        cur.execute(
            f"INSERT INTO CLINICAL VALUES({values})")
        connection.commit()


def insert_dietary(values):
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database)
    with connection:
        cur = connection.cursor()
        cur.execute(
            f"INSERT INTO DIETARY VALUES({values})")
        connection.commit()


def insert_metabolic(values):
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database)
    with connection:
        cur = connection.cursor()
        cur.execute(
            f"INSERT INTO METABOLIC VALUES({values})")
        connection.commit()


def insert_patient(values):
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database)
    with connection:
        cur = connection.cursor()
        cur.execute(
            f"INSERT INTO PATIENT VALUES({values})")
        connection.commit()


def insert_stool_sample(values):
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database)
    with connection:
        cur = connection.cursor()
        # print(f"INSERT INTO `STOOL_SAMPLE_ANALYSIS` VALUES({values})")
        cur.execute(
            f"INSERT INTO `STOOL_SAMPLE_ANALYSIS` VALUES({values})")
        connection.commit()
