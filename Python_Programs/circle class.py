class Circle:
    pi = 3.14 # class variable
    def __init__(self,raduis):
        self.raduis=raduis
    def area(self):
        return Circle.pi*self.raduis*self.raduis
    def circumference (self):
        return 2*Circle.pi*self.raduis
c = Circle(4)
print(c.area())
print(c.circumference())
        
