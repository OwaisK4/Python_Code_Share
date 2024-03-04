# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation: F_{n} = F_{n-1} + F_{n-2} with seed values and F_0 = 0 and F_1 = 1.

# fibonacci(0) = 0
# fibonacci(1) = 1
# fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)


# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     total = fibonacci(n - 1) + fibonacci(n - 2)
#     return total


memo = {0: 0, 1: 1}


def fibonacci(n):
    print(f"n = {n}, memo = {memo}")
    if n in memo:
        return memo[n]
    total = fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = total
    print(f"Inserted n = {n} in memo table")
    return total


if __name__ == "__main__":
    # n = 10
    # for i in range(0, n + 1):
    #     print(i, fibonacci(i))
    n = 5
    print(fibonacci(n))
    # print(memo[0])
    # print(memo[1])
    # print(memo[2])
