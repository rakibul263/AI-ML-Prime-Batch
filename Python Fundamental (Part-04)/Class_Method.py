class Laptop:
  storage_type = "SSD";

  @classmethod
  def get_class_info(cls):
    print(f"This Laptop storage type is {cls.storage_type} ");


l1 = Laptop();
l1.get_class_info();
Laptop.get_class_info();
