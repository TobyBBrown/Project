import re
from mysql.connector import MySQLConnection, Error

game_query = "select * from testapi"

gpu_query = "select * from gpubenchmarks"

update_query = "update testapi set min_gpu_score=%s, rec_gpu_score=%s where appid = %s"

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
                if gpu['GPU_Name'] in minimum:
                    min_list.append(gpu['Benchmark_Score'])
            if recommended is not None:
                if gpu['GPU_Name'] in recommended:
                    rec_list.append(gpu['Benchmark_Score'])
        values.append(max(min_list, default=None))
        values.append(max(rec_list, default=None))
        values.append(game['appid'])
        cursor3.execute(update_query, values)
        con.commit()

except Error as error:
    print(error)
finally:
    cursor1.close()
    cursor2.close()
    con.close()