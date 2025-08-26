#
# builtin_names = dir(__builtins__)
# for name in builtin_names:
#     print(name)


x= 10
def namespacing():
    x= 20
    print(locals())

namespacing()
print(x)

