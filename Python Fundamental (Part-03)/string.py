word1 = "I Love"
word2 = "Python"
print(len(word1))
print(word1 + " " + word2)

# slicing
print(word2[2:4])

#normal formatting
a = 5
b = 6
sum = a + b
print("Sum is {}".format(sum))
print("Sum of {} & {} is {}".format(a, b, sum))

#index based formatting
print("sum of {1} & {0} is {2}".format(a, b, sum))
