class Employee: 
    language = "Python" # This is a class attribute
    salary = 120000000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
 
 
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


Sung_Jin_Woo = Employee("Sung Jin Woo", 120000000, "JavaScript") 
Sung_Jin_Woo.name = "Sung Jin Woo"
print(Sung_Jin_Woo.name, Sung_Jin_Woo.salary, Sung_Jin_Woo.language)

Sung_Jin_Woo.getInfo()

Sung_Jin_Woo.greet()