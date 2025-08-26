
#Python comprehension is a short and efficient way to create
# lists, tuples, dictionaries, and sets using a single line of code

l = [1,2,3,4,5,6,7,8]

result = [i*i for i in l if i%2==0]

print(result)



newlist  =[]
for li in l:
    if li%2==0:
        newlist.append(li*li)

print(newlist)




tuples = (1,2,3,4,5,6,7,8)

tresult = [t*2 for t in tuples if t%2!=0]

print(tresult)


dicts = {
    'first_name': 'Narayan',
    'last_name' : "Zade",
    'age' : 30,
    'gender': "Male"

}

resultdict = {k:v for (k,v) in dicts.items()}

print(resultdict)


newdict = { n: n*n for n in range(1, 10)}
print(newdict)