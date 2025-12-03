class Teacher:
 def __init__(self, salary):
  self.salary = salary;

class Student:
  def __init__(self, gpa):
   self.gpa = gpa;

class TA(Teacher, Student):
  def __init__(self, salary, gpa, name):
   super().__init__(salary);
   Student.__init__(self, gpa);
   self.name = name;

  def get_info(self):
    print(f"Teacher Assistant Name is : {self.name} \nSalary : {self.salary} \nCGPA : {self.gpa}");

ta1 = TA(15_000, "9.3", "Shuvo");
ta1.get_info();
