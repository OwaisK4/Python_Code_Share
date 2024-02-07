from random import randint

l = []
for i in range(5):
    x = randint(0, 10)
    l.append(x)

# print(l)
# l.sort()
# print(l)

# del l[0]
l = [5, 2, 66, 2, 23, 99]
print(l)
# l.remove(2)
# print(l)
l = sorted(list(set(l)))
print(l)
