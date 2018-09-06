"""Functions for getting the data from the steam store api and inserting data in the project database."""

from mysql.connector import MySQLConnection, Error
import requests


def check_id(appid):
    """Checks whether the steam store api has an entry for the appid provided.
    Returns the boolean value corresponding to the presence of an entry.
    """

    url = 'https://store.steampowered.com/api/appdetails/?appids=' + str(appid)
    json = requests.get(url).json()
    success = json[str(appid)]['success']
    return success


def get_api_data(appid, level):
    """Retrieves data from the steam store api entry for the given appid and for the given
    requirements level (minimum/recommended).
    Returns a tuple containing the game appid, name and retrieved specifications.
    """

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
    """Inserts the provided game data into the game_requirements table."""

    query = """insert into game_requirements(appid, name, min_specs, rec_specs)
            values (%s,%s,%s,%s)"""

    args = (appid, name, min_specs, rec_specs)
            
    try:
        con = MySQLConnection(host='localhost',
               database='project',
               user='root',
               password='project')
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
