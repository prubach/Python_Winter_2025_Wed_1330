a = 4
if a >= 5:
    print('a is greater than or eq 5')
elif a >=3:
    print('a is greater than or eq 3')
else:
    print('a is less 5')

s = 'abcd'
match s:
    case 'a':
        print('s is a')
    case 'abc':
        print('s is abc')
    case _:  # default case - not matched previously
        print('s is unknown')

a = 10
if a % 2 == 0:
    print('a is even')
else:
    print('a is odd')

b = 10 if a > 5 else 100
print(f'b is {b}')
