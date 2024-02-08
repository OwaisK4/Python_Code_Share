num = 3
count = 0
for i in range(num):
    for j in range(num):
        for k in range(num):
            pass
            # print(i, j, k)
            # count += 1
    # print(i)

# print(f"Count = {count}")

# for i in range(num):
#     for j in range(i + 1):
#         print(i, j)

# Let x, y such that x + y = 12
# for i in range(1, 11):
#     for j in range(i, 11):
#         if i + j == 12:
#             print(f"{i} + {j} == 12")

for i in range(5):
    for j in range(5 - i):
        # print(" " * i, end="")
        print(" ", end="")
    print("*")
    # print()
