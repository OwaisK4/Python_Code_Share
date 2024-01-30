# fact(4) = 1 * 2 * 3 * 4 = 24


def factorial(num):
    answer = 1
    for i in range(1, num + 1):
        answer = answer * i
    return answer


for i in range(1, 10):
    a = factorial(i)
    print(a)

# a = 5
# a = a**2
# print(a)


# def funFunction(a):
#     total = a**2
#     return total
# print(total)


# intermediate = funFunction(5)
# final = funFunction(intermediate)
# print(final)
