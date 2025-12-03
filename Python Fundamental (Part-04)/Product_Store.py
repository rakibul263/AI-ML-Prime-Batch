class Product:
  count = 0;
  def __init__(self, name, price):
    self.name = name;
    self.price = price;
    Product.count += 1;

  def get_info(self):
    print(f"Price of name is {self.name} of Tk. {self.price}");

  @classmethod
  def get_count(cls):
    print(f"Total Objects : {cls.count}");

  @staticmethod
  def calc_discount(price, discount):
    print(f"Discount Price : {price - (discount * price / 100)}")

p1 = Product("Phone", 10_000);
p2 = Product("Laptop", 50_000);
p3 = Product("Tab", 40_000);
Product.get_count();
Product.calc_discount(30_000, 10);


