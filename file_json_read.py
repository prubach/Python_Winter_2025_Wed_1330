import json
import os

my_file = os.path.join('data', 'my_file.json')

rates_dict = {}
with open(my_file, 'r') as f:
    rates_dict = json.load(f)

print(rates_dict)
print(rates_dict['EUR'])