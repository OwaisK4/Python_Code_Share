from random import randint

numbers = set()
# numbers = []

for i in range(10):
    numbers.add(randint(0, 50))
    # numbers.append(randint(0, 50))

print(type(numbers))
print(numbers)

x = randint(0, 50)
print(f"x = {x}")
# if x in numbers:
#     print(f"Removing x = {x}")
#     numbers.remove(x)
#     print(numbers)
# else:
#     print(f"x not found in numbers")

if x not in numbers:
    print(f"Adding x = {x}")
    numbers.add(x)
    print(numbers)
else:
    print(f"x already present in numbers")
