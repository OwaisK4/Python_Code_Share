class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        print("Student: ", end="")
        print(self.name, self.age, self.subject)


class Teacher(Person):
    def __init__(self, name, age, experience):
        super().__init__(name, age)
        self.experience = experience

    def display(self):
        print("Teacher: ", end="")
        print(self.name, self.age, self.experience)


if __name__ == "__main__":
    # p = Person("Owais", 20)
    # p.display()
    # s = Student("Owais", 20, "science")
    # s.display()
    object: Person
    choice = int(input("Enter a choice: (0 for student, 1 for teacher)"))
    if choice == 0:
        object = Student("Owais", 20, "science")
    else:
        s = Teacher("Owais", 20, "science")
