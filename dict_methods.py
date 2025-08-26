# Creating a sample dictionary
student = {"name": "Alice", "age": 20, "city": "New York"}

# 1️⃣ clear() - Removes all elements
student.clear()
print("After clear:", student)  # {}

# 2️⃣ copy() - Creates a copy of the dictionary
student = {"name": "Alice", "age": 20, "city": "New York"}
student_copy = student.copy()
print("Copied dictionary:", student_copy)  # {'name': 'Alice', 'age': 20, 'city': 'New York'}

# 3️⃣ fromkeys() - Creates a dictionary with specified keys
keys = ["name", "age", "city"]
default_value = "Unknown"
new_dict = dict.fromkeys(keys, default_value)
print("Dictionary from keys:", new_dict)  # {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

# 4️⃣ get() - Gets the value of a key
print("Get age:", student.get("age"))  # 20
print("Get country:", student.get("country", "Not Found"))  # Not Found

# 5️⃣ items() - Gets all key-value pairs as tuples
print("Items:", student.items())  # dict_items([('name', 'Alice'), ('age', 20), ('city', 'New York')])

# 6️⃣ keys() - Gets all keys
print("Keys:", student.keys())  # dict_keys(['name', 'age', 'city'])

# 7️⃣ pop() - Removes a key and returns its value
age = student.pop("age")
print("Popped age:", age)  # 20
print("After pop:", student)  # {'name': 'Alice', 'city': 'New York'}

# 8️⃣ popitem() - Removes the last inserted key-value pair
last_item = student.popitem()
print("Popped item:", last_item)  # ('city', 'New York')
print("After popitem:", student)  # {'name': 'Alice'}

# 9️⃣ setdefault() - Gets value if key exists, otherwise sets it
student.setdefault("country", "USA")
print("After setdefault:", student)  # {'name': 'Alice', 'country': 'USA'}

# 🔟 update() - Updates the dictionary with another dictionary
student.update({"age": 21, "city": "San Francisco"})
print("After update:", student)  # {'name': 'Alice', 'country': 'USA', 'age': 21, 'city': 'San Francisco'}

# 1️⃣1️⃣ values() - Gets all values
print("Values:", student.values())  # dict_values(['Alice', 'USA', 21, 'San Francisco'])
