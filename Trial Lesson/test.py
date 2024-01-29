num = input("Enter a number: ")
print(num)
print(type(num))


num = int(num)

remainder = num % 2
if remainder == 0:
    print("Number is even")
else:
    print("Number is odd")

# counter = 0
# while counter < num:
#     counter += 2

# if counter == num:
#     print("Number is even")
# else:
#     print("Number is odd")
