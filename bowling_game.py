"""
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
n - number of rows

How many bowls are necessary given the "n"
"""
def count_bowls_loop(n):
    bowls_count = 0
    for bowl in range(1, n + 1):
        bowls_count += bowl
    return bowls_count

def count_bowls_range(n):
    return sum(range(1, n+1))

def count_bowls_sequence(n):
    return round((n * (n + 1))/2)

def count_bowls_recursion(n):
    if n == 1:
        return 1
    else:
        prev_sum = count_bowls_recursion(n - 1)
        cur_sum = prev_sum + n
        return cur_sum


if __name__ == '__main__':
    n = 999
    print(f'Method: count_bowls_loop: {count_bowls_loop(n)}')
    print(f'Method: count_bowls_range: {count_bowls_range(n)}')
    print(f'Method: count_bowls_sequence: {count_bowls_sequence(n)}')
    print(f'Method: count_bowls_recursion: {count_bowls_recursion(n)}')
