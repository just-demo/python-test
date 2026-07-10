my_str1 = 'single quotes'
my_str2 = "double quotes"
my_str3 = """this
is
a multiline
string"""

print(my_str1)
print(my_str2)
print(my_str3)
print(f"formatted {my_str1}")
print("formatted {}".format(my_str1))
print("formatted {1} {0}".format(my_str1, my_str2))
print("repeat " * 10)


class Demo1:
    pass

class Demo2:
    def __str__(self):
        return "Custom Demo str"

print(str(Demo1()))
print(str(Demo2()))