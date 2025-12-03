class Student:
 def  __init__(self, name, cgpa):
  self.name = name;
  self.cgpa = cgpa;

stu1 = Student("Rakibul", 3.4);
stu2 = Student("Shuvo", 3.2);

print(stu1.name, stu1.cgpa);
print(stu2.name, stu2.cgpa);
