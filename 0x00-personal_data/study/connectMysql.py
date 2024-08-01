#!/usr/bin/env python3
def get_db():
    "connect to secure dataBase"

    db = mysql.connector.connect(
        user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password = os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database = os.getenv('PERSONAL_DATA_DB_NAME')
    )

    return db

if __name__ == "__main__":
    import mysql.connector
    import os

    print(get_db())
