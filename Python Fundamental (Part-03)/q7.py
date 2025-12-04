str = input("Enter a string:");

count = 0;

for val in str:
  if(val == " "):
    count += 1;

print(count);
