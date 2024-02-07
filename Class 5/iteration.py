sentence = "MongoDB covers a wide range of database examples and use cases"
words = sentence.split()

freq = {}
for word in words:
    freq.setdefault(word, 0)
    freq[word] += 1

# print(freq)
# for key in freq:
#     print(key, freq[key])

for k, v in freq.items():
    print(k, v)
