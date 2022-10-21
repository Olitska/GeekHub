# Користувач вводить змінні "x" та "y" з
# довільними цифровими значеннями. Створіть
# просту умовну конструкцію (звісно вона повинна
# бути в тілі ф-ції), під час виконання якої буде
# перевірятися рівність змінних "x" та "y" та у
# випадку нерівності - виводити ще і різницю.
# Повинні працювати такі умови (x, y, z заміність
# на відповідні числа:
# x > y;   відповідь - "x більше ніж y на z"
# x < y;   відповідь - "y більше ніж x на z"
# x == y.   відповідь - "x дорівнює y"

def check(x, y):
    if x > y:
        return f'x is more than y by {x - y}.'
    if x < y:
        return f'y is more than x by {y - x}.'
    if x == y:
        return f'x is equal to y.'

user_x = int(input('Please write x: '))
user_y = int(input('Please write y: '))
print(check(user_x, user_y))
