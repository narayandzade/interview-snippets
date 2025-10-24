






# def mydeco(func):
#     def wraper(*args):
#         if 'admin' in args:
#             return func(args)
#         else:
#             print("Invalid Access")
#     return wraper


# @mydeco
# def hello(user):
#     print("welcome admin")



# hello("admin")

# names = ["Alice", "Bob", "Charlie"]
# ids = [101, 102, 103]


# print(dict(zip(ids,names)))



# import numpy as np


# a1 = np.array([1,2,3,4,5])
# a2 = np.array([1,2,3,4,5])

# print(a1+a2)


# import pandas as pd


# a = ["narayan","amruta","abc"]

# data = pd.Series(a, index=["a","b","c"])
# print(data["b"])


# print(range(5))  # Output: [0, 1, 2, 3, 4]



# from abc import ABC , abstractmethod



# class Payement(ABC):
#     @abstractmethod
#     def pay(self):
#         pass

# class UIPayemnt(Payement):
#     def __init__(self,amount):
#         self.amount = amount

#     def pay(self):
#         print(f"Payment of RS{self.amount} made sucessfully using UPI.")


# class CreditCard(Payement):
#     def __init__(self,amount):
#         self.amount = amount

#     def pay(self):
#         print(f"Payment of RS {self.amount} Has done using credit card")
        




# upi = UIPayemnt(100)
# ccard = CreditCard(200)
# ccard.pay()
# upi.pay()


print("--------------------------------------")




# inputs = [ int(i) for i in input("enter numbers").split()]

# print(inputs)


# from multiprocessing import Pool
# import math

# def calculate_factorial(n):
#     return math.factorial(n)

# numbers = [100000, 200000, 300000, 400000]

# with Pool(processes=4) as pool:
#     results = pool.map(calculate_factorial, numbers)

# print(results)




# def reverse_list(l):
#     if len(l)<=1:
#         return l
#     else:
#         return reverse_list(l[1:]) + [l[0]]
    

# print(reverse_list([1,2,3,4,5]))



# import unittest

# def add(a,b):
#     return a+b

# class MYTest(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(1,4),5)



# if __name__ == '__main__':
#     unittest.main()
    
import copy

original = [1, 2, 3]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0] = 100
print(original)  # [1, 2, 3]
print(shallow)