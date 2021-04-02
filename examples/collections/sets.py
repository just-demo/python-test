my_set = set('a')
my_set.update(['b', 'c'])
my_set.add('d')
my_set.remove('c')
my_set |= {'b', 'c'}

print(my_set)
print(len(my_set))
print('a' in my_set)
print('z' in my_set)

my_set2 = {'a', 'z'}
print(my_set.intersection(my_set2))
print(my_set.union(my_set2))
