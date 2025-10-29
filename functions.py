def sum_it(a :int = 10, b: int = 50) -> int:
    summ = a + b
    #d = 100
    #def multiply(a, b):
    #    return a * b
    #summ = multiply(a, b)
    return summ

c = sum_it(2, 3)
c = sum_it(a=70, b=20)

#print(f'd={d}') # - not visible
print(f'c={c}')

b = 3
#d = 0
if b > 5:
    d = 9
else:
    d = 80

print(f'd={d}')

def sum_and_multiply(a, b):
    summ = a + b
    def multiply(c, d):
       return c * d
    multi = multiply(a, b)
    print(f'multi={multi}')
    #return summ, multi

print('inside function')

#print(sum_and_multiply(10, 3))
sum_and_multiply(10, 3)