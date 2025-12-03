class Employee:
  start_time = "10AM";
  end_time = "6PM";

  def change_time(self, new_end_time):
    self.end_time = new_end_time;

class Teacher(Employee):
  def __init__(self, subject):
    self.subject = subject;

t1 = Teacher("Math");
t1.change_time("5AM");
print(t1.start_time, t1.end_time)

