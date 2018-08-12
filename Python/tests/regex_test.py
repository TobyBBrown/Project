import re
import requests

specs = '''Minimum:OS:Microsoft® Windows® XP SP2 / Vista / 7Processor:Intel® Pentium 2,0 GHz/AMD
2000+Memory:2 GB RAMGraphics:GeForce 7300/Radeon 9200DirectX®:9.0cHard Drive:2 GB HD
spaceSound:DirectX® compatible'''

specs2 = '''Minimum:OS: Windows VistaProcessor: Intel Core 2 Duo E6550Memory: 3 GB RAMGraphics:
nVidia GeForce 9400 1 Gb/Amd Radeon HD 4550 1 GbDirectX: Version 9.0cStorage: 9 GB available space'''

line = 'hello mr boby'
search = re.findall(r'.*(?=\smr)|(?<=mr\s).*', line, re.X)


##os = re.search(r'(?<=OS:).*(?=processor:)', specs, re.I).group()
##os2 = re.search(r'(?<=OS:).*(?=processor:)', specs2, re.I).group()
##if re.search(r'xp',os2, re.I):
##    print('XP')
##elif re.search(r'vista', os2, re.I):
##    print('Vista')
##elif re.search(r'7', os2, re.I):
##    print(7)
##elif re.search(r'8', os2, re.I):
##    print(8)
##elif re.search(r'10', os2, re.I):
##    print(10)
### what if searches are none, particularly first one (no group())
##
##memory = re.search(r'(?<=memory:).*(?=ram|graphics:)', specs2, re.I).group()
##print(re.search(r'\d', memory).group())

    

for i in search:
    print(i)
