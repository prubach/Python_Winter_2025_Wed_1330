import os.path

my_file = os.path.join('data', 'rates.csv')

with open(my_file, 'r') as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        i += 1
        print(f'{i}: {line}', end='')

cur_dict = {}

def change_curr(cur_dict, from_cur, to_cur, value):
    new_val = 0

    return new_val


print(change_curr(cur_dict, 'PLN', 'USD', 100))

line = 'EUR;2312'
my_arr = line.split(';')
print(my_arr)
s1 = '|'.join(my_arr)
print(s1)
