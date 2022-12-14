# Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
# - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
# - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
# - якесь власне додаткове правило :)
# Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним
# текстом.

class LoginException(Exception):
    pass

def user(username, password):
    if len(username) >= 3 and len(username) <= 50:
        if len(password) >= 8 and password.isalpha() == False and password.isalnum():
            return True 
    if len(username) < 3 or len(username) > 50:
        raise LoginException("Wrong login!")
    if len(password) < 8 or password.isalpha() or password.isalnum() == False:
        raise LoginException("Wrong password!")
    
test_username = str(input("Enter username: "))
test_password = str(input("Enter password: "))
print(user(test_username, test_password))
