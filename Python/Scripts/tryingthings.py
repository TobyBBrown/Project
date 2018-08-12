import re
from mysql.connector import MySQLConnection, Error

specs = """Recommended:OS: 64-bit: Win 7, Win 8, Win 10Processor: Intel Core i7-3770, 3.4 GHz | AMD FX-8350, 4.0 GHzMemory: 
8 GB RAMGraphics: NVIDIA GeForce GTX 660 | AMD Radeon HD 7950DirectX: Version 11Network: Broadband Internet 
connectionStorage: 44 GB available space"""

specs2 = """Minimum:OS: Windows Vista / 7 / 8Processor: Intel® Core? i3 / AMD® Athlon? 64 x2 or higherMemory:
         2 GB RAMGraphics: Nvidia® GeForce? 8800 GTS / AMD® Radeon? HD 3850 or betterDirectX: Version 9.0cStorage: 
         1 GB available space """

graphicsobj = re.search(r'(?<=graphics:).*?(?=directx|hard|network|storage)', specs2, re.I)
print(graphicsobj.group())
subobj = re.sub(r'®|\?|™', '', graphicsobj.group())
print(subobj)

query = "select * from gpubenchmarks"
try:
    con = MySQLConnection(host='localhost',
                          database='project',
                          user='root',
                          password='Katm2803')
    if con.is_connected():
        print('Connected to database')

    cursor1 = con.cursor()
    cursor2 = con.cursor()
    cursor1.execute(query)

    rows = cursor1.fetchall()
    for row in rows:
        if row[1] in subobj:
            print(row[0])

except Error as error:
    print(error)
finally:
    cursor1.close()
    con.close()


# processorobj = re.search(r'(?<=processor:).*(?=memory:)', specs, re.I)
# processor = re.findall(r'intel .*[^,|]')
# if processorobj is not None:
#     print(processor.group())