class Laptop:
  storage_type = "SSD";

  def __init__(self, brand, ram):
    self.brand = brand;
    self.ram = ram;

  def get_init_info(self):
    print(f"Laptop has a {self.brand} {self.ram} and {self.storage_type}");

  @classmethod
  def class_method_info(cls):
    print(f"Laptop has a {cls.storage_type}");

  @staticmethod
  def get_discount(price, discount):
    final_price = price - (discount * price / 100);
    print(f"This Product final price is {final_price}");

l1 = Laptop("Apple", "8GB");
l1.get_init_info();
l1.class_method_info();
l1.get_discount(40_000, 10);
