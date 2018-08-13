import re

specs = """Minimum:Requires a 64-bit processor and operating systemOS: Windows 7 SP1 or newerProcessor: Intel® i5-4590 / AMD FX 8350 equivalent or greaterMemory: 8 GB RAMGraphics: NVIDIA GeForce® GTX 970 / AMD Radeon? R9 290 equivalent or greaterDirectX: Version 11Storage: 2300 MB available space"""

procobj = re.search(r'(?<=processor:).*?(?=memory)', specs, re.I)
processor = re.sub(r'®|\?|™', '', procobj.group())
print(processor)

cpu = "Intel Core i5-4590 @ 3.30GHz"

if '@' in cpu:
    splitproc = re.findall(r'.*(?=\s@) | (?<=@\s).*', cpu)
    name = splitproc[0].strip()
    clock = splitproc[1].strip()
##    for i in range(len(splitproc)):
##        splitproc[i] = splitproc[i].strip()
##        print(splitproc[i])

print(name, clock)
