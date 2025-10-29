for i in range(10):
    print(i, end=' ')

print('\n----')
for i in range(2, 10, 3): # from 2 to 10 (not including) with a step of 3
    print(i, end=' ')

print('\n----')
for i in reversed(range(2, 10, 3)):
    print(i, end=' ')

print('\n----')
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    if a > 8:
        break
    print(a, end=' ')


a: int = 5457
