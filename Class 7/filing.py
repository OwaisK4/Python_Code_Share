f = open("input.txt", "r")

# for line in f:
#     print(line, end="")

# text1 = f.read()
text2 = f.readlines()
print(text2)
print(type(text2))

f.close()
