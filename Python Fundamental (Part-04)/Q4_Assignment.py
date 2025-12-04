class Shape:
  def area(self):
    pass;

class Circle(Shape):
  def area(self):
    print("Circle!");

class Rectangle(Shape):
  def area(self):
    print("Rectangle");

class Triangle(Shape):
  def area(self):
    print("Triangle");


tri1 = Triangle();
tri1.area();
