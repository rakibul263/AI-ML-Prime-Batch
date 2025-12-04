salary = int(input("Enter Your Salary : "));

def Tax(percentage, salary) :
   tax = (percentage/100) * salary;
   return print(tax);

if (salary < 30000) :
  Tax(5, salary);
elif (salary >= 30000 and salary <= 70000 ):
  Tax(15, salary);
elif (salary > 70000) :
  Tax(25, salary);
