class Student:
  college_name = "ABC College"; #class attributes
  PI = 3.1

  def __init__(self, name, cgpa):
    self.name = name; #instance attributes
    self.cgpa = cgpa;
    self. PI = 3.14

stu1  = Student("Rakibul", 3.23)
print(stu1.name, stu1.cgpa);
print(Student.college_name);
print(stu1.PI);
