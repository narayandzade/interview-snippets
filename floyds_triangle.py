def floyds_triangle(n):
    num = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(num, end=" ")
            num += 1
        print()

# Example: Draw Floyd’s triangle with 5 rows
floyds_triangle(4)
