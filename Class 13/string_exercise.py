word = "ambulance"


def reverseCut(word):
    print(word)
    while len(word) > 1:
        word = word[::-1]
        word = word[1:-1]
        print(word)


reverseCut(word)
