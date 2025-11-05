import os.path

#my_file = 'data\\my_file.txt'  # Only on Windows
#my_file = 'data/my_file.txt'
#my_file = 'C:/Users/prubac/PycharmProjects/Python_Winter_2025_Wed_1330/data/my_file.txt'
#my_file = 'C:/TEMP/my_file.txt'
#my_file = '../../../../TEMP/my_file.txt'
my_file = os.path.join('data', 'my_file.txt')

cwd = os.getcwd()
print('cwd={cwd}'.format(cwd=cwd))


f = open(my_file, 'r')
lines = f.readlines()
i = 0
for line in lines:
    i += 1
    print(f'{i}: {line}', end='')
f.close()

print('--------')

with open(my_file, 'r') as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        i += 1
        print(f'{i}: {line}', end='')
