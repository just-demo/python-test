class ParamAware:
    def increment(self, num):
        return num + 1


class Static:
    @staticmethod
    def increment(num):
        return num + 1


p = ParamAware()
s = Static()

print(p.increment(10))
print(s.increment(10))
print(ParamAware.increment(ParamAware(), 10))
print(Static.increment(10))
