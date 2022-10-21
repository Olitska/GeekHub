# Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400we(nw,kowe%00koi!jn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345"
# -> просто потицяв по клаві =)
# Створіть ф-цію, яка буде отримувати довільні рядки на зразок цього та яка обробляє наступні випадки:
# - якщо довжина рядка в діапазоні 30-50 (включно) -> прінтує довжину, кількість букв та цифр
# - якщо довжина менше 30 -> прінтує суму всіх чисел та окремо рядок без цифр та знаків лише з буквами (без пробілів)
# - якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)

def big_string(word):
    if 30 <= len(word) <= 50:
        quantity = {'Letters': 0, 'Numbers': 0}
        for i in word:
            if i.isalpha():
                quantity['Letters'] += 1
            if i.isdigit():
                quantity['Numbers'] += 1
        return f'Length of the string is {len(word)}. There are {quantity["Letters"]} letters and {quantity["Numbers"]} numbers.'
    if len(word) < 30:
        numbers_sum = 0
        for x in word:
            if x.isdigit():
                number = int(x)
                numbers_sum += number
        new_string = ''  
        for c in word:  
            if c.isalpha():  
                new_string += c
        return f'The sum of numbers is {numbers_sum}. The string without numbers and symbols is "{new_string}".'
    if len(word) > 50 :
        return f'You are tired. Go home.'

something = str(input('Please write something: '))
print(big_string(something))
