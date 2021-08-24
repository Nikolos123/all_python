"""
Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации (нуль необходимо
исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
“elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""
import random


def ran(start, end, num) :
    rand_l = []
    rand_d = {}

    while num > 0:
        num = random.uniform(start, end)
        if num:
            rand_l.append(num)
            rand_d[f'elem_{num}'] = num
            num -= 1
    print(rand_l)
    print(rand_d)


if __name__ == '__main__':
    ran(-55, 31, 102)