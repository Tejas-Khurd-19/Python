class Employee: 
    language = "Python" # This is a class attribute
    salary = 120000000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


Naruto = Employee()
# Naruto.language = "JavaScript" # This is an instance attribute

Naruto.getInfo() 
# Employee.getInfo(Naruto)

Naruto.greet()
