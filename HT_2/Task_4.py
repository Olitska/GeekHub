# Write a script which accepts a <number> from
# user and then <number> times asks user for
# string input. At the end script must print out
# result of concatenating all <number> strings.

number = int(input('Please write a number: '))
result = ""
for n in range(number):
  string_input = input("Please print string: ")
  result = result + string_input
print(result)
