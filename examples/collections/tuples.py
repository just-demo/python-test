pair = ('a', 'b')
triple = 'c', 'd', 'e'
print('a' in pair)
print('z' in triple)
print(hash(pair))
print(len(pair))
a, b = pair
c, d = ('c', 'd')
e, f = 'e', 'f'
print(a, b, c, d, e, f)
for item in triple:
    print(item)
