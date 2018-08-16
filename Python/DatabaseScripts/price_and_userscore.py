from mysql.connector import MySQLConnection, Error
import requests


def database_insert():
    game_query = "select appid from game_requirements"


    update_query = "update game_requirements set userscore=%s, price=%s where appid = %s"

    try:
        con = MySQLConnection(host='localhost',
                              database='project',
                              user='root',
                              password='Katm2803')
        if con.is_connected():
            print('Connected to database')

        cursor = con.cursor(buffered=True, dictionary=True)
        cursor.execute(game_query)
        games = cursor.fetchall()

        for game in games:
            args = []
            appid = game['appid']
            userscore, price = get_data(appid)
            print(appid, userscore, price)
            args.append(userscore)
            args.append(price)
            args.append(appid)

            cursor.execute(update_query, args)
            con.commit()

    except Error as error:
        print(error)
    finally:
        cursor.close()
        con.close()


def get_data(appid):
    url = 'http://steamspy.com/api.php?request=appdetails&appid=' + str(appid)
    json = requests.get(url).json()
    if json is not None:
        userscore = json['userscore']
        price = json['price']
        if price is not None:
            price = int(price)
        else:
            price = 0
        return userscore, price
    return None


def main():
    database_insert()


if __name__ == '__main__':
    main()