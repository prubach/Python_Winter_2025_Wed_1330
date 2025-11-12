import os


def change_curr(cur_dict, from_cur, to_cur, value):
    new_val = 0

    # Check if both currencies exist
    if from_cur in cur_dict and to_cur in cur_dict:
        # Convert from source currency to USD, then to target
        usd_value = value / cur_dict[from_cur]
        new_val = usd_value * cur_dict[to_cur]
    else:
        print("Error")
    return round(new_val, 2)


cur_dict = {}
with open('data/rates.csv', 'r') as f:
    next(f) # skip first line - header
    for line in f:
        cur, rate = line.strip().split(';')

        cur_dict[cur] = float(rate.replace(',', '.'))
        #cur_dict[cur] = float(rate)

print(cur_dict)

print(change_curr(cur_dict, 'PLN', 'USD', 100))
