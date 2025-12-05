try:
  x = int(input("Enter x : "));
  ans = 10 / x;
except ZeroDivisionError:
  print(f"Division by 0 is not allowed.");
except ValueError:
  print(f"Enter valid input");
else:
  print(f"ans is : {ans}")
finally:
  print("End of our program");
