import json
import os
from rates_csv_read_by_amine import cur_dict

my_file = os.path.join('data', 'my_file.json')

with open(my_file, 'w') as f:
    json.dump(cur_dict, f)