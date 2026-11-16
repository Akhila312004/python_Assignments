'''1. Constructor (__init__)'''

# A constructor is a special method in Python that is automatically called when an object is created. It is used to initialize object data.

class Student:
    def __init__(self, name):
        self.name = name
        s1 = Student("Ravi")
        print(s1.name)


'''2. Class Attributes'''

# Variables defined directly inside a class.
# Shared by all objects of that class.

class Student:
    school = "10000 Coders" # Class Attribute


'''3. Instance Attributes'''

# Variables defined inside the constructor using self.
# Different for each object.

class Student:
    def __init__(self, name):
        self.name = name # Instance Attribute


''''Class 1: Student'''


class Student:
    school = "10000 Coders" # Class Attribute
    def __init__(self, name, age):
        self.name = name # Instance Attribute
        self.age = age # Instance Attribute
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("School:", Student.school)

s1 = Student("Ravi", 22)
s1.display()


'''Class 2: Employee'''

class Employee:
    company = "Microsoft" # Class Attribute
    def __init__(self, emp_name, salary):
        self.emp_name = emp_name
        self.salary = salary
    def display(self):
        print("Employee Name:", self.emp_name)
        print("Salary:", self.salary)
        print("Company:", Employee.company)

e1 = Employee("Rahul", 50000)
e1.display()


'''Class 3: Car'''

class Car:
    wheels = 4 # Class Attribute
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def display(self):
        print("Brand:", self.brand)
        print("Color:", self.color)
        print("Wheels:", Car.wheels)

c1 = Car("Toyota", "Black")
c1.display()