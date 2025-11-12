import pickle
import os

my_file = os.path.join('data', 'my_file.pkl')

rates_dict = {}
with open(my_file, 'rb') as f:
    rates_dict = pickle.load(f)

print(rates_dict)
print(rates_dict['EUR'])