from mysql.connector import MySQLConnection, Error
import requests


def check_id(appid):
    url = 'https://store.steampowered.com/api/appdetails/?appids=' + str(appid)
    json = requests.get(url).json()
    success = json[str(appid)]['success']
    print(appid)
    return success


def get_api_data(appid, level):
    url = 'https://store.steampowered.com/api/appdetails/?appids=' + str(appid)
    json = requests.get(url).json()
    reqs = json[str(appid)]['data']['pc_requirements']
    if level in reqs:
            specs = reqs[level]
    else:
            specs = None
    name = json[str(appid)]['data']['name']
    return appid, name, specs


def insert(appid, name, min_specs, rec_specs):
    query = """insert into game_requirements(appid, name, min_specs, rec_specs)
            values (%s,%s,%s,%s)"""

    args = (appid, name, min_specs, rec_specs)
            
    try:
        con = MySQLConnection(host='localhost',
               database='project',
               user='root',
               password='Katm2803')
        if con.is_connected():
            print('Connected to database')

        cursor = con.cursor()
        cursor.execute(query, args)

        print('insert id', appid)
        con.commit()

    except Error as error:
        print(appid)
        print(error)

    finally:
        cursor.close()
        con.close()


def main():
    reqs = get_api_data(400)
    insert(*reqs)


if __name__ == '__main__':
    main()
