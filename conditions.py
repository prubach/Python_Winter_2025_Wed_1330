p = False
q = False
print(f'p={p} q={q}')

if p != True:
    print('p!=True')

if p and q:
    print('p and q')
else:
    print('not p or not q')

if p or q:
    print('p or q')
else:
    print('not p and not q')

if p ^ q:
    print('p XOR q')
else:
    print('not p XOR q')