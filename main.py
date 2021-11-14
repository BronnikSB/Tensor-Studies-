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

# Задача № 7

# num = 0
#
# while num != 123:
#     if num % 2 == 0:
#         print(num)
#     num += 1

# num = 123
#
# for i in range(1, num):
#     if i % 3 == 0:
#         print(i)

# Задача № 8

# number_str = 5
# for i in range(1, number_str + 1):
#     symbol = "* " * i
#     print(i, symbol)

# Задача № 9

# num_user = int(input("Введите целое число:"))
# num_user_new = num_user - 2
# while num_user_new > 1:
#     num_user *= num_user_new
#     num_user_new -= 2
# print(num_user)

# Задача №10

# num_use = int(input("Введите число от 1 до 100:"))
# lst = []
# for i in range(num_use):
#     if i == 0:
#         continue
#     elif i % 5 == 0:
#         lst.append(i)
# print(lst)
# # Задача № 11
#
# num_max = max(lst)
# num_min = min(lst)
# index_max = lst.index(num_max)
# index_min = lst.index(num_min)
# lst[index_min], lst[index_max] = lst[index_max], lst[index_min]
# print(lst)
#
# # Задача №12

# sum_lst = 0
# multiply_lst = 1
# for i in lst:
#     sum_lst += i
#     multiply_lst *= i
# print(f"Сумма элементов списка равна:{sum_lst}\n"
#       f"Произведение элементов списка равно:{multiply_lst}")

# Задача № 13

# lst = [
#     {"Наименование": "Бекон",
#      "Цена": 150},
#     {"Наименование": "Яйца",
#      "Цена": 86},
#     {"Наименование": "Сливки",
#      "Цена": 210},
#     {"Наименование": "Паста",
#      "Цена": 250},
#     {"Наименование": "Базилик",
#      "Цена": 70}
# ]
# for i in range(len(lst)):
#     for k in range(0, len(lst) - i - 1):
#         if lst[k]["Цена"] < lst[k + 1]["Цена"]:
#             lst[k]["Цена"], lst[k+1]["Цена"] = lst[k+1]["Цена"], lst[k]["Цена"]
# print(lst[0], "\n", lst[1], sep="")

# Задача № 14

# def cash(deposit, perсent_years, years):
#     summa = deposit * (perсent_years / 100)
#     summa *= years
#     summa += deposit
#     return summa
#
#
# print(cash(1000000, 6.5, 5))

# Задача № 15

# def palindrome(a):
#     """Функция проверяет является ли число Палидромом,
#     где a - принимаемое значение"""
#     num_palindrome = str(a)
#     if num_palindrome[0:] == num_palindrome[::-1]:
#         return True
#     return False
#
#
# print(palindrome(121))

# Задача № 16

# num_div = 0
#
# for i in range(2, 1000):
#     for k in range(2, i):
#         if i % k == 0:
#             num_div += 1
#     if num_div == 0:
#         print(i)
#     else:
#         num_div = 0

# Задача № 17
#
# num_use = 123123
# print(type(num_use))
#
#
# def happiness_exam(num):
#     happiness_num = []
#     for i in list(str(num)):
#         happiness_num.append(int(i))
#     if happiness_num[0:3] == happiness_num[3:6]:
#         return print(f'{num} является счасливым числом')
#     return print(f'{num} является не счастливым числом')
#
#
# happiness_exam(num_use)

## Задача № 18

txt = input("Введите текст:")


def double_count(txt_use):
    """Функция ищет повторяющиеся элементы в списке
    и выводить колиество повторений(В данной функции
    не используется метод .count())"""
    count = []  # Список, который хранит в себе элемент, дубль которого мы ищем
    punctuation = ['.', ',', '!', '?', '(', ')', ':', ';', '"', '/', '-']  # Список знаков препинания, для удаления
    double_dict = {}
    value_num = 1 # Количество повторяющихся элементов
    value_r = 1 # Начало диапазона для поиска дублей
    for i in punctuation:
        txt_use = txt_use.replace(i, "") # Удаляем знаки препинания
    txt_use = txt_use.lower().split() # Приводим текст к одному регистру, переводим в список
    # ----------- Увеличиваем диапазон если он равен i(если не увеличить, то в список будут попадать значения, которые
    # не повторяются)
    for i in range(len(txt_use)-1):
        if value_r == i:
            value_r += 1
    # ------------------------------------------------
        if txt_use[i] in double_dict: # Проверяем есть ли в списке уже данный ключ, если нет, то не берем его
            continue
        else:
            count.append(txt_use[i]) # добавляем элемент который будем проверять на дубль
        for k in range(value_r, len(txt_use)):
            if txt_use[k] == count[0]: # Поиск дубля
                value_num += 1
                double_dict[count[0]] = value_num # Обновляем счетчик
        value_num = 1
        count = [] # Обнуляем, что бы в списке был только тот элемент, который проверяем
    print(double_dict)


double_count(txt)