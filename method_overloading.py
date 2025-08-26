


class A:

    def __init__(self, *args):
        self.args = args

    def add(self):

        return  sum(self.args)



a = A(1,2,3,4)
print(a.add())