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
