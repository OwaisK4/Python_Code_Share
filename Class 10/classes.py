class Car:
    def __init__(self, brand="Honda", year=2007, price=5000):
        print("Created a car")
        self.brand = brand
        self.year = year
        self.price = price

    def display(self):
        print(f"Brand is {self.brand}. Year is {self.year}. Price is {self.price}")

    def addYear(self):
        self.year = self.year + 1


civic = Car()
civic.display()

altima = Car(price=9000, year=2005, brand="Toyota")
altima.display()

civic.addYear()
civic.display()
civic.addYear()
civic.display()

altima.display()
