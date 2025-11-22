def count(n):
  cnt = 0;
  while n > 0:
    cnt += 1;
    n = n // 10;
  return cnt;

number = int(input("Enter a number : "))

result = count(number);
print(result)
