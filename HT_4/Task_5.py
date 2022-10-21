# Ну і традиційно - калькулятор :) Повинна бути
# 1 функція, яка приймає 3 аргументи - один з
# яких операція, яку зробити! Аргументи брати
# від юзера (можна по одному - окремо 2, окремо +,
# окремо 2; можна всі разом - типу 2 + 2).
# Операції що мають бути присутні: +, -, *, /, %,
# //, **. Не забудьте протестувати з різними
# значеннями на предмет помилок!

def calculator(x, y, operation):
    x = float(input('Write first argument: '))
    operation = input("Write operation: ")
    y = float(input('Write second argument: '))
    if operation == '+':
        return f'{x + y}'
    if operation == '-':
        return f'{x - y}'
    if operation == '*':
        return f'{x * y}'
    if operation == '/':
        if y != 0:
            return f'{x / y}'
        else: 
            return "You cannot divide by zero!"
    if operation == '%':
        if y != 0:
            return f'{x % y}'
        else:
            return "You cannot divide by zero!"
    if operation == '//':
        if y != 0:
            return f'{x // y}'
        else:
            return "You cannot divide by zero!"
    if operation == '**':
        if y != 0:
            return f'{x ** y}'
        else:
            return 1
        

a = 0
b = 0
c = ''
print(calculator(a, b, c)) 
