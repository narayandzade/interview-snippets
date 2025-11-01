
import pickle
import threading
import multiprocessing
import time
import copy





# class Number:
#     def __init__(self,value):
#         self.value = value

#     def __add__(self, other):
#         return Number(self.value + other.value)
    
#     def __str__(self):
#         return str(self.value)
    


# n1 = Number(10)
# n2 = Number(10)

# print(n1+n2)
import os
print("Current directory:", os.getcwd())
print("File exists:", os.path.exists("data.xlsx"))

import pandas as pd
import pandas as pd

data = {
    'name': ['Narayan', 'Raj'],
    'age': [30, 25],
    'city': ['Solapur', 'Pune']
}

df = pd.DataFrame(data)
df.to_excel('data.xlsx', index=False, engine='openpyxl')

print("Excel file created!")


df = pd.read_excel('data.xlsx', engine='openpyxl')
print(df)
