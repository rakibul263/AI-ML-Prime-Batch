from abc import ABC, abstractmethod

class Employee(ABC):
  @abstractmethod
  def calculate_salary(self):
    pass

class Intern(Employee):
  def calculate_salary(self):
    print("Intern Salary.");

class FullTimeEmployee(Employee):
  def calculate_salary(self):
    print("FullTimeEmployee Salary");

class ContractEmployee(Employee):
  def calculate_salary(self):
    print("ContractEmployee salary");


c1 = ContractEmployee();
c1.calculate_salary();
