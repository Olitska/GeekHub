# Write a script which accepts a <number> (int)
# from user and generates dictionary in range
# <number> where key is <number> and value is
# <number> * <number>.

number = int(input("Please write a number: "))
dictionary = dict()
for i in range(0, number + 1):
    dictionary[i] = i * i
print(dictionary)
