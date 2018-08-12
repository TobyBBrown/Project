from single_api_insert import *
import re
from time import sleep

for i in range(0, 920000, 10):
    success = check_id(i)
    if success:
        data = get_api_data(i, 'recommended')
        if data[2] is not None:
            specs = re.sub(r'<([^>]*)>', '', data[2])
            rec_specs = re.sub(r'[\t\n\r]', '', specs)
        else:
            rec_specs = None
        data = get_api_data(i, 'minimum')
        if data[2] is not None:
            specs = re.sub(r'<([^>]*)>', '', data[2])
            specs = re.sub(r'[\t\n\r]', '', specs)
            min_search = re.search(r'.*(?=Recommended)', specs)
            if min_search is None:
                min_search = re.search(r'.*', specs)
            else:
                rec_search = re.search(r'Recommended(.*)', specs)
                rec_specs = rec_search.group()
            min_specs = min_search.group()
        else:
            min_specs = None
        final_data = data[0], data[1], min_specs, rec_specs
        insert(*final_data)
    sleep(1)