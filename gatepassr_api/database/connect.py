import psycopg2
from flask import current_app

#import sys
#sys.path.insert(0, "gatepassr_api/database")
#from config import load_config
"""
dbname*: the database name
*database*: the database name (only as keyword argument)
*user*: user name used to authenticate
*password*: password used to authenticate
*host*: database host address (defaults to UNIX socket if not provided)
*port*: connection port number (defaults to 5432 if not provided)
"""


def connect():
    """ Connect to the PostgreSQL database server """
    config = {"host": current_app.config['POSTGRES_HOST_URI'], "password": current_app.config['POSTGRES_PASSWD'], "dbname": current_app.config['POSTGRES_DATABASE_NAME'], "user": current_app.config['POSTGRES_USERNAME']}

    try:
        # connecting to the PostgreSQL server
        #with psycopg2.connect(host = current_app.config['POSTGRES_HOST_URI'], password = current_app.config['POSTGRES_PASSWD'], dbname = current_app.config['POSTGRES_DATABASE_NAME'], user = current_app.config['POSTGRES_USERNAME']) as conn:

        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            cursor = conn.cursor()
            return cursor, conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


#connect(config)
