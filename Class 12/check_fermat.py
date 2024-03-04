def check_fermat(a, b, c, n):
    if n > 2:
        pass
    else:
        return "No, that doesn't work"
    if a**n + b**n == c**n:
        return "Holy smokes..."
    else:
        return "No, that doesn't work"


# Write the therom. a^n + b^n = c^n
# If n > 2 = "Holy smokes...."
# If n <= 2 then print "No, that doens't work"
if __name__ == "__main__":

    # a = 5
    # b = 10
    # c = 3
    n = 3
    for a in range(100):
        for b in range(100):
            for c in range(100):
                string = check_fermat(a, b, c, n)
                print(string)
    pass
