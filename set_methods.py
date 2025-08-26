# Creating sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# add(): Adds an element to the set
set1.add(6)
print("After add:", set1)  # {1, 2, 3, 6}

# clear(): Removes all elements from the set
set3 = {7, 8, 9}
set3.clear()
print("After clear:", set3)  # set()

# copy(): Returns a copy of the set
set_copy = set1.copy()
print("Copy of set1:", set_copy)  # {1, 2, 3, 6}

# difference(): Returns a set containing the difference
print("Difference:", set1.difference(set2))  # {1, 2, 6}

# difference_update(): Removes items found in another set
set1.difference_update(set2)
print("After difference_update:", set1)  # {1, 2, 6}

# discard(): Removes a specified item without error if not found
set2.discard(4)
print("After discard:", set2)  # {3, 5}

# intersection(): Returns common elements
set1 = {1, 2, 3}
print("Intersection:", set1.intersection(set2))  # {3}

# intersection_update(): Keeps only common elements
set1.intersection_update(set2)
print("After intersection_update:", set1)  # {3}

# isdisjoint(): Returns True if no common elements
set4 = {10, 11}
print("Is Disjoint:", set1.isdisjoint(set4))  # True

# issubset(): Checks if set1 is subset of set2
set5 = {1, 2}
print("Is Subset:", set5.issubset({1, 2, 3}))  # True

# issuperset(): Checks if set contains another set
print("Is Superset:", {1, 2, 3}.issuperset(set5))  # True

# pop(): Removes and returns an arbitrary element
set6 = {10, 20, 30}
print("Popped item:", set6.pop())  # Removes any item

# remove(): Removes a specific element, raises error if not found
set6.remove(20)
print("After remove:", set6)  # {30}

# symmetric_difference(): Returns elements in either set, but not both
set7 = {1, 2, 3}
set8 = {3, 4, 5}
print("Symmetric Difference:", set7.symmetric_difference(set8))  # {1, 2, 4, 5}

# symmetric_difference_update(): Updates with symmetric difference
set7.symmetric_difference_update(set8)
print("After symmetric_difference_update:", set7)  # {1, 2, 4, 5}

# union(): Returns all unique elements from both sets
set9 = {5, 6}
print("Union:", set8.union(set9))  # {3, 4, 5, 6}

# update(): Adds elements from another set
set8.update(set9)
print("After update:", set8)  # {3, 4, 5, 6}



print(eval("10 + 23"))


import array


a = array.array('i',[1,2,3,4,5])

print(a)