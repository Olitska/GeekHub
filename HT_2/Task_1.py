# Write a script which accepts a sequence of comma-separated numbers
# from user and generate a list and a tuple with those numbers.

sequence = input("Input a sequence of comma-separated numbers: ")
list = sequence.split(",")
tuple = tuple(list)
print('List:', list)
print('Tuple:', tuple)
