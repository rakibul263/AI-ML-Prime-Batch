students = [
    ("Rakib", "Math"),
    ("Shuvo", "Math"),
    ("Nishi", "Physics"),
    ("Anik", "Physics"),
    ("Mim", "English"),
    ("Rafi", "English")
]
# print unique course name
unique_courses = set();
for tup in students:
  unique_courses.add(tup[1]); #course value
print(unique_courses);

# list students enroll english
for name, course in students:
  if(course == 'English'):
    print(name);

