



# mylist = [1,2,3,4,5]
# print(mylist)


# mytuple  = (1,2,3,4,5)
# print(mytuple)



# def mydecor(func):
#     def wraper(username, password):
#         if username == 'admin' and password == 'admin':
#             return func(username,password)
#         else:
#             print("invalid username or assword ")
#     return wraper


# @mydecor
# def login(username,password):
#     print(f"welcome to dashbaord, {username}")




# login(username="admin", password="admin")



#list comprehesion 


# mylist = [1,2,3,4,5,6]

# newlist = [ x for x in mylist if x%2==0 ]
# print(newlist)



# mydict = {
#     1:1,
#     2:2,
#     3:3,
#     4:4,
#     5:5
# }


# newdict = { k:v*v for (k,v) in mydict.items() }

# print(newdict)



# def mygenerator(n):
#     for i in range(1, n+1):
#         yield i*i




# gen = mygenerator(3)

# print(next(gen))
# print(next(gen))
# print(next(gen))



# myiterator = iter(['a','b','c','d'])

# print(next(myiterator))


# import pandas as pd 

# data = {
#     "name" : ["Narayan","Amruta", "Advika"],
#     "age" : [34,23,5],
#     "location" : ["pune","pune","pune"]

# }

# pddata = pd.DataFrame(data)
# print(pddata)



# dicttionary = {
#     "name": "Narayan",
#     "name" : "Amruta"
# }

# print(dicttionary)


