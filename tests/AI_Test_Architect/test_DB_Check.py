import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="orangehrm"
)

cursor = connection.cursor()

# Check current database
cursor.execute("SELECT DATABASE()")
print("Current Database:", cursor.fetchone())

# Check tables
cursor.execute("SHOW TABLES")

tables = cursor.fetchall()

print("Total Tables:", len(tables))

for table in tables[:5]:
    print(table)

cursor.close()
connection.close()