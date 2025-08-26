my_list = [1, 2, 3, 2, 4, 5, 1, 6]

# duplicates = list(set([x for x in my_list if my_list.count(x) > 1]))
# print(duplicates) 
seen = []
duplicates = []
for element in my_list:
    if element  in seen and element not in duplicates:
        duplicates.append(element)
    else:
        seen.append(element)

print(duplicates)




# from collections import Counter

# my_list = [1, 2, 3, 2, 4, 5, 1, 6]

# counts = Counter(my_list)
# duplicates = [item for item, count in counts.items() if count > 1]

# print(duplicates) 
