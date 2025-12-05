data = True;
flag = False;
line = 1;
with open("word_search.txt", "r") as f:
  while data:
    data = f.readline();
    if "python" in data:
      flag = True;
      break;
    line += 1;

if flag:
  print(f"Word Found at Line : {line}");
else:
  print("Word Not Found");
