class BankAccount:
  def __init__(self, name, balance):
    self.name = name; #public
    self.__balance = balance; #private

  def get_balance(self):
    return self.balance;

  def set_balance(self, new_balance):
    self.balance = new_balance;

acc1 = BankAccount("Rakibul Hasan", 40_500);
acc2 = BankAccount("Zaidur Rahaman", 60_000);
acc2.set_balance(80_000);
print(acc2.get_balance());
# print(acc1.name, acc1.balance);
print(acc1._BankAccount__balance)
