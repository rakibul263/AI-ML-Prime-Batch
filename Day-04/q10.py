str = input("Enter a string : ");
unique_char = set(str);
count = 0;
for val in unique_char:
  count += 1;
  print(val);
print("Unique Character Count : {}".format(count));
