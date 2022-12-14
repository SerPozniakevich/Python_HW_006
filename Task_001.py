# Использование List Comprehension
# Задача № 3 к третьему семинару.
# "Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
#Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.19"

import copy
import random
from random import uniform


# list1 = [1.1, 1.2, 3.1, 5, 10.01]
# print(list1)
# f = 2  # количество знаков после запятой. 
# def num_fract(x):
#     return round(list1[x] % 1, f)

# list_fract = [num_fract(i) for i in range(len(list1)) if list1[i] % 1 != 0]

# print(list_fract)

# max_num = max(list_fract)
# min_num = min(list_fract)
# print(f'{list1}, => {max_num - min_num}')

# Var student

input_list = list(map(lambda x : float(x), input("Введите дробные числа через пробел:\n").split()))
fract_list = [round(i % 1, 2) for i in input_list if i % 1 != 0]
print(f'Для списка: {input_list}\nразница между MAX и MIN значений дробной части равна:\n {max(fract_list) - min(fract_list)}')