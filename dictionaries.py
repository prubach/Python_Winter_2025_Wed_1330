#my_dict_i = {10: 'ten', 20: 'twenty', 30: 'thirty'}

my_list = [('EUR', 4.2), ('USD', 3.5),('EUR', 4.0)]
print(my_list)
my_dict = dict(my_list)
print(my_dict)

print(my_dict.get('PLN')) # - if key not found returns None
#print(my_dict['PLN'])  # - if key not found raises KeyError

print(my_dict.get('PLN', 5.0)) # - if key not found returns None

vals = [x[1] for x in my_list]
print(vals)

print(f'Sum={sum(vals)}')
print(f'Max={max(vals)}')
print(f'Min={min(vals)}')