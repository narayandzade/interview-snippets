
class A:
    def show(self, amount):
        self.amount = amount
        print(f"show of A{self.amount}")

class B:
    def show(self):
        print(f"Show of B")


class C:
    def show(self):
        print(f"Show of C")


a= A()
b= B()
c = C()

a.show(200)
b.show()