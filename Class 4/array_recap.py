import os

path = "/home/owaisk4/Win_backup/Projects/Preply/Michael J./Class 3/"
files = os.listdir(path)
# print(files)
# print(type(files))

for file in files:
    # newFile = file.upper()
    newFile = file[1:]
    print(newFile)
    os.rename(f"{path}{file}", f"{path}{newFile}")
    # print(file)


# a = [5, 1, 2, 5, 7]
# for elem in a:
#     print(elem)

# a.sort()
# a = a[1:]
# a = a[: len(a) - 1]

# print(a)
