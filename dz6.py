# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# Для N = 5: 1, -3, 9, -27, 81

# num = int (input("Введите число N"))
# result = []
# for i in range (num):
#     result.append ((-3)**i)
# print (f'Для N={num}: ', end = ' ')
# print (*result, sep=', ')

# Доработка:

# num = int (input("Введите число N: "))
# result = [((-3)**i) for i in range (num)]
# print (f'Для N={num}: ', end = ' ')
# print (*result, sep=', ')

# 2. Для натурального n создать словарь ключ-значение,
# состоящий из элементов последовательности 3n + 1.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n=int(input('Введите n:'))
# my_dict={}
# for key in range(1, n+1):
#     my_dict[key]=3*key+1
# print (f'Для n={n}: ', end = ' ')
# print(my_dict)

# Доработка: 
# n=int(input('Введите n: '))
# my_dict={key: 3*key+1 for key in range(1, n+1)}
# print (f'Для n={n}: ', end = ' ')
# print(my_dict)

# 3. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# number='0.56'
# summa=0
# for i in range(len(number)):
#     if number[i].isdigit():
#         summa+=int(number[i])
# print(summa)

# Доработка:
# number='0.56'
# summa = sum(map(int, str(number).replace('.', '')))
# print(summa)