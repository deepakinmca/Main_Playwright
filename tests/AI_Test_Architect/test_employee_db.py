from utils.db_connection import *
from utils.db_queries import *

cursor = connection.cursor()
query = """
SELECT
    emp_number,
    employee_id,
    emp_firstname,
    emp_lastname
FROM hs_hr_employee
LIMIT 10;
"""

cursor.execute(query)

employees = cursor.fetchall()

print("Employees:\n")

for emp in employees:
    print(emp)

cursor.close()
connection.close()