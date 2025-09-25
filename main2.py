#Условные операторы и циклы
#if elif else / 
#while - работает до сих пор пока значение не станет ложным

while True:
    color = input('enter your color ')
    if color == 'green':
        print(f'You can go')
    elif color == 'yellow':
        print(f'you can see speed or stop')
    elif color == 'red':
        print(f'STOP')
    else:
        print('Look at situation')
    
    answer = input('Вы точно хотите выключить светофор? ')
    if answer == 'да':
        break
    elif answer == 'нет':
        continue