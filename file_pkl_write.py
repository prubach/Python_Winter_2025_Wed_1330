import os
import pickle

from rates_csv_read_by_amine import cur_dict

my_file = os.path.join('data', 'my_file.pkl')

with open(my_file, 'wb') as f:
    pickle.dump(cur_dict, f)