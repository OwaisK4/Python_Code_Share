:
    if n == 0:
        return 0
    if n == 1:
        return 1
    total = fibonacci(n - 1) + fibonacci(n - 2)
    return total