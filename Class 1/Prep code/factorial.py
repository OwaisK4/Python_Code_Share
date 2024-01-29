# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     return fact


def factorial(n):
    if n <= 1:
        return 1
        # pass
    else:
        print(f"n = {n}")
        return n * factorial(n - 1)


answer = factorial(int(input()))
print(answer)
