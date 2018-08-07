from mysql.connector import MySQLConnection, Error

def connect():
    try:
        con = MySQLConnection(host='localhost',
               database='Project',
               user='root',
               password='Katm2803')

        if con.is_connected():
            print('Connected to database')

    except Error:
        print(Error)

    finally:
        con.close()

if __name__ == '__main__':
    connect()
