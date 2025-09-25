# Словари

student = {
    'name': 'Radomir',
    'age': 27,
    'work': 'IT', 
    'laptop': True,
    False : 'Moto',
    1997 : 28
}

#Создание пары-ключи и значение
for key, value in student.items():
    print(f'{key} - {value}')



#Update
student['work'] = 'IT Teacher'
student.update(age=28)

#Удаление
del student[1997]


#Добавление данных
student['car'] = 'golf4'
student.update(childhood='Karakol')

#Вывод данных
print(student['name'])
print(student)

