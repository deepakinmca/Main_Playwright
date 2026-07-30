from utils.db_connection import get_db_connection


def get_employee(employee_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT *
    FROM hs_hr_employee
    WHERE employee_id = %s
    """

    cursor.execute(query, (employee_id,))
    employee = cursor.fetchone()

    cursor.close()
    connection.close()

    return employee


def employee_exists(employee_id):
    return get_employee(employee_id) is not None


def get_employee_by_name(first_name, last_name):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT *
    FROM hs_hr_employee
    WHERE emp_firstname = %s
      AND emp_lastname = %s
    """

    cursor.execute(query, (first_name, last_name))
    employee = cursor.fetchone()

    cursor.close()
    connection.close()

    return employee


def get_all_employees():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM hs_hr_employee")
    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return employees