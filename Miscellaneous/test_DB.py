import mysql.connector
from utils.db_connection import get_db_connection

connection = get_db_connection()
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="orangehrm"
)

cursor = connection.cursor()

cursor.execute("SHOW TABLES")

tables = cursor.fetchall()

print("Total Tables:", len(tables))

for table in tables:
    print(table[0])

cursor.close()
connection.close()