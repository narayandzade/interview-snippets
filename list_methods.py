# Creating a sample list
numbers = [5, 2, 9, 1, 5]

# 1️⃣ sort() - Sorts the list in ascending order
numbers.sort()
print("Sorted list:", numbers)  # [1, 2, 5, 5, 9]

# 2️⃣ append() - Adds a single element to the end of the list
numbers.append(10)
print("After append:", numbers)  # [1, 2, 5, 5, 9, 10]

# 3️⃣ extend() - Adds multiple elements from an iterable
numbers.extend([7, 3])
print("After extend:", numbers)  # [1, 2, 5, 5, 9, 10, 7, 3]

# 4️⃣ index() - Returns the first occurrence index of a value
print("Index of 5:", numbers.index(5))  # 2

# 5️⃣ max() - Returns the maximum value in the list
print("Max value:", max(numbers))  # 10

# 6️⃣ min() - Returns the minimum value in the list
print("Min value:", min(numbers))  # 1

# 7️⃣ len() - Returns the length of the list
print("Length of list:", len(numbers))  # 8

# 8️⃣ list() - Converts a tuple into a list
tuple_data = (11, 12, 13)
converted_list = list(tuple_data)
print("Converted list:", converted_list)  # [11, 12, 13]

# 9️⃣ type() - Returns the class type of an object
print("Type of numbers:", type(numbers))  # <class 'list'>

# 🔟 count() - Returns the count of a value in the list
print("Count of 5:", numbers.count(5))  # 2

# 1️⃣1️⃣ insert() - Inserts a value at a specific index
numbers.insert(2, 100)
print("After insert:", numbers)  # [1, 2, 100, 5, 5, 9, 10, 7, 3]

# 1️⃣2️⃣ remove() - Removes the first occurrence of a value
numbers.remove(5)
print("After remove:", numbers)  # [1, 2, 100, 5, 9, 10, 7, 3]

# 1️⃣3️⃣ pop() - Removes and returns the element at the given index (default last)
popped_value = numbers.pop()
print("Popped value:", popped_value)  # 3
print("After pop:", numbers)  # [1, 2, 100, 5, 9, 10, 7]

# 1️⃣4️⃣ reverse() - Reverses the list in place
numbers.reverse()
print("Reversed list:", numbers)  # [7, 10, 9, 5, 100, 2, 1]

# 1️⃣5️⃣ copy() - Returns a shallow copy of the list
numbers_copy = numbers.copy()
print("Copied list:", numbers_copy)  # [7, 10, 9, 5, 100, 2, 1]
