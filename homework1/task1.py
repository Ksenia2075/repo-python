# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным. *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

weekday = int(input('Введите число дня недели: '))

if weekday > 7:
    print('Вы ввели некорректные данные')

elif weekday < 6:
    print('Это рабочий день')

else:
    print('Это выходной')


