def number_pyramid(n):
    for i in range(1, n+1):
        print(' ' * (n-i) + ''.join(str(j) for j in range(1, i+1)))

# Example: Draw a number pyramid with 5 rows
number_pyramid(5)
