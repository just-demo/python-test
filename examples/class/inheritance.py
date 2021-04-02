class Parent(object):
    def __init__(self):
        self.value = 1

    def get_value(self):
        return self.value


class Parent2(object):
    def get_value(self):
        return 100


class Child1(Parent):
    pass


class Child2(Parent):
    def get_value(self):
        return super().get_value() + 2


class Child02(Parent2, Child2):
    def get_value(self):
        return super().get_value() + 10


class Child12(Child1, Child2):
    def get_value(self):
        return super().get_value() + 10


p = Parent()
c1 = Child1()
c2 = Child2()
c02 = Child02()
c12 = Child12()

print(p.get_value())
print(c1.get_value())
print(c2.get_value())
print(c02.get_value())
print(c12.get_value())

print(dir(p))
