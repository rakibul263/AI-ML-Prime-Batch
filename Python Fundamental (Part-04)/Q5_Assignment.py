class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand;
    self.model = model;

class Car(Vehicle):
  def __init__(self, brand, model, seat):
    super().__init__(brand, model);
    self.seat = seat;

class Bike(Vehicle):
  def __init__(self, brand, model, engine):
    super().__init__(brand, model);
    self.engine = engine;

bike1 = Bike("BMW", "4V", "250GHZ");
print(f"bike brand : {bike1.brand}\nModel : {bike1.model}\nEngine : {bike1.engine}")
