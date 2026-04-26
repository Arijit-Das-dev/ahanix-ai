import mysql.connector
from datetime import datetime
from Backend.Config.settings import settings

def connect_db():
    conn = mysql.connector.connect(
        host = settings.MY_SQL_HOST,
        user = settings.MY_SQL_USER,
        password = settings.MY_SQL_PASSWORD,
        database = settings.MYSQL_JARVIS_WEATHER
    )
    return conn


def insert_weather(temparature, windspeed, winddirection, weather_code, humidity, pressure, cloud_cover):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
        INSERT INTO weather_info (temparature, windspeed, winddirection, weather_code, humidity, pressure, cloud_cover, dates)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    today = datetime.now().date()   # store current date
    values = (temparature, windspeed, winddirection, weather_code, humidity, pressure, cloud_cover, today)

    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()