import re

specs = """Minimum:OS: Microsoft Windows XP/Vista/7 (32 bit or 64 bit)Processor: Intel® Pentium® 4 2.0 GHz equivalent or faster processorMemory: 256 MB RAMGraphics: 1024x768 or better video resolution in High Color modeStorage: 250 MB available spaceSound Card: DirectSound-compatible sound cardAdditional Notes: 1024 x 768 pixels or higher desktop resolution """

procobj = re.search(r'(?<=processor:).*?(?=memory)', specs, re.I)
processor = re.sub(r'®|\?|™', '', procobj.group())
print(processor)

cpu = "AMD Phenom II X2 555"

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





# print(cpu, clock, model.group(), code.group())


##    for i in range(len(split_cpu)):
##        split_cpu[i] = split_cpu[i].strip()
##        print(split_cpu[i])


