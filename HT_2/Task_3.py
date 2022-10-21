# Write a script which accepts a <number> from user and print
# out a sum of the first <number> positive integers.

number = int(input("Input a number: "))
sum = (number * (number + 1)) / 2
print("Sum of the first", number ,"positive integers:", sum)
