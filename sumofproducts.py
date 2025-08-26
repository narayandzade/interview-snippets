

#sum of products in possible pairs


def sumofproducts(numbers):
    total_sum = 0
    n = len(numbers)

    for i in range(n):
        for j in range(i + 1, n):
            total_sum += numbers[i] * numbers[j]

    return total_sum


# Example usage:
numbers = [1, 2, 3, 4, 5]
result = sumofproducts(numbers)
print(result)  # Output: 35

# 1*2 + 1*3 + 1*4 + 1*5
# 2*3 + 2*4 + 2*5
# 3*4 + 3*5
# 4*5
