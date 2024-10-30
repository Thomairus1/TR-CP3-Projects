# polymorphism is when a method or function is changed for a more specific situation
import math
from abc import ABC, abstractmethod 
class Shape(ABC):
    def __init__(self, x):
        self.x = x
    @abstractmethod
    def area(self):
        return 0
    
class Square(Shape):
    def area(self):
        return self.x * self.x
    
class Circle(Shape):
    def area(self):
        return math.pi * self.x**2
    
class Rectangle(Shape):
    def __init__(self, x, y):
        super(). __init__(x)
        self.y = y
    
    def area(self):
        return self.x + self.y

sqr = Square(4)
cir = Circle(4)
rec = Rectangle(5, 3)
shape = Shape(6)
print(sqr.area())
print(cir.area())
print(rec.area())
print(shape.area())