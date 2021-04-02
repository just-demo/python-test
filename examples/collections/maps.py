my_map = {'a': 1, 'b': 2}
my_map['c'] = 3
my_map['a'] = 4
print(my_map['a'])
print(my_map.keys())
print(my_map.values())
print('a' in my_map)
print('z' in my_map)
print(my_map.items())
print(my_map['z'])  # error
