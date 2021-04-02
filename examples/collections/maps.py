my_map = {'a': 1, 'b': 2, 100: False}
my_map['c'] = 3
my_map['a'] = 4
print(my_map)
print(my_map['a'])
print(my_map.keys())
print(my_map.values())
print('a' in my_map)
print('z' in my_map)
print(my_map.items())
# print(my_map['z'])  # error
for key in my_map:
    print(key, ':', my_map[key])
for key, value in my_map.items():
    print(key, ':', value)
