def reverse_string(s, index):
    if index >= len(s):
        return
    reverse_string(s, index + 1)
    print(s[index], end=" ")
    print(f"index = {index}")
    return


if __name__ == "__main__":
    s = "country"
    reverse_string(s, 0)
    print()
