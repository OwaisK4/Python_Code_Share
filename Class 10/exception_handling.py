numer = int(input("Enter numerator: "))
denom = int(input("Enter denominator: "))

try:
    division = numer / denom
except ZeroDivisionError:
    division = 0
finally:
    print(f"Division: {division}")
