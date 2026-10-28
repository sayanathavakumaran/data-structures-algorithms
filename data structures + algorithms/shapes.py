import math
class Shape():
    def __init__(self,colour,name):
        self.colour = colour
        self.name = name
    def show_details(self):
        print(f"colour: {self.colour}")
        print(f"name: {self.name}")
class Rectangle(Shape):
    def __init__(self,width,length,colour,name):
        Shape.__init__(self,colour,name)
        self.width = width
        self.length = length
    def area(self):
        return self.length*self.width

class Circle(Shape):
    def __init__(self,radius,colour,name):
        Shape.__init__(self,colour,name)
        self.radius = radius
    def area(self):
        pi = math.pi
        return round(pi*self.radius*self.radius,2)

rect = Rectangle(2,1,"blue","rectangle")
rect.show_details()
print(rect.area())
circle = Circle(3,"red","circle")
circle.show_details()
print(circle.area())