a = [i for i in range(10)]


def printArray(l: list[int], i: int):
    if i == len(l):
        return
    print(l[i], end=" ")
    printArray(l, i + 1)


printArray(a, 0)
