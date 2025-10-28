mi_conjunto = set([1, 2, 3, 4, 5])
print(mi_conjunto)
print(type(mi_conjunto))

mi_conjunto = set({1, 2, 3, 4, 5})
print(mi_conjunto)
print(type(mi_conjunto))

mi_conjunto = {1, 2, 3, 4, 5}
print(mi_conjunto)
print(type(mi_conjunto))

mi_conjunto = {1, 2, 3, 4, 5, 5, 5, 5}
print(mi_conjunto)

# print(mi_conjunto[0])

# mi_conjunto = {1, [2, 3]}

mi_conjunto = { 1, (2, 3)}
print(mi_conjunto)

mi_conjunto = {1, 2, 3, 4, 5}
print(len(mi_conjunto))
print(2 in mi_conjunto)
print(6 in mi_conjunto)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)

s1.add(2)
print(s1)

s1.remove(3)
print(s1)

# s1.remove(6)

s1.discard(6)
print(s1)

s1.discard(4)
print(s1)

s1.pop()
print(s1)

s1 = {1, 2, 3}
print(s1.clear())

s1 = {1, 2, 3}
print(s1.copy())

s1 = {1, 2, 3}
s2 = {1, 2}
print(s1.difference(s2))

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.difference(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.union(s2))





