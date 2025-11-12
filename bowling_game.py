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

print(f'Method: count_bowls_loop: {count_bowls_loop(6)}')
print(f'Method: count_bowls_range: {count_bowls_range(6)}')
print(f'Method: count_bowls_sequence: {count_bowls_sequence(6)}')
