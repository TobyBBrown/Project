"""Script for matching CPUs for both minimum and recommended specifications in game requirements
with their CPU benchmark scores and inserting those scores into the game requirements table.
"""

import re
from mysql.connector import MySQLConnection, Error


def main():
    """Connects to database project and queries all game rows. For each game, regexes are used to
    match the given CPU requirements with CPUs in the cpubenchmarks table. The average of all matched benchmark
    scores is then inserted into the corresponding field for that game in the game_requirements table.
    """

    game_query = "select * from game_requirements"

    cpu_query = "select * from cpubenchmarks"

    update_sql = "update game_requirements set min_cpu_score=%s, rec_cpu_score=%s where appid = %s"

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
        cursor2.execute(cpu_query)

        games = cursor1.fetchall()
        cpus = cursor2.fetchall()

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
                min_obj = re.search(r'(?<=processor:).*?(?=memory)', min_spec, re.I)
                if min_obj is not None:
                    minimum = re.sub(r'®|\?|™', '', min_obj.group())
            if rec_spec is not None:
                rec_obj = re.search(r'(?<=processor:).*?(?=memory)', rec_spec, re.I)
                if rec_obj is not None:
                    recommended = re.sub(r'®|\?|™', '', rec_obj.group())
            for cpu in cpus:
                if 'intel' in cpu['CPU_Name'].lower():
                    # For Intel CPUs, split the name into it's model name, it's specific model code
                    # and, if present, it's given clock speed.
                    if '@' in cpu['CPU_Name']:
                        split_cpu = re.findall(r'.*(?=\s@) | (?<=@\s).*', cpu['CPU_Name'])
                        cpu_name = split_cpu[0].strip()
                        clock = re.search(r'.*(?=ghz)', split_cpu[1].strip(), re.I)
                        model = re.search(r'(?<=intel\s).*(?=\s)', cpu_name, re.I)
                        code = re.search(r'(?<=' + re.escape(model.group()) + r'\s)[^\s]*', cpu_name, re.I)
                    else:
                        clock = re.search(r'\d\.?\d*(?=\s*ghz)', cpu['CPU_Name'], re.I)
                        model = re.search(r'(?<=intel\s).*(?=\s)', cpu['CPU_Name'], re.I)
                        code = re.search(r'(?<=' + re.escape(model.group()) + r'\s)[^\s]*', cpu['CPU_Name'], re.I)
                    if code is None:
                        code = model
                    if clock is not None:
                        clock = float(clock.group())

                    # If the CPU is present in the particular specification for a given game that benchmark score
                    # is considered  a direct match. Otherwise, the benchmark is only matched if both the model name
                    # and the CPU clock speed are in the game specifications.
                    if minimum is not None:
                        if code.group().lower() in minimum.lower():
                            min_score_list.append(cpu['Benchmark_Score'])
                        elif 'ghz' in minimum.lower():
                            ghz = re.search(r'\d\.?\d*(?=\s*ghz)', minimum, re.I)
                            if ghz is not None:
                                ghz = float(ghz.group())
                            if model.group().lower() in minimum.lower() and clock == ghz:
                                min_score_list.append(cpu['Benchmark_Score'])
                    if recommended is not None:
                        if code.group().lower() in recommended.lower():
                            rec_score_list.append(cpu['Benchmark_Score'])
                        elif 'ghz' in recommended.lower():
                            ghz = re.search(r'\d\.?\d*(?=\s*ghz)', recommended, re.I)
                            if ghz is not None:
                                ghz = float(ghz.group())
                            if model.group().lower() in recommended.lower() and clock == ghz:
                                rec_score_list.append(cpu['Benchmark_Score'])
                else:
                    # AMD CPUs had more regular names that the Intel CPUs, these are therefore simply matched
                    # by the presence of the model name directly in the game specifications.
                    model = re.search(r'(?<=amd\s).*', cpu['CPU_Name'], re.I)
                    if minimum is not None:
                        if model.group() in minimum:
                            min_score_list.append(cpu['Benchmark_Score'])
                    if recommended is not None:
                        if model.group() in recommended:
                            rec_score_list.append(cpu['Benchmark_Score'])

            # It is likely that for each game multiple CPU scores will be matched, scores are therefore put
            # into a list and the average score of the list is used as the final benchmark score. This minimises
            # potential differences between the matched score and the true game requirement score.
            args.append(average(min_score_list))
            args.append(average(rec_score_list))
            args.append(game['appid'])
            cursor3.execute(update_sql, args)
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