# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random
# myList = [random.randint(0,10) for i in range(random.randint(5,5))]
# print(myList)
# list_length = len(myList)
# sumOfElements = 0
# count = 1

# while count < list_length:
#     sumOfElements = sumOfElements + myList[count]
#     count = count + 2

# print("Сумма нечетных элементов:", sumOfElements)


# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# '''Функция создает список чисел из строки, введенной пользователем'''

# def Create_List_By_User():
#     data = input('Введите числа через пробел: ')
#     data = data.split(' ')
#     data = list(map(int,data))
#     return data


# '''Функция создает список произведений парных чисел из списка, введенного пользователем.
# Парой считаются первый и последний элемент, второй и предпоследний и т.д.'''

# def Proivz_By_Pair(numbers):
#     new_data = []
#     i = 0
#     l = len(numbers)
#     while i < l/2:
#         new_data.append(numbers[i]*numbers[l-1-i])
#         i+=1
#     return new_data


# numbers = Create_List_By_User()
# print(numbers, ' -> ', end='')
# print(Proivz_By_Pair(numbers))


# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# '''Функция создает список чисел из строки, введенной пользователем'''

# def Create_List_By_User_Float():
#     data = input('Введите числа через пробел: ')
#     data = data.split(' ')
#     data = list(map(float, data))
#     return data


# '''Функция находит разницу между максимальным и минимальным значением дробной части элементов в списке'''

# def Find_Max_And_Min(numbers):
#     max_number = numbers[0] % 1
#     min_number = max_number
#     for i in numbers[1:]:
#         i = i % 1
#         if i > max_number:
#             max_number = i
#         elif i < min_number:
#             min_number = i
#     return round(max_number - min_number, 2)


# numbers = Create_List_By_User_Float()
# print(numbers, ' -> ', end='')
# print(Find_Max_And_Min(numbers))


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# '''Функция преобразовывает десятичное число в двоичное'''

# def Convert_To_Binary(number: int) -> str:
#     ostatok: str = ""
#     if number // 2 == 0:
#         return 1
#     else:
#         ostatok = str(Convert_To_Binary(number//2)) + str(number % 2)
#         return (ostatok)


# number = int(input('Введите число: '))
# print(Convert_To_Binary(number))

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# def Make_Fibonacci_list(number):
#     lst = [0, 1]
#     i = 1
#     while i < number:
#         lst.append(lst[i-1] + lst[i])
#         i += 1
#     i = 0
#     k = 1
#     while i < number*2:
#         lst.insert(0, lst[i + 1] * k)
#         i += 2
#         k = -k
#     return lst


# number = int(input('Введите число: '))
# print(Make_Fibonacci_list(number))
