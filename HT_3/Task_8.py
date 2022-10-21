# Створити цикл від 0 до ... (вводиться користувачем).
# В циклі створити умову, яка буде виводити поточне
# значення, якщо остача від ділення на 17 дорівнює 0.

def operation(number):
    return number % 17
finish_number = int(input('Please write a number: '))   
for i in range(finish_number + 1):
    if not operation(i) == 0:
        continue
    print(i)
