import re
from mysql.connector import MySQLConnection, Error

specs = """Minimum:Requires a 64-bit processor and operating systemOS: Windows 7 SP1 or newerProcessor: Intel® i5-4590 / AMD FX 8350 equivalent or greaterMemory: 8 GB RAMGraphics: NVIDIA GeForce® GTX 970 / AMD Radeon? R9 290 equivalent or greaterDirectX: Version 11Storage: 2300 MB available space  """

specs2 = """Minimum:OS: Windows Vista / 7 / 8Processor: Intel® Core? i3 / AMD® Athlon? 64 x2 or higherMemory: 2 GB RAMGraphics: Nvidia® GeForce? 8800 GTS / AMD® Radeon? HD 3850 or betterDirectX: Version 9.0cStorage: 1 GB available space """

specs3 = """Minimum:OS: Windows XPProcessor: 1GHzMemory: 512 MB RAMGraphics: Radeon 4850 / GeForce 8800 (integrated gfx is not officially supported)DirectX: Version 9.0Storage: 500 MB available spaceSound Card: any
Additional Notes: Be sure to use the latest sound and graphics drivers"""

graphicsobj = re.search(r'(?<=graphics:).*?(?=directx|hard|network|storage)', specs, re.I)
print(graphicsobj.group())
subgraphics = re.sub(r'®|\?|™', '', graphicsobj.group())
print(subgraphics)

gpu_query = "select * from gpubenchmarks"
game_query = "select * from game_requirements"
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
        if row[1] in subgraphics:
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