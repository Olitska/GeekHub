# Write a script that will run through a list of tuples and replace
# the last value for each tuple. The list of tuples can be hardcoded.
# The "replacement" value is entered by user. The number of elements
# in the tuples must be different.

value = input("Please write 'replacement' value: ")
list = [('a', 'b', 'c'), ('d', 'e', 'f', 'g'), ('h', 'i'), ('Anna',)]
print([tuple[:-1] + (value,) for tuple in list])
