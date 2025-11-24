def sum_to_n_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

print("Sum using while loop:", sum_to_n_while(10))
