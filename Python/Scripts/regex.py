import re


def os_regex(specs):
    if specs is not None:
        os_obj = re.search(r'(?<=os:).*(?=processor:)', specs, re.I)
        if os_obj is not None:
            os = os_obj.group()
            if re.search(r'xp', os, re.I):
                return 'XP'
            elif re.search(r'vista', os, re.I):
                return 'Vista'
            elif re.search(r'7', os, re.I):
                return '7'
            elif re.search(r'8', os, re.I):
                return '8'
            elif re.search(r'10', os, re.I):
                return '10'
    return None


def mem_regex(specs):
    if specs is not None:
        mem_obj = re.search(r'(?<=memory:).*(?=ram|graphics:)', specs, re.I)
        if mem_obj is not None:
            mem = mem_obj.group()
            mem_num = re.search(r'\d', mem)
            if mem_num is not None:
                return mem_num.group()
    return None
