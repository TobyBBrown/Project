from mysql.connector import MySQLConnection, Error
from single_api_insert import insert

def query_insert():
    try:
        con = MySQLConnection(host='localhost',
               database='test',
               user='root',
               password='Katm2803')
        if con.is_connected():
            print('Connected to database')

        cursor = con.cursor()
        cursor.execute("select * from testapi")
        row = cursor.fetchall()
        print(cursor.rowcount)

    except Error:
        print(Error)

    finally:
        cursor.close()
        con.close()

if __name__ == '__main__':
    query_insert()
