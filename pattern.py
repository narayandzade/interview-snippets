
# for i in range(5):
#     for i in range(5):
#         print("*", end=" ")
#     print("*")

# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *


for i in range(5):
    for i in range(5-i):
        print("*", end="")
    print("*")
