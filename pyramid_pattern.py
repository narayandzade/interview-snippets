def pyramid_pattern(n):
    for i in range(1, n+1):
        print(' ' * (n-i) + '*' * (2*i-1))

# Example: Draw a pyramid with 5 rows
pyramid_pattern(5)
