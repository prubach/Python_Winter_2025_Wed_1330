l1 = [1, 2, 3, 2, 1]
#l1 = (1, 2, 3, 2, 1)
print(l1[4])
l1.insert(2, 4)
print(l1)
l1.remove(3)
print(l1)
l1.pop(1) # remove at index 1
print(l1)
l1.append(7)
print(l1)
print('-----------')
s1 = set(l1)
print(s1)
#print(s1[3]) - no indices for elements


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(my_dict['d'])

my_dict_i = {10: 'ten', 20: 'twenty'}
print(my_dict_i[10])

print(my_dict_i.keys())
print(type(my_dict_i.keys()))
print(my_dict_i.values())
print(type(my_dict_i.values()))
print(my_dict_i.items())

for key, value in my_dict_i.items():
    print(key, value)

for key in my_dict_i.keys():
    print(key, my_dict_i[key])

