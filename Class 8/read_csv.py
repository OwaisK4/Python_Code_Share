f = open("times.csv", "r")
threads = []
times = []

data = f.readlines()
for i in range(1, len(data)):
    data[i] = data[i].strip()
    temp = data[i].split(",")
    # print(temp)
    threads.append(temp[0])
    times.append(temp[1])

print(data)
print(threads)
print(times)
