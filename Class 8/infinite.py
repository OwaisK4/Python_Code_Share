def func(num):
    if num > 990:
        return
    print(f"Hello world from func {num}")
    func(num + 1)
    print(f"Hello world from func {num}")


if __name__ == "__main__":
    func(0)
