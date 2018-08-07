from mysql.connector import MySQLConnection, Error

def insert(firstname, lastname, age):
    query = "insert into family(firstname, lastname, age)" \
            "values (%s,%s,%s)"

    args = (firstname, lastname, age)
            
    try:
        con = MySQLConnection(host='localhost',
               database='test',
               user='root',
               password='Katm2803')
        if con.is_connected():
            print('Connected to database')

        cursor = con.cursor()
        cursor.execute(query, args)

        
        print('insert id', cursor.lastrowid)
        con.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        con.close()

def main():
  insert('Granny', 'Person', 82)  

if __name__ == '__main__':
    main()
