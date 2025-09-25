# Переменные типы данных ввод информации и вывод информации
stunent_name_1 = 'Adelina'
stunent_name_2 = 'Aida'
stunent_name_3 = 'Daniyar'

#Нельзя называть переменные
# c цифры, с точки, и какие то зарезервированные слова
#Зарезервированные слова посмотреть в интернете
#student 1 = X
print(f'Привет я {stunent_name_1}')
print(f'Привет я {stunent_name_2}')
print(f'Привет я {stunent_name_3}')

name = input('как вас зовут? ')
print(f'Привет {name.capitalize()}')


#Типы данных
#string(str), integer(int), float 
#string - это тип данных который имеет любой символ который находится в кавычках
#integer - любое число 1234534
num1 = 12
num2 = 13
print(num1+num2)
#float - число с плавающей точкой - 23.23
num1 = 12.2222
num2 = 13.23
summ_ = num1+num2
print(round(summ_, 2))