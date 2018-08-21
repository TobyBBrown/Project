"""Script for matching GPUs for both minimum and recommended specifications in game requirements
with their GPU benchmark scores and inserting those scores into the game requirements table.
"""

import re
from mysql.connector import MySQLConnection, Error


def main():
    """Connects to database project and queries all game rows. For each game, regexes are used to
    match the given GPU requirements with GPUs in the cpubenchmarks table. The average of all matched benchmark
    scores is then inserted into the corresponding field for that game in the game_requirements table.
    """

    game_query = "select * from game_requirements"

    gpu_query = "select * from gpubenchmarks"

    update_query = "update game_requirements set min_gpu_score=%s, rec_gpu_score=%s where appid = %s"

    try:
        con = MySQLConnection(host='localhost',
                              database='project',
                              user='root',
                              password='project')
        if con.is_connected():
            print('Connected to database')

        cursor1 = con.cursor(buffered=True, dictionary=True)
        cursor2 = con.cursor(buffered=True, dictionary=True)
        cursor3 = con.cursor()
        cursor1.execute(game_query)
        cursor2.execute(gpu_query)

        games = cursor1.fetchall()
        gpus = cursor2.fetchall()

        for game in games:
            print(game['appid'])
            args = []
            min_score_list = []
            rec_score_list = []
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

            # GPU names are matched directly if they are in the gme specifications.
            for gpu in gpus:
                if minimum is not None:
                    if gpu['GPU_Name'].lower() in minimum.lower():
                        min_score_list.append(gpu['Benchmark_Score'])
                if recommended is not None:
                    if gpu['GPU_Name'].lower() in recommended.lower():
                        rec_score_list.append(gpu['Benchmark_Score'])

            # It is likely that for each game multiple GPU scores will be matched, scores are therefore put
            # into a list and the average score of the list is used as the final benchmark score. This minimises
            # potential differences between the matched score and the true game requirement score.
            args.append(average(min_score_list))
            args.append(average(rec_score_list))
            args.append(game['appid'])
            cursor3.execute(update_query, args)
            con.commit()

    except Error as error:
        print(error)
    finally:
        cursor1.close()
        cursor2.close()
        con.close()


def average(lst):
    """Calculates and returns the average of values in the given list."""

    if not lst:
        return None
    return sum(lst) / len(lst)


if __name__ == '__main__':
    main()