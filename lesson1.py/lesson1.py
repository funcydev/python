'''
1) Напишите программу, которая спрашивает имя пользователя и затем приветствует его
'''

# name = input("Enter your name: ")
# print('Hello,', name)

'''
2) Напишите программу, которая считывает три числа и выводит их сумму.
'''
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# print(f'Summ of numbers {a}, {b} and {c} is: {a + b + c}')

'''
3) Напишите программу, для решения следующей задачи: n школьников делят k яблок поровну,
неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику? 
Сколько яблок останется в корзинке? Программа получает на вход числа n и k и должна вывести 
искомое количество яблок (два числа).
'''
pupil_num = int(input("Enter amount of pupile: "))
apple_num = int(input("Enter amount of apples: "))
each_get = apple_num // pupil_num
# remain = apple_num
print (f'Each pupil got {each_get} apple')
print (f'')