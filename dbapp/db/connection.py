import pyodbc

CONNECTION_STRING = """
DRIVER={MySQL ODBC 9.4 Unicode Driver};
SERVER=localhost;
PORT=3306;
DATABASE=sampledb;
UID=user;
PWD=userpass;
OPTION=3;
"""

def get_connection():
    """`pyodbc.Connection`インスタンスを返す
    """
    return pyodbc.connect(CONNECTION_STRING)