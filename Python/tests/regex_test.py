import re
import requests

line = 'hello mr boby'
searchobj = re.search(r'(?<=hello ).*(?=boby)',line)
print(searchobj.group())
