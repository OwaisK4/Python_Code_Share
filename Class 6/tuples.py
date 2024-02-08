def func(n):
    sum = n + 2
    multiple = n * 2
    divisor = n / 2
    return sum, multiple, divisor


def print_name(t):
    print(type(t))
    print(t[0], t[1], t[2])
    # t[0] = "None"


if __name__ == "__main__":
    # n = int(input("Enter number: "))
    # answer = func(n)
    # print(answer)
    # n1, n2, n3 = func(n)
    # print(type(n1), type(n2))
    # print(n1, n2)
    names = ("Owais", "Ali", "Khan")
    print_name(names)
    print(names)
