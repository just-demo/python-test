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

my_list = [x * x for x in range(4)]
for i in my_list:
    print(i, end='')

print()

generator = (x * x for x in range(4))
for i in generator:
    print(i, end='')

print()

print("Demo fibonacci generator:")


def fibonacci():
    a, b = 0, 1
    while True:
        print("fibonacci before")
        yield a
        a, b = b, a + b
        print("fibonacci after")

fib = fibonacci()
for _ in range(5):
    print(next(fib))