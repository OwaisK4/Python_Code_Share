# import math
# num = math.factorial(2)
# print(num)


def factorial(n):
    if n <= 1:
        return 1
    fact = n * factorial(n - 1)
    return fact


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(factorial(num))
