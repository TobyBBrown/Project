import re
from mysql.connector import MySQLConnection, Error

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
       # correct^###########################################################################################^correct#
        for cpu in cpus:
            if 'intel' in cpu['CPU_Name'].lower():
                if '@' in cpu['CPU_Name']:
                    split_cpu = re.findall(r'.*(?=\s@) | (?<=@\s).*', cpu['CPU_Name'])
                    cpu = split_cpu[0].strip()
                    clock = re.search(r'.*(?=ghz)', split_cpu[1].strip(), re.I)
                else:
                    clock = re.search(r'\d\.?\d*(?=\s*ghz)', cpu, re.I)
                if clock is not None:
                    clock = float(clock.group())
                model = re.search(r'(?<=intel\s).*(?=\s)', cpu['CPU_Name'], re.I)
                code = re.search(r'(?<=' + re.escape(model.group()) + r'\s)[^\s]*', cpu['CPU_Name'], re.I)
                if minimum is not None:
                    if code.group() in minimum.lower():
                        min_list.append(cpu['Benchmark_Score'])
                    elif 'ghz' in minimum.lower():
                        ghz = re.search(r'\d\.?\d*(?=\s*ghz)', minimum, re.I)
                        if ghz is not None:
                            ghz = float(ghz.group())
                        if model.group() in minimum and clock == ghz:
                            min_list.append(cpu['Benchmark_Score'])
                if recommended is not None:
                    if code.group() in recommended.lower():
                        rec_list.append(cpu['Benchmark_Score'])
                    elif 'ghz' in recommended.lower():
                        ghz = re.search(r'\d\.?\d*(?=\s*ghz)', recommended, re.I)
                        if ghz is not None:
                            ghz = float(ghz.group())
                        if model.group() in recommended and clock == ghz:
                            rec_list.append(cpu['Benchmark_Score'])
            else:
                model = re.search(r'(?<=amd\s).*?(?=\s)', cpu['CPU_Name'], re.I)
                code = re.search(r'(?<=' + re.escape(model.group()) + r'\s).*', cpu['CPU_Name'], re.I)
                if minimum is not None:
                    if code.group() in minimum or model.group() + code.group() in minimum:
                        min_list.append(cpu['Benchmark_Score'])
                if recommended is not None:
                    if code.group() in recommended or model.group() + code.group() in recommended:
                        rec_list.append(cpu['Benchmark_Score'])
# TODO if list empty and ghz in processor, put ghz value in for basic comparison
        values.append(max(min_list, default=None))
        values.append(max(rec_list, default=None))
        values.append(game['appid'])
        cursor3.execute(update_sql, values)
        con.commit()

except Error as error:
    print(error)
finally:
    cursor1.close()
    cursor2.close()
    con.close()


if 'intel' in cpu.lower():
    if '@' in cpu:
        split_cpu = re.findall(r'.*(?=\s@) | (?<=@\s).*', cpu)
        cpu = split_cpu[0].strip()
        clock = re.search(r'.*(?=ghz)', split_cpu[1].strip(), re.I)
    else:
        clock = re.search(r'\d\.?\d*(?=\s*ghz)', cpu, re.I)
    if clock is not None:
        clock = float(clock.group())
    model = re.search(r'(?<=intel\s).*(?=\s)', cpu, re.I)
    code = re.search(r'(?<=' + re.escape(model.group()) + r'\s)[^\s]*', cpu, re.I)
    if code.group() in processor or model.group() + code.group() in processor:
        #TODO get and put score into database
        print('code match')
    else:
        if 'ghz' in processor.lower():
            ghz = re.search(r'\d\.?\d*(?=\s*ghz)', processor, re.I)
            if ghz is not None:
                ghz = float(ghz.group())
            if model.group() in processor and clock == ghz:
                print('ghz match', clock, ghz)
                #TODO get and put score in database
                #THINK deal with core2 duo as this is common one to mention
        else:
            print('no match')
            #TODO put None in database
else:
    model = re.search(r'(?<=amd\s).*?(?=\s)', cpu, re.I)
    code = re.search(r'(?<=' + re.escape(model.group()) + r'\s).*', cpu, re.I)
    print(code.group())
    if code.group() in processor or model.group() + code.group() in processor:
        #TODO get and put score into database
        print('code match')


#TODO/THINK if list of scores empty and ghz in processor, put ghz value in and use as basic comparison