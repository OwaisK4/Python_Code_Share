def has_no_e(words: str):
    for i in words:
        if i == "e":
            return False
    return True


if __name__ == "__main__":
    f = open("words.txt", "r")
    words = f.readlines()
    for i in range(len(words)):
        words[i] = words[i].strip()

    for i in range(len(words)):
        result = has_no_e(words[i])
        if result == True:
            print(words[i])
