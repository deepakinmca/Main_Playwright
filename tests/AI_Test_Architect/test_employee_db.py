import pytest
from utils.db_connection import get_db_connection

@pytest.mark.skip
def test_get_employees():
    connection = get_db_connection()
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

    print("\nEmployees:")
    for emp in employees:
        print(emp)

    assert len(employees) > 0

    cursor.close()
    connection.close()