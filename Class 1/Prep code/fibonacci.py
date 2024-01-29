memo = {0: 0, 1: 1}


def fibonacci(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memo[n]


answer = fibonacci(int(input()))
print(answer)

# for i in range(10):
#     print(fibonacci(i), end=" ")
