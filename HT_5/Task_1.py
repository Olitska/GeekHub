# Написати функцію <square>, яка прийматиме один аргумент
# - сторону квадрата, і вертатиме 3 значення у вигляді
# кортежа: периметр квадрата, площа квадрата та його
# діагональ.

def square(side):
    return (4 * side, side * side, side * (2 ** (0.5)))

a = int(input('Enter the side of the square: '))

print(square(a))
