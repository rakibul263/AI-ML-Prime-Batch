class Person:
  def __init__(self, name, age=None, address=None):
    self.name = name;
    self.age = age;
    self.address = address;

  def display_info(self):
        print(f"Name: {self.name}")
        if self.age is not None:
            print(f"Age: {self.age}")
        if self.address is not None:
            print(f"Address: {self.address}")

p1 = Person("Rakibul", 23);
p2 = Person("Shuvo");
p3 = Person("Murad", 24, "Dhaka");

p1.display_info();
print("---------")
p2.display_info();
print("---------")
p3.display_info();
