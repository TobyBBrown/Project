import re
from statistics import mean
from mysql.connector import MySQLConnection, Error


def main():
    game_query = "select * from testapi"

    cpu_query = "select * from cpubenchmarks"

    update_sql = "update testapi set min_cpu_score=%s, rec_cpu_score=%s where appid = %s"

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

        args = []

        for game in games:
            values = []
            min_list = []
            rec_list = []
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

                    if minimum is not None:
                        if code.group().lower() in minimum.lower():
                            min_list.append(cpu['Benchmark_Score'])
                        elif 'ghz' in minimum.lower():
                            ghz = re.search(r'\d\.?\d*(?=\s*ghz)', minimum, re.I)
                            if ghz is not None:
                                ghz = float(ghz.group())
                            if model.group().lower() in minimum.lower() and clock == ghz:
                                min_list.append(cpu['Benchmark_Score'])
                    if recommended is not None:
                        if code.group().lower() in recommended.lower():
                            rec_list.append(cpu['Benchmark_Score'])
                        elif 'ghz' in recommended.lower():
                            ghz = re.search(r'\d\.?\d*(?=\s*ghz)', recommended, re.I)
                            if ghz is not None:
                                ghz = float(ghz.group())
                            if model.group().lower() in recommended.lower() and clock == ghz:
                                rec_list.append(cpu['Benchmark_Score'])
                elif 'amd' in cpu['CPU_Name'].lower():
                    model = re.search(r'(?<=amd\s).*', cpu['CPU_Name'], re.I)
                    #code = re.search(r'(?<=' + re.escape(model.group()) + r'\s).*', cpu['CPU_Name'], re.I)
                    if minimum is not None:
                        if model.group() in minimum:
                            min_list.append(cpu['Benchmark_Score'])
                    if recommended is not None:
                        if model.group() in recommended:
                            rec_list.append(cpu['Benchmark_Score'])
            # if not min_list:
            #     if minimum is not None:
            #         if 'ghz' in minimum.lower():
            #             ghz = re.search(r'\d\.?\d*(?=\s*ghz)', minimum, re.I)
            #             if ghz is not None:
            #                 ghz = float(ghz.group())
            #                 min_list.append(ghz)
            # if not rec_list:
            #     if recommended is not None:
            #         if 'ghz' in recommended.lower():
            #             ghz = re.search(r'\d\.?\d*(?=\s*ghz)', recommended, re.I)
            #             if ghz is not None:
            #                 ghz = float(ghz.group())
            #                 rec_list.append(ghz)
            print(min_list)
            values.append(average(min_list))
            values.append(average(rec_list))
            values.append(game['appid'])
            cursor3.execute(update_sql, values)
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