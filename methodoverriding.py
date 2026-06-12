class Shape:
    def show(self):
        print("Area of shape")

class Circle(Shape):
    def show(self):
        print("Area of Circle")

class Rectangle(Shape):
    def show(self):
        print("Area of rectangle")

shapes = [Circle(), Rectangle()]

for s in shapes:
    s.show()    # runtime polymorphism occur.....