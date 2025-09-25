#функции

#Параметр по умолчанию


# *args, **kwargs

def meal(**kwargs):
    return kwargs

meals = meal(dinner='Plov', breakfast='Cheese Soup')
for key, value in meals.items():
    print(f'{key}-{value}')
print(meals)





# def names(*args):
#     return args

# name = names('Misha', 'Jarred', 'Jensen')
# name = list(name)
# name.append('Rubby')


# typ_name = type(name)
# print(typ_name)
# print(name)



# #return
# def square(a,b):
#     return a*b

# result = square(1,3)
# print(result)





# def student2(name, name1, name2='Adelina'):
#     print(f'{name}-{name1}-{name2}')


# student2('Anna', 'Egor', 'Eleonora')


# def student(name='Dean'):
#     print(f'Hello - {name}')

# student('qwerty')


# def greeting(name):
#     print(f'Hello - {name}')

# while 1:
#     greeting(str(input('What is your name? ')))



# def square(a,b):
#     c = a*b
#     print(f'Площадь - {c}')

# square(1,3)
# square(4,5)
# square(44, 11)
