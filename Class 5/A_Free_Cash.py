n = int(input())
d = {}
for i in range(n):
    time = input()
    if time not in d:
        d[time] = 0
    d[time] += 1

# print(d)
maximum = 0
for key in d:
    maximum = max(maximum, d[key])

print(maximum)
