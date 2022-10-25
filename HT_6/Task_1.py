# Створіть функцію, всередині якої будуть записано СПИСОК із п'яти користувачів (ім'я та пароль). Функція повинна приймати
# три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за
# замовчуванням - <False>).
# Логіка наступна:
#   якщо введено коректну пару ім'я/пароль - вертається True;
#   якщо введено неправильну пару ім'я/пароль:
#     якщо silent == True - функція повертає False
#     якщо silent == False - породжується виключення LoginException (його також треба створити) =))

class LoginException(Exception):
    pass

def user(username, password, silent = False):
    users = [('user_1', 'pass_1'), ('user_2', 'pass_2'), ('user_3', 'pass_3'), ('user_4', 'pass_4'), ('user_5', 'pass_5')]
    user_test = (username, password)
    for pair in users:
        a = False
        if pair == user_test:
            a = True
            return a
    if silent:
        return a
    else:
        raise LoginException("Wrong login and password!")
    
test_username = str(input("Enter username: "))
test_username = test_username.lower()
test_password = str(input("Enter password: "))
print(user(test_username, test_password))
