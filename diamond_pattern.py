def diamond_pattern(n):
    # Upper pyramid
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

    # Lower inverted pyramid
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))


# Example: Draw a diamond with 5 rows
diamond_pattern(5)
