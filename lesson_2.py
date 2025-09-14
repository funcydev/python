'''
1) Составить три формы присвоение следующего вида x, y, z = y, z, x (придумать способ применения )


'''

'''
2) Распечатать: сложение, вычитание, умножение, деление, возведение в степень следующих переменных:

num1 = '3.14'
num2 = '4'
'''
# num1 = '3.14'
# num2 = '4'
# num3, num4 = (float(num1)), (int(num2))
# num5 = str(num3 + num4)
# num6 = str(num3 - num4 - 0.001)
# num7 = str(num3 * num4)
# num8 = str(num3 / num4)
# num9 = str(num3 ** num4)
# print(f'{num1} + {num2} = {num5[0:4]}')
# print(f'{num1} - {num2} = {num6[0:5]}')
# print(f'{num1} * {num2} = {num7[0:6]}')
# print(f'{num1} / {num2} = {num8[0:5]}')
# print(f'{num1} ** {num2} = {num9[0:5]}')

'''
3) Воспользуйтесь различными методами строк
str1 = ' << pYthOn -   '
str2 = '   pYthOn \n .   '
str3 = ' (( pYthOn - :+   '
'''
# str1 = ' << pYthOn -   '
# str2 = '   pYthOn \n .   '
# str3 = ' (( pYthOn - :+   '
# print(str1[4:10].lower())
# print(str2[3:9].upper())
# print(str3[4:10].capitalize())

'''
4) Обработайте каждую переменную и получите результат как на картинке:
'''
# string1 = 'I love python'
# string2 = 'Hello my dear friend'
# string3 = 'полиморфизм'
# print(string1[::-1])
# print(string2[6:8], string2[14:])
# string4 = (string3[0], string3[2])
# ********************************************************************


'''
5) С помощью метода строк Замените слово show на display и создайте другую переменную
'''
# show = 'show ip interface brief'
# show2 = show.replace('show', 'display')
# print(show)
# print(show2)
'''
6)В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом. 
Напишите программу, которая определяет номер купе, в котором находится место 
с заданным номером (нумерация мест сквозная, начинается с 1).Формат входных данных:
'''
num = int(input('enter your seat number: '))
num2 = (num + 3) // 4
print(f'Your seat in coupe {num2}')
'''
7) Подсчитайте общее количество цифр в числе.
Например, число 75869 , поэтому на выходе должно быть 5 .
'''
# num = '75869'
# print(len(num))
