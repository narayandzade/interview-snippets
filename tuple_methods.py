# Comparing tuples (Python 3 way, as cmp() is removed)
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
print("tuple1 == tuple2:", tuple1 == tuple2)  # False
print("tuple1 < tuple2:", tuple1 < tuple2)      # True (compares element-wise)

# len(): total length of the tuple
t = (10, 20, 30, 40)
print("Length:", len(t))  # 4

# max(): returns the item from the tuple with the maximum value
print("Max:", max(t))  # 40

# min(): returns the item from the tuple with the minimum value
print("Min:", min(t))  # 10

# tuple(seq): converts a list into a tuple
list_seq = [100, 200, 300]
converted_tuple = tuple(list_seq)
print("Converted tuple:", converted_tuple)  # (100, 200, 300)

# sum(): returns the arithmetic sum of all the items in the tuple
print("Sum:", sum(t))  # 10 + 20 + 30 + 40 = 100

# any(): returns True if at least one item in the tuple is True
bool_tuple = (False, 0, None, 5)
print("Any True:", any(bool_tuple))  # True, because 5 is True

# all(): returns True only if all items in the tuple are True
bool_tuple_all = (0, 0, "non-empty" , 0)
print("All True:", all(bool_tuple_all))  # True

# sorted(): returns a sorted version of the tuple as a list
unsorted_tuple = (3, 1, 4, 2)
sorted_list = sorted(unsorted_tuple)
print("Sorted list from tuple:", sorted_list)  # [1, 2, 3, 4]

# index(): returns the index of the first appearance of an item in the tuple
print("Index of 4:", unsorted_tuple.index(4))  # 2

# count(): returns the number of times an item appears in the tuple
sample_tuple = (1, 2, 3, 2, 4, 2)
print("Count of 2:", sample_tuple.count(2))  # 3
