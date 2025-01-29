# Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self, n):
        self.temp = n 
    
    def square(self):
        print(f"The square is {self.temp*self.temp}")

    def cube(self):
        print(f"The cube is {self.temp*self.temp*self.temp}")

    def squareroot(self):
        print(f"The squareroot is {self.temp**1/2}")

a = Calculator(4)
a.square()
a.cube()
a.squareroot()