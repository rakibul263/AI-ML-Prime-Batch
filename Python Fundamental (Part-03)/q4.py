tup = (1,2,3,4,5,6,7,8,9);
odd = [];
even = [];
for val in tup:
  if(val % 2 == 0):
    even.append(val);
  else:
    odd.append(val);

print(tuple(odd));
print(tuple(even));

