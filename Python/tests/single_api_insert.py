from mysql.connector import MySQLConnection, Error
import requests


def get_api_data(appid):
    url = 'https://store.steampowered.com/api/appdetails/?appids=' + str(appid)
    json = requests.get(url).json()
    name = json[str(appid)]['data']['name']
    specs = json[str(appid)]['data']['pc_requirements']['minimum']
    return appid, name, specs


def insert(appid, name, specs):
    query = """insert into testapi(appid, name, specs)
            values (%s,%s,%s)"""

    args = (appid, name, specs)
            
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
    reqs = get_api_data(400)
    insert(*reqs)


if __name__ == '__main__':
    main()
