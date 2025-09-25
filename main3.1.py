# Кортеж
data_type = (1, 4, 5, 67 , 'sdfsdf', 'fsdfsdf')
print(data_type.count(1))
print(data_type.index('sdfsdf'))

data_type = list(data_type)

data_type.append('hello')

data_type = tuple(data_type)




# people = ['Maria', 12, 'Adam', 11, True, 'Liza', 18]
# age = []
# name = []
# for i in people:
#     if type(i) == str:
#         name.append(i)
#     else:
#         age.append(i)


# age.remove(True)
# age.sort()

# print(age)
# print(name)