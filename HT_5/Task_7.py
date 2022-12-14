# Написати функцію, яка приймає на вхід список (через
# кому), підраховує кількість однакових елементів у ньому
# і виводить результат.
# Елементами списку можуть бути дані будь-яких типів.
#   Наприклад:
#   1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ---->
#   "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"

def user_list(n):
    user_list_1 = []
    for i in range(n):
        print('Enter item ', i,  'of the list: ')
        x = input()
        user_list_1.append(x)
    print('User list: ', user_list_1)    
    return user_list_1    

def same(list_1):
    elements = {i:list_1.count(i) for i in list_1}
    print('The number of identical elements: ')
    for key in elements:
        print(key, ': ', elements[key])    
    return elements
    
number = int(input('Enter the number of list items: '))
test_list = user_list(number)  
same(test_list)
