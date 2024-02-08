f = open("words.txt", "r")

words = f.readlines()

for i in range(len(words)):
    words[i] = words[i].strip()

print(words[:10])
print(len(words))

# for i in words:
# if i.startswith("j"):
#         print(i)


for word in words:
    if len(word) > 20:
        print(word, len(word))
