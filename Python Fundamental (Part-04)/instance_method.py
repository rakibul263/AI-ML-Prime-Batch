class Laptop:
  storage_type = "SSD"

  def __init__(self, brand, ram):
    self.brand = brand;
    self.ram = ram;

  def get_info(self):
    print(f"laptop has {self.brand} Brand {self.ram} and storage type {self.storage_type}");

l1 = Laptop("HP", "4GB")
l2 = Laptop("Apple", "8GB");

l1.get_info();
l2.get_info();
