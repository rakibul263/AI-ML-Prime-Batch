decimal = float(input("Enter a decimal number : "))

print("Integer part : ", int(decimal))
print("fractional part : ", round(decimal - int(decimal), 2))
