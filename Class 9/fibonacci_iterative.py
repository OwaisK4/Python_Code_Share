def fibonacci(n):
    fib = [0, 1]
    for i in range(0, n):
        fib.append(fib[-1] + fib[-2])
    return fib[-1]


if __name__ == "__main__":
    # n = 10
    # for i in range(0, n + 1):
    #     print(i, fibonacci(i))
    n = 1000
    print(fibonacci(n))
