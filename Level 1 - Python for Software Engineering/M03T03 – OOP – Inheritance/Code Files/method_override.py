#user inputs that ask for the name, age, hair colour, and eye colour of a person

name = input("Enter your name: ")
age = int(input("Enter your age: "))
hair_colour = input("Enter your hair colour: ")
eye_colour = input("Enter your eye colour: ")

#Create an Adult class and print statements about the person using the user inputs
class Adult:
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    def can_drive(self):
        if self.age >= 18:
            print(f"{self.name} is old enough to drive.")
        else:
            print(f"{self.name} is not old enough to drive.")

#create subclass of Adult class name Child and print statements about the person using the user inputs
class Child(Adult):
    def __init__(self, name, age, hair_colour, eye_colour):
        super().__init__(name, age, hair_colour, eye_colour)

    def can_drive(self):
        print(f"{self.name} is a child and cannot drive.")

#define age and if they can drive or not
if age >= 18:
    person = Adult(name, age, hair_colour, eye_colour)
else:
    person = Child(name, age, hair_colour, eye_colour)
person.can_drive()
