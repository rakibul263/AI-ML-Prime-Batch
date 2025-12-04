color = input("Enter Color (Green, Red, Yellow) : ");

match color:
  case "Green" :
    print("GO.");
  case "Red" :
    print("Stop");
  case "Yellow" :
    print("Look");
  case _:
    print("Wrong Color Entered.")
