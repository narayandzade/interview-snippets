import copy

mylist  = [1,2,[1,2,3,4]]


newlist = copy.deepcopy(mylist)

newlist[2][1] = 33
print(f"My origibal list :",mylist)
print(f"shaloow copy is :", newlist)