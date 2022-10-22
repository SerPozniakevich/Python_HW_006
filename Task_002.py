# Использование map и lambda
# Задача 3 к уроку 2 
# Задайте список из n чисел последовательности (1+ (1/n))^n 
# и выведите на экран их сумму.
# Пример:
# Для n = 5: сумма = 11,55

a = int(input('Введите N: '))
list_a = [x for x in range(1, a + 1)]
list_a = list(map(lambda x : (1 + (1 / x)) ** x, list_a))
sum_sequ = 0
for i in list_a:
    sum_sequ += i
print(f'Для N = {a}: сумма = {round(sum_sequ, 2)}')