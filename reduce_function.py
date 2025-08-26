#
# from functools import reduce
#
#
#
# mylist  = [1,2,3,4,5,5,6]
#
#
# result = reduce(lambda x,y : x+y, mylist)
# print(result)
#
#
# newstringlist  = ['Hello','Narayan' , 'Zade', 'How', 'are','You','?']
#
# mystring = reduce(lambda x,y: x+" "+y,newstringlist)
# print(mystring)
#
#
# words = ["apple", "banana", "cherry", "blueberry", "grape"]
#
#
# word = reduce(lambda x, y :x if len(x) > len(y) else y ,words)
# print(word)
#
#

from functools import  reduce
names = ['Narayan', 'AMruta', 'Advikka']

namelist = reduce(lambda acc , name : sorted(acc + [name]),names, [] )
names.sort()

print(names)