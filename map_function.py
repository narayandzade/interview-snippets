# from time import process_time_ns
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
#
# newlist = map(lambda n: n * 2, my_list)
#
# print(list(newlist))
#
#
#

my_list = ["Apple", "BAnana", "Fruit"]

mynewlist = map(lambda s : s[1].lower() =='a', my_list)


print(list(mynewlist))