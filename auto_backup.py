from datetime import datetime
import psycopg2
import os
import sys

def main():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_name = date.today().strftime("%Y-%m-%d") # Date only filename format in YYYY-MM-DD

    connection3 = psycopg2.connect("host='localhost' dbname='' user='' password=''") # Enter Db name and Db Admin's Username & Password
    cursor5 = connection3.cursor()
    os.system('pg_dump -U admin_user db_name | gzip > ' + BASE_DIR + '/sos/DB_Backup/' + file_name + '.gz') # Replace 'admin_user' and 'db_name' with Admin's Username and Database name respectively.
    connection3.commit()
