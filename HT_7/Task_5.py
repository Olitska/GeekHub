# Напишіть функцію,яка приймає на вхід рядок та повертає
# кількість окремих регістро-незалежних букв та цифр, які
# зустрічаються в рядку більше ніж 1 раз.
# Рядок буде складатися лише з цифр та букв (великих і малих).
# Реалізуйте обчислення за допомогою генератора в один рядок.

def count_repeated_symbols(string):
    list=[]

    for letter in string:
        if string.count(letter) >= 2:
            if letter not in list:
                list.append(letter)


    for item in list:
        if item != " ":
            print(item, string.count(item))


count_repeated_symbols(str(input('Please write a string: ')))
