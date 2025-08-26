def pattern(n):
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces+ stars + spaces)


pattern(5)


def mydecorator(func):
    def wrapper(*args):
        if 'admin' not in args:
            print("access denied")
            return
        return func(*args)
    return wrapper


@mydecorator
def hello(user):

    print("welcome Baba")


hello('admin')


def passstatement(n):
    for i in range(n):
        if i == 3:
            # We want to skip any special logic for i == 3
            pass
        else:
            print(f"Square of {i} is {i * i}")



passstatement(10)



def pattern2(n):
    for i in range(n+1):
        print("*" *i)
    for i in range(n-1, 0,-1):
        print("*" *i)


pattern2(5)