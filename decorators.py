# #decorator


# def decorator(func):
#     def wrapper(*args):
#         if "admin" in args:
#             func(*args)
#         else:
#             print("access denied")
#     return wrapper


# @decorator
# def hello(user):
#     print("Welcome to dahsboard")



# hello("admin")







def decorator_func(fun):
    def wrapper(*args):
        if 'admin' in args:
            return fun(args)
        else:
            print("invalid creds")
    return wrapper



@decorator_func
def hello(admin):
    print("welcome")

hello('admin')



