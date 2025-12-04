class Student:
  def __init__(self, name, roll_no, marks):
    self._name = name;
    self._roll_no = roll_no;
    self._marks = marks;

  def set_marks(self, new_marks):
    if(new_marks >= 0 and new_marks <= 100):
      self._marks = new_marks;
    else:
      print("marks must be between 0 to 100.");

  def get_marks(self):
    print(f"Name : {self._name} \nRoll Number : {self._roll_no} \nMarks : {self._marks}");

stu1 = Student("Rakibul", 1263, 87);
stu1.get_marks();
