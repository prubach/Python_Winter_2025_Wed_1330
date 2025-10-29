def sum_and_multiply(a, b):
    summ = a + b
    def multiply(c, d):
        print(a, b, c, d)
        return c * d
    multi = multiply(a, b)
    print(f'multi={multi}')
    #return summ, multi

print('inside function')

#print(sum_and_multiply(10, 3))
sum_and_multiply(10, 3)