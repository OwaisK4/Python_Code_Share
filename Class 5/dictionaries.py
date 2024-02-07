# array = ["Jan", "Feb", "Mar", "Apr"]

# num = int(input("Enter month number: "))
# print(f"You were born in month: {array[num - 1]}")

# month = input("Enter month name: ")
# print(f"You were born in month: {array[num - 1]}")
# for i in range(len(array)):
#     if array[i] == month:
#         print(f"You were born in month: {i + 1}")
#         break
# else:
#     print("No month found")

# d = {"May": 5, "Jan": 1, "Feb": 2, "Apr": 4, "Mar": 3}
# print(d["Aug"])
# d.setdefault("Jan", 12)
# d["Nov"] = 11
# print(d)
# print(d.get("Aug"))
# d = dict()

sentence = "MongoDB covers a wide range of database examples and use cases, supporting key-value pair data concepts. With its flexible schema and rich query language with secondary indexes, MongoDB is a compelling store for “key-value” data. Learn more in this article and try it with MongoDB Atlas, MongoDBs Database-as-a-Service platform."

words = sentence.split()
print(words)

freq = {}
for word in words:
    freq.setdefault(word, 0)
    freq[word] += 1

for key in freq:
    print(f"{key}: {freq[key]}")
