class BankAccount :
  def __init__(self, account_number, owner_name, balance):
    self.account_number = account_number;
    self.owner_name = owner_name;
    self.balance = balance;

  #method
  def deposit(self, amount):
    if(amount > 0):
      self.balance += amount;
      print(f"Deposit Balance : {amount} and current balance : {self.balance}");
    else:
      print(f"Deposit amount must be positive.");

  def withdraw(self, amount):
    if(amount <= 0):
      print(f"Withdraw amount must be positive. Your balance is : {self.balance}");
    else:
      self.balance -= amount;
      print(f"Withdraw successful. Your Current amount is : {self.balance}");

  def check_balance(self):
    print(f"your current balance is: {self.balance}")

BankAccount1 = BankAccount(1263, "Rakibul", 50_000);
BankAccount1.check_balance();
BankAccount1.withdraw(20_000);
BankAccount1.deposit(500);
