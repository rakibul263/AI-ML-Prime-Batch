f = open("sample.txt", "r");
data = f.read();
# data = f.readline();
print(data);

f = open("sample.txt", "a");
f.write("Daffodil International University");
