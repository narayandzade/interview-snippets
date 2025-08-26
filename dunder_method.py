# from os import access
#
#
# class BanckAccount():
#     def __init__(self, balance):
#         self.balance  = balance
#
#     def __sub__(self, amount):
#         if amount >self.balance:
#             print("Insufficient balance")
#             return  self
#         return BanckAccount(self.balance - amount)
#
#     def __add__(self, amount):
#         return BanckAccount(self.balance + amount)
#
#     def __str__(self):
#         return f"bank balance is {self.balance}"
#
#
#
# bank = BanckAccount(200)
#
# print(bank-201)


# def decorator(func):
#     def wrapper():
#         print("beofre decorator")
#         func()
#         print("after decortor")
#     return  wrapper()
#
#
# @decorator
# def hello():
#     print("hello")
#
# hello



# print(range(5))



# def methodbaba(*args):
#
#     print(args)
#
#
# methodbaba(1,2,3,4 )



# x = map(int , input("enter value by space").split())
#
# print(tuple(x))




d = {'a': 1, 'b': 2, 'c': 3}



d1 = d
d1.pop('a')
print(d)