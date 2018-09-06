"""Script that checks each potential steam appid and, when an entry is present,
 formats the data using regexes to enhance it's readability and inserts it into the database.
 """

from data_extract_and_insert import *
import re
from time import sleep

for i in range(0, 920000, 10):  # There are no steam games with appids greater that 920000
    success = check_id(i)
    if success:
        data = get_api_data(i, 'recommended')
        if data[2] is not None:  # data[2] corresponds to the game's specifications
            specs = re.sub(r'<([^>]*)>', '', data[2])
            rec_specs = re.sub(r'[\t\n\r]', '', specs)
        else:
            rec_specs = None
        data = get_api_data(i, 'minimum')
        if data[2] is not None:
            specs = re.sub(r'<([^>]*)>', '', data[2])
            specs = re.sub(r'[\t\n\r]', '', specs)
            # Some entries had the recommended spec written in the minimum specs section,
            # this therefore need to be checked and separated.
            min_search = re.search(r'.*(?=Recommended)', specs)
            if min_search is None:
                min_search = re.search(r'.*', specs)
            else:
                rec_search = re.search(r'Recommended(.*)', specs)
                rec_specs = rec_search.group()
            min_specs = min_search.group()
        else:
            min_specs = None
        final_data = data[0], data[1], min_specs, rec_specs  # data[0] is the appid and data[1] the name
        insert(*final_data)
    sleep(1)