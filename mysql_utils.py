import mysql.connector as mysql

import settings


class DBManager:
    def __init__(self):
        self.credentials = self.get_db_credentials()
        self.db = self.connect_to_db()
        self.cursor = self.db.cursor(dictionary=True)
        self.table_name = settings.DB_TABLE_NAME

    # Get DB credentials
    def get_db_credentials(self):
        host = settings.DB_HOST
        port = settings.DB_PORT
        database = settings.DB_DATABASE
        user = settings.DB_USER
        password = settings.DB_PASSWORD

        credentials = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port
        }

        return credentials

    # Connect to DB
    def connect_to_db(self):
        db = mysql.connect(host=self.credentials['host'],
                           port=self.credentials['port'],
                           database=self.credentials['database'],
                           user=self.credentials['user'],
                           password=self.credentials['password'])
        return db

    # Insert clothe item
    def insert_movie(self, movie):
        insert_query = 'INSERT into {} (id, title, magnet, last_updated) VALUES ("{}", "{}", "{}", "{}")'.format(self.table_name, movie['id'], movie['title'], movie['magnet'], movie['last_updated'])

        self.cursor.execute(insert_query)
        self.db.commit()

        return movie['title']

    # Close connection to database
    def close(self):
        self.cursor.close()
        self.db.close()
