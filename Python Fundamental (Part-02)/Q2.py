def even(a, b):
  for var in  range(a, b+1):
    if(var % 2 == 0):
      print(var);

a = int(input("Enter First Number : "));
b = int(input("Enter Second Number : "));

even(a, b);

