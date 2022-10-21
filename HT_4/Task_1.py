# Написати функцію season, яка приймає один аргумент (номер місяця від 1
# до 12) та яка буде повертати пору року, до якої цей місяць належить
# (зима, весна, літо або осінь). У випадку некоректного введеного значення
# - виводити відповідне повідомлення.

def season(x):
    if x <= 0 or x > 12:
        y = 'Number is not correct. Please write a month number (1 - 12).'
    if 0 < x < 3 or x == 12:
        y = 'Winter'
    if 2 < x < 6:
        y = 'Spring'
    if 5 < x < 9:
        y = 'Summer'
    if 8 < x < 12:
        y = 'Autumn'
    return y    
        
month = int(input('Please write month number: '))
print (f'It is {season(month)}.')
