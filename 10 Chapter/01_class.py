class Employee: 
    language = "Python" # This is a class attribute
    salary = 120000000


Tejas = Employee()
Tejas.name = "Tejas" # This is an instance attribute
print(Tejas.name, Tejas.language, Tejas.salary)

rohan = Employee()
rohan.name = "Rohan Zoro Roronoa"
print(rohan.name, rohan.salary, rohan.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class