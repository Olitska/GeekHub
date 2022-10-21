# Створіть 3 різних функції (на ваш вибір). Кожна з цих
# функцій повинна повертати якийсь результат (напр. інпут
# від юзера, результат математичної операції тощо). Також
# створіть четверту ф-цію, яка всередині викликає 3
# попередні, обробляє їх результат та також повертає
# результат своєї роботи. Таким чином ми будемо викликати
# одну (четверту) функцію, а вона в своєму тілі - ще 3.

def function_1(x):
    return x ** 1

def function_2(x):
    return x ** 2
    
def function_3(x):
    return x ** 3

def function_4(x):
    return function_1(x) + function_2(x) + function_3(x)

number = int(input('Please write number: '))    
print(function_4(number))   
