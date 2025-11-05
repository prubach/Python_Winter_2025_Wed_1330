from time import time
import numpy as np

from lists_2D import sum_cols_rows, sum_np_cols_rows

def time_func(func, n):
    t0 = time()
    #print(f'Running {func.__name__} with n={n}')
    print(f'Running {func.__name__}')
    res = func(n)
    #print(f'Result={res}')
    t1 = time()
    elapsed = round(t1 - t0, 8)
    print(f'Done in {elapsed} sec')


def gen_lists(n):
    list_of_lists = []
    for i in range(n):
        list_of_lists.append(np.random.randint(100000, size=(10000, 10000)))
    return list_of_lists

mtrx = gen_lists(1)[0]
print(mtrx)
print('---------------')
time_func(sum_cols_rows, mtrx)
#c, r, s = sum_cols_rows(mtrx)
#print(c[:3], r[:3], s)
print('------Numpy----')
#c, r, s = sum_np_cols_rows(mtrx)
#print(c[:3], r[:3], s)
time_func(sum_np_cols_rows, mtrx)




