class Shape:
    def area(self):
        print("This is area")

class Circle(Shape):
    def __init__(self,pi,r):
        self.pi = pi
        self.r = r
    def area(self):
        print(f"Area of circle is {self.pi*self.r**2}")
        
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        print(f"Area of Rectangle is {self.length * self.breadth}")
        
circle = Circle(3.14,5)
rectangle = Rectangle(10,20)
circle.area()
rectangle.area()
        