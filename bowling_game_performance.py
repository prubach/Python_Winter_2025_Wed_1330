from performance_test import time_func
from bowling_game import count_bowls_range, count_bowls_sequence, count_bowls_recursion, count_bowls_loop

#n = 998
n = 200000000
time_func(count_bowls_loop, n)
time_func(count_bowls_range, n)
time_func(count_bowls_sequence, n)
#time_func(count_bowls_recursion, n)