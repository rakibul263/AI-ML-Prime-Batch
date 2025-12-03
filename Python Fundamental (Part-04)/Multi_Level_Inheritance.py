class Employee:
  start_time = "10AM";
  end_time = "5PM";

class AdminStaff(Employee):
  def __init__(self, role):
    self.role = role;

class Accountant(AdminStaff):
  def __init__(self, salary, role):
    super().__init__(role);
    self.salary = salary;

  def get_info(self):
    print(f"Employee Role is {self.role} and salary is {self.salary}");

acc1 = Accountant(10_000, "CA");
acc1.get_info();
