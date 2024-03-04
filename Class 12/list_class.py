class newList(list):
    def __init__(self):
        super().__init__()

    def display(self):
        print(self)

    def double(self):
        for i in range(len(self)):
            self[i] = self[i] * 2

    def append(self, value) -> None:
        super().append(value)
        super().append(value)
        return self


if __name__ == "__main__":
    l = newList()
    for i in range(10):
        l.append(i)
    l.display()
    l.append(100)
    l.display()
    # l.double()
    # l.display()
