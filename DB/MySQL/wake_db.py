import mysql.connector
from datetime import datetime
from Backend.Config.settings import settings

def connect_db():
    conn = mysql.connector.connect(
        host = settings.MY_SQL_HOST,
        user = settings.MY_SQL_USER,
        password = settings.MY_SQL_PASSWORD,
        database = settings.MY_SQL_JARVIS_WAKE
    )
    return conn


def insert_wake(wake):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
        INSERT INTO wake_info (Wake_word, dates)
        VALUES (%s, %s)
    """

    today = datetime.now().date()   # store current date
    values = (wake, today)

    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()