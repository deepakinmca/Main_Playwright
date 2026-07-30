import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="orangehrm"
)

cursor = connection.cursor()

cursor.execute("SELECT DATABASE();")
print("Connected to:", cursor.fetchone())

cursor.execute("SHOW TABLES;")

tables = cursor.fetchall()

print("Tables:")
for table in tables:
    print(table)

cursor.close()
connection.close()