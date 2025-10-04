
# import pdb

# class Math:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         pdb.set_trace()
#         return Math(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"Math({self.x}, {self.y})"

# m1 = Math(2, 4)
# m2 = Math(3, 4)

# print(m1 + m2)  # Output: Math(5, 8)



# import logging
# from itertools import zip_longest

# logging.basicConfig(level=logging.INFO)

# l1 = [1, 2, 3, 4, 5]
# l2 = [2, 3, 4, 5]

# zipped = list(zip_longest(l1, l2, fillvalue="-"))
# print(zipped)

# newl1, newl2 = zip(*zipped)

# logging.info("This is a debug log")
# print(newl1)
# print(newl2)

# def findmissing_number(numbers):
#     maxnumber = max(numbers)
#     missing = []

#     for i in range(1,maxnumber):
#         if i not in numbers:
#             missing.append(i)

#     print(missing)


# findmissing_number([1,3,4,5,6])


# def sum_of_products(mylist):
#     n = len(mylist)
#     total_sum = 0
#     for i in range(n):
#         for j in range(i):

#             total_sum+= mylist[i]*mylist[j]
#     return total_sum






# print(sum_of_products([1,2,3,4,5]))





#anagram check








def fibonacci1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)

for i in range(10):
    print(fibonacci1(i))
print("------------------------------------")

def fibonacci2(n):
    a = 0
    b= 1
    for _ in range(n):
        print(a)
        a,b = b,a+b


fibonacci2(10)



def find_duplicate(mylist):
    seen = set()
    duplicate  = []
    for i in mylist:
        if i not in seen:
            seen.add(i)
        else:
            duplicate.append(i)
    return duplicate



print(find_duplicate([1,2,2,3,4,5,5]))


def return_index(e, l):

   for  k , v in enumerate(l):
       if v==e:
           return k
       

print(return_index(3, [1,2,3,4,5,6]))



def second_highest(mylist):
    unique = list(set(mylist))
    maxn = max(unique)
    unique.remove(maxn)
    maxn = max(unique)
    print(maxn)







second_highest([34,56,78,99,89,12])





def generator(n):
    for i in range(1,n+1):

        yield i*i



x = generator(5)

print(next(x))
print(next(x))
print(next(x))


i = iter(['A','B','C'])

print(next(i))
print(next(i))
print(next(i))





permissions = {
    frozenset(['read','write','update']): "Admin",
    frozenset(['read']) : "User"
}




print(permissions[frozenset(['read'])])


print("--------------------------------------------------")
for i in range(1, 11):
    if i < 10:
        print(i, end=",")
    else:
        print(i)



print("-------------------------------------------")

t = (1,2,3,4,5)
print(t)
print(t.count(2))
print(t.index(2))


print("----------------------------------")


s = { 1,2,3,4,5}


s.add(22)
s.discard(222)
news  = s.intersection({6,7,5})
print(news)





def any_dict(**kwargs):
    for k , v in kwargs.items():
        print(f"{k} : {v}")




any_dict(name ="narayan")




file = open("demo.txt", "w")
file.write("Hello, Python!")
file.close()


file2 = open("demo.txt", "r")
print(file2.read())


try:
    x = int(float("100.2"))
except ValueError as e:
    print(e)
else:
    print(x)
finally:
    print("finally")


# import requests

# response = requests.get('https://example.com')
# print(response.text)



fname  = "Narayan"
lname = "Zade"

print("My Name is {} {}".format(fname, lname))
print(f"My Name is {fname} {lname}")

print("----------------------------------")


dct = {'A': 1, 'B': 2, 'C': 3}
print(list(dct.keys()))


from abc import ABC , abstractmethod


class Payement(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UPIPayment(Payement):
    def pay(self, amount):
        print(f"Payment of RS {amount} is successfully done using UPI Method")





upi = UPIPayment()
upi.pay(1000)
