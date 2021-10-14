# Задача № 1

# print('Находим сумму n + nn + nnn')
# num = 100
# num_double = num * num
# num_triple = num * num * num
# num = num + num_double + num_triple
# print(num)

# Задача № 2

# print('Вычисляем суму целого числа:')
# num = 73
# num = str(num)
# num_one = num[0]
# num_two = num[1]
# outcome = int(num_one) + int(num_two)
# print(f'Сумма целого числа равна {outcome}')

# Задача № 3

# print('Найти корень 3 степени из 343')
# x = 343
# for i in range(10):
#     root = i ** 3
#     if root == 343:
#         print(i)
##
# print('Находим и удаляем нужный символ в строке\n'
#       '"Привет, как твои дела? Как настроение?"\n')
# txt = 'Привет, как твои дела? Как настроение?'
# search = txt.count('а')     #Находим нужный символ
# txt = txt.replace('а', '')   #Удаляем символ
# print(f'Количество букв "а":{search}\nСтрока с удаленными букквами "а": {txt}')

# Задача № 5

# print('Анкета')
# first_name = input('Введите Ваше имя:')
# last_name = input('Введите Вашу фамилию:')
# age = input('Введите Ваш возраст:')
# from_country = input('Откуда Вы?:')
# print(f'Ваша анкета заполнена:\n'
#       f'Имя:{first_name}\n'
#       f'Фамилия:{last_name}\n'
#       f'Возраст:{age}\n'
#       f'Страна:{from_country}')

# Задача № 6

# print('Проверка номера телефона на наличие букв.')
# phone_number = input('Введите номер телефона:')
# phone_number_len = len(phone_number)
#
#
# def phone_number_examination(number):
#     for i in range(phone_number_len):
#         while number[i].isdigit() or number[i] == ' ' or number[i] == '-' or number[i] == '+':
#             break
#         else:
#             return print('Значение не верно!')
#     print('Ok')
#
#
# phone_number_examination(phone_number)
