n = int(input())
d = {}
for i in range(n):
    time = input()
    if time not in d:
        d[time] = 1
    else:
        d[time] += 1
        # d[time] = d[time] + 1
    print(d)

# print(d)
maximum = 0
for key in d:
    maximum = max(maximum, d[key])

print(maximum)
