import pyodbc
from settings import db_server, db_name, db_password, db_username, db_port, db_driver

def create_db_cursor():
    connection_string = f'DRIVER={db_driver};SERVER={db_server};PORT={db_port};DATABASE={db_name};UID={db_username};' \
                        f'PWD={db_password}'
    conn = pyodbc.connect(connection_string)
    return conn.cursor()


client = create_db_cursor()

def example_select():
    client.execute("SELECT * from users")
    row = client.fetchone()
    while row:
        print(str(row[0]) + " " + str(row[1]))
        row = client.fetchone()

example_select()