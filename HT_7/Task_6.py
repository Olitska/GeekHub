# Напишіть функцію,яка приймає рядок з декількох
# слів і повертає довжину найкоротшого слова.
# Реалізуйте обчислення за допомогою генератора
# в один рядок.

string = str(int('Write a string: '))
minimal = min(len(word) for word in string.split())
print(minimal)
