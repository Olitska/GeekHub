# Користувачем вводиться початковий і кінцевий рік. Створити цикл, який
# виведе всі високосні роки в цьому проміжку (границі включно). P.S. Рік
# є високосним, якщо він кратний 4, але не кратний 100, а також якщо він
# кратний 400.

def leap_1(x):
    return x % 400
def leap_2_1(x):
    return x % 4    
def leap_2_2(x):
    return x % 100    
start_year = int(input('Please write start year: ')) 
finish_year = int(input('Please write end year: '))
print ('Leap years:')
for year in range(start_year, finish_year + 1):
    if leap_2_1(year) == 0 and leap_2_2(year) != 0 or leap_1(year) == 0:
        print(year)
