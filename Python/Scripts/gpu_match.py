import re
from mysql.connector import MySQLConnection, Error


def main():
    game_query = "select * from game_requirements"

    gpu_query = "select * from gpubenchmarks"

    update_query = "update game_requirements set min_gpu_score=%s, rec_gpu_score=%s where appid = %s"

    try:
        con = MySQLConnection(host='localhost',
                              database='project',
                              user='root',
                              password='Katm2803')
        if con.is_connected():
            print('Connected to database')

        cursor1 = con.cursor(buffered=True, dictionary=True)
        cursor2 = con.cursor(buffered=True, dictionary=True)
        cursor3 = con.cursor()
        cursor1.execute(game_query)
        cursor2.execute(gpu_query)

        games = cursor1.fetchall()
        gpus = cursor2.fetchall()

        args = []

        for game in games:
            print(game['appid'])
            values = []
            min_list = []
            rec_list = []
            min_spec = game['min_specs']
            rec_spec = game['rec_specs']
            minimum = None
            recommended = None
            if min_spec is not None:
                min_obj = re.search(r'(?<=graphics:).*?(?=directx|hard|network|storage)', min_spec, re.I)
                if min_obj is not None:
                    minimum = re.sub(r'®|\?|™', '', min_obj.group())
            if rec_spec is not None:
                rec_obj = re.search(r'(?<=graphics:).*?(?=directx|hard|network|storage)', rec_spec, re.I)
                if rec_obj is not None:
                    recommended = re.sub(r'®|\?|™', '', rec_obj.group())
            for gpu in gpus:
                if minimum is not None:
                    if gpu['GPU_Name'].lower() in minimum.lower():
                        min_list.append(gpu['Benchmark_Score'])
                if recommended is not None:
                    if gpu['GPU_Name'].lower() in recommended.lower():
                        rec_list.append(gpu['Benchmark_Score'])
            print(min_list)
            print(rec_list)
            values.append(average(min_list))
            values.append(average(rec_list))
            values.append(game['appid'])
            cursor3.execute(update_query, values)
            con.commit()

    except Error as error:
        print(error)
    finally:
        cursor1.close()
        cursor2.close()
        con.close()


def average(lst):
    if not lst:
        return None
    return sum(lst) / len(lst)


if __name__ == '__main__':
    main()