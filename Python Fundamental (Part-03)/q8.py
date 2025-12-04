list1 = [1,2,3,4,5];
list2 = [3,4,5,6,7];

flag = False;
for val in list1:
  if val in list2:
    flag = True;
    break;

if flag:
  print("Common Element Found");
else:
  print("Common Element is Not Found");
