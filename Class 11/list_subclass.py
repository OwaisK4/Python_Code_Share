class newList(list):
    def __init__(self):
        super().__init__()

    def display(self):
        print(self)


if __name__ == "__main__":
    l = newList()
    l.append(1)
    l.append(2)
    l.display()
