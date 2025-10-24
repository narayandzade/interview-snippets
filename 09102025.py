# # class A:
# #     def show(self):
# #         print("A")

# # class B(A):
# #     def show(self):
# #         print("B")

# # class C(A):
# #     def show(self):
# #         print("C")

# # class D(B, C):
# #     pass

# # d = D()
# # d.show()  # Output: B, Python follows MRO (D → B → C → A)


# # s = "PythonProgramming"


# # print(s[:6])


# # t1 = (1, 2, 3)
# # t2 = (4, 5, 6)

# # t1=t1+t2
# # print(t1)

# # inputs = list(map(int, input("Enter number by space ").split()))
# # print(inputs)




# # inputs = list(int(x) for x in input("enter inputs").split())

# # print(inputs)


# # d = { 
# #     "a":1,
# #     "b": 2,
# #     "c" : 3,
# #     "d" : 4
# # }

# # print(d)
# # d2 = d.copy()
# # d3 = dict(d)
# # print(d2)
# # print(d3)


# # print("--------------delete dic----------------")

# # d3.clear()
# # print(d3)




# x = lambda *args : sum(args)

# print(x(1,2,3,4))

# print((lambda x,y :x+y)(2,3) )

# print("-------------------------------------------------------")
# import multiprocessing

# def task(num):
#     print("Square:", num*num)

# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target=task, args=(5,))
#     p2 = multiprocessing.Process(target=task, args=(10,))
#     p1.start(); p2.start()
#     p1.join(); p2.join()

# x = 10  # Global namespace

# def func():
#     x = 5  # Local namespace
#     print(x)

# func()



# def recursive_list(lst):
#     if len(lst) <=1:
#         return lst
#     else:
#         return recursive_list(lst[1:]) + [ lst[0]]
    


# print(recursive_list([1,2,3,4,5]))

# import unittest

# def add(a, b):
#     return a + b

# class MyTestCase(unittest.TestCase):
#     def test_add_equal(self):
#         self.assertEqual(add(2, 4), 6)
    
#     def test_add_not_equal(self):
#         self.assertNotEqual(add(2, 4), 6)

# if __name__ == "__main__":
#     unittest.main()




#map





# mylist = [1,2,3,4,5,6,7,8,9,10]

# quare_list = list(map(lambda x:x*x, mylist))

# print(quare_list)



# mytuple  = (1,2,3,4,5,6,7,8)

# newt = tuple(filter(lambda x: x%2==0, mytuple))

# print(newt)


# from functools import reduce


# mylist2 = [1,2,3,4,5]

# newlist2 = reduce(lambda x,y : x+y, mylist2)

# print(newlist2)



# mylist = [1,22,3,24,52,6]


# maxnum = mylist[0]
# for num in mylist:
#     if maxnum <num:
#         maxnum = num


# print(maxnum)

# class My:
#     def __init__(self,value):
#         self.value = value

#     def __add__(self,other):
#         return My(self.value + other.value)
    
#     def __str__(self):
#         return str(self.value)
    
# my1 = My(10)
# my2 = My(10)
# my3 = My(10)

# print(my1+my2+my3)





