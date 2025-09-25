import random
from random import randint, sample
import datetime

print('Добро пожаловать в наше казино')
start = datetime.datetime.now()

try:
    cash = int(input('введите вашу ставку '))
    print(f'Вы внесли - {cash}')
    if cash <= 0:
        print('Не пытайтесь обмануть систему')
except:
    print('Произошла ошибка в системе!')

while cash !=0:
    try:
        bet = int(input(f'какую ставку {cash} желаете поставить? '))
        if bet > cash:
            print('у вас нехватает денег!')
            continue
        person = [randint(1,6), randint(1,6)]
        computer = [randint(1,6), randint(1,6)]
        print(f'у тебя выпало - {person}\nу соперника{computer}')

    except:
        print('вводите только цифры!')
    
    if sum(person) > sum(computer):
        cash += bet
        print(f'Winner - {cash}')
    
    elif sum(person) < sum(computer):
        cash -= bet
        print(f'Lose - {cash}')
    else:
        print(f'Ничья - У вас бабосиков {cash}')
    
endgame = datetime.datetime.now() - start
print(f'Вы провели в игре - {endgame}')







# #try exept - исключения
# while 1:
#     try:
#         num1 = float(input('введите первое число'))
#         operation = str(input('выберите операцию + - * /'))
#         num2 = float(input('введите второе число'))
    
#         if operation == "+":
#             print(f'{num1}+{num2}={num1+num2}')
#         elif operation == '-':
#             print(f'{num1}-{num2}={num1-num2}')
#         elif operation == '*':
#             print(f'{num1}*{num2}={num1*num2}')
#         elif operation == '/':
#             print(f'{num1}/{num2}={num1/num2}')
#         else:
#             print('операция неизвестна')
#             continue
#     except: 
#          print('пожалуйста вводите только цифры и операции + - * /')
#     game_exit = input('хотите выключить программу? Да/Нет - ').upper()
#     if game_exit == 'ДА':
#         print('Досвидания')
#         break
#     elif game_exit == 'НЕТ':
#         continue
#     else:
#         print('Программа сломана!!!')
#         break



# try:
#     number_1 = '12'
#     number_2  = '12'
#     print(number_1+number_2)
# except:
#     print('что то пошло не так проверь код')
