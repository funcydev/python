# 1
# name = input("What is your name?: ")
# print(f"Hello {name}")
#
# a = 2
# b = 4
# print(a+b)
#
# print('Hello great programmer!')
#
# first_name = 'Ramil'
# last_name = 'Yunusov'
# age = 19
# print(type(age))
# print(first_name + ' ' + last_name + ' ' + str(age))
# #or
# print(first_name, last_name, str(age))
# print(f'{first_name} {last_name} {age}')
#
# name = input('Type your name dude!: ')
# print('Hello', name, 'How are you?')
# print(f'{name}, are you okay')
#
# num1 = int(input("Type first number: "))
# num2 = int(input("Type second number: "))
# #print(num1 + num2)
# print(f'{num1}+{num2}={num1+num2}')
#
# result1 = 5 + 3
# result2 = 5 - 3
# result3 = 5 * 3
# result4 = 5 / 3
# result8 = 5 % 3    #ostatok ot deleniya
# result5 = 5 ** 3
# result6 = 5 ** 0.5
# result7 = 10 // 3
# print(type(result4))
# print(int(result4))
#
# print(f' result1 = {result1}\n result2 = {result2}\n result3 = {result3} \n result4 = {result4} \n result5 = {result5} \n result6 = {result6} \n result7 = {result7} \n result8 = {result8} ')
#
# a = 1
# a = a + 1
# print(a)
#
#
# 2
# string1 = 'i love python'
# print(type(string1))
# print(string1[0])
# print(string1[4])
# print(string1[-1])
# ###[START:STOP:STEP]
# print(string1[2:6])
# print(string1[::-1])
# print(string1[6::-1])
# string2 = string1.upper()
# print(string2)
# string3 = string2.lower()
# print(string3)
# string4 = string3.capitalize()
# print(string4)
# # print(string4.islower())
# # print(string4.isupper())
# string5 = 'I Love Python'
# string6 = '7'
# print(string5.istitle())
# print(string6.isdigit())
# a = input('type number one: ')
# b = input('type number two: ')
# print(a.isdigit() and b.isdigit())
# if a.isdigit() and b.isdigit():
#     print(int(a) + int(b))
#
# string1 = ' i love python '
# string1 = string1.strip()
# print(string1.startswith('i'))
# print(string1.endswith('n'))
# print(string1[-2] == 'o')
# string1 = ' I love PythoN -'
# string1 = string1.lower().lstrip().rstrip(' -')
# print(string1)
# print(string1.count('o'))
# print(string1.replace('python', 'Java'))
# print(string1.find('o'))

# interface_configuration = '''
# nmcli con mod {0} ipv4.addresses {1}/{2}
# nmcli con mod {0} ipv4.gateway {3}
# nmcli con mod {0} ipv4.dns {4}
# nmcli con up {0}
# '''
# conf = interface_configuration.format('eth0', '192.168.100.1', '24', '192.168.100.254', '8.8.8.8')
# print(conf)

# interface_configuration = '''
# nmcli con mod {name} ipv4.addresses {ip}/{prefix}
# nmcli con mod {name} ipv4.gateway {gw}
# nmcli con mod {name} ipv4.dns {dns}
# nmcli con up {name}
# '''
# conf = interface_configuration.format(name = 'eth0',
#                                       ip = '192.168.100.1',
#                                       prefix = '24',
#                                       gw = '192.168.100.254',
#                                       dns = '8.8.8.8')
# print(conf)
#
# header_tables = "{:15} {:20} {:10} {}"
# line1 = header_tables.format('interface', 'ip', 'prefix', 'gw')
# line2 = header_tables.format('eth0', '192.168.1.10', '24', '192.168.1.1')
# line3 = header_tables.format('eth1', '192.168.1.11', '24', '192.168.1.1')
# line4 = header_tables.format('eth2', '192.168.1.12', '24', '192.168.1.1')
# line5 = header_tables.format('eth3', '192.168.1.13', '24', '192.168.1.1')
#
# print(line1)
# print('-'*60)
# print(line2)
# print(line3)
# print(line4)
# print(line5)
# print('-'*60)
#
# a = 12
# b = 4
# c = a
# a = b
# b = c
# print(a, b)
#
# a = b = 1
# print(a, b)
#
# a, b = 7, 13
# print(a, b)
#
# a = 12
# b = 34
# a, b = b, a
# print(a, b)

string1 = 'python'
print(len(string1))

a = 14
print(id(a))
a = a + 1
print(a)
print(id(a))


