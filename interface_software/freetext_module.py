from h11 import SERVER
import pypyodbc as odbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'THTHTH'
DATABASE_NAME = 'VDGS'

connection_string = f"""
    DRIVVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_connection=yes;
    uid=<username>
    pwd=<password>
"""

conn = odbc.connect(connection_string)

print(conn)