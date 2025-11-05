import numpy as np

def sum_rows(l1):
    return [ sum(row) for row in l1 ]

def sum_cols(l1):
    res_sum = []
    for i in range(len(l1[0])):
        col_sum = 0
        for j in range(len(l1)):
            col_sum += l1[j][i]
        res_sum.append(col_sum)
    return res_sum

def sum_cols_zip(l1):
    print(list(zip(*l1)))
    return sum_rows(list(zip(*l1)))


def sum_all(l1):
    return sum(sum_rows(l1))

def sum_cols_rows(l1):
    return sum_rows(l1), sum_cols(l1), sum(sum_rows(l1))

def sum_np_cols_rows(l1):
    row_sum = np.sum(l1, axis=1)
    col_sum = np.sum(l1, axis=0)
    return row_sum.tolist(), col_sum.tolist(), int(np.sum(l1))


if __name__=='__main__':
    num_list = [[2, 4],
                [6, 7],
                [8, 9]]
    print(num_list)
    print(num_list[1])
    print(num_list[1][0])
    num_list[1][0] = 90
    print(num_list)
    print('sum rows:')
    print(sum_rows(num_list))
    print('sum cols:')
    print(sum_cols(num_list))
    print('sum all:')
    print(sum_all(num_list))

    print('sum cols zip:')
    print(sum_cols_zip(num_list))
    print('sum using numpy:')
    print(sum_cols_rows(num_list))
    print(sum_np_cols_rows(num_list))

