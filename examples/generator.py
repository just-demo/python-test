def sequence():
    yield 0
    yield 1
    yield 2


def squares(n):
    for i in range(n):
        yield i ** 2


for i in sequence():
    print(i, end='')

print()

for i in squares(4):
    print(i, end='')

print()

myList = [x * x for x in range(4)]
for i in myList:
    print(i, end='')

print()

generator = (x * x for x in range(4))
for i in generator:
    print(i, end='')

print()

