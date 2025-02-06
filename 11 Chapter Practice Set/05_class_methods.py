class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()
# A class method is a method that is bound to the class and not the instance of the class. 
# It takes the class itself as its first argument (typically named cls), rather than an instance of the class