import monkey


def monkey_func(self):

    print("monkey_func() is called")

monkey.A.func = monkey_func


obj = monkey.A()
obj.func()