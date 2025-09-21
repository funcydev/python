# x = -4
# if x > 0:
#     print('x>0')
# elif x < 0:
#     print('x<0')
# else:
#     print('x=0')

# number = int(input('Enter your seat number: '))
# if number % 4:
#     print(f'Number of coupe: {number // 4 + 1}')
# else:
#     print(f'Number of coupe: {number // 4}')

city = input('Enter city name: ').lower()
if not city:
   cnt = len(city)
   if city == 'tashkent'[0:cnt]:
        print('Sunny day in Tashkent')
   elif city == 'london'[0:cnt]:
        print('Renny day in London')
   elif city == 'paris'[0:cnt]:
        print('Lovely day in Paris')
   else:
        print("XZ")
print('You did not set city name')