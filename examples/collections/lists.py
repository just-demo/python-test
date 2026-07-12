my_list = ['a']
my_list.extend(['b', 'c'])
my_list.append('d')
my_list.insert(3, 'e')
my_list.remove('c')
print(my_list.pop(1))
my_list += ['b', 'c']
print(sorted(my_list))
my_list.sort()
my_list.reverse()
print(my_list)
print(len(my_list))
print('a' in my_list)
print('z' in my_list)
print(my_list[:2])
print(my_list[2:])
print(my_list[:])
for item in my_list:
    print(item)

print("Demo copy:")
a = [1, 2, 3, 0, 0, 0]
b = [4, 5, 6]
a[3:] = b
print(a)

print("Demo swap:")
my_list = ['a', 'b']
my_list[0], my_list[1] = my_list[1], my_list[0]
print(my_list)