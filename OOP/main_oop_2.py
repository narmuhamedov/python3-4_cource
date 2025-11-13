#Абстракция, Инкапсуляция и полиморфизм

# from abc import ABC, abstractclassmethod

# class Animal(ABC):
#     @abstractclassmethod
#     def make_sound(self):
#         pass


# class Dog(Animal):
#     def make_sound(self):
#         print('Гав Гав')

# class Cat(Animal):
#     def make_sound(self):
#         print('Мяу-Мяу')

# dog = Dog()
# cat = Cat()

# dog.make_sound()
# cat.make_sound()



#Инкапсуляции

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
    
#     def deposit(self, amount):
#         self.__balance += amount
    

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f'Снято: {amount}')
#         else:
#             print('Недостаточно средств')
    
#     def get_balance(self):
#         return self.__balance

# acount = BankAccount(1000)
# acount.deposit(500)
# acount.withdraw(200)

# print(acount.get_balance)
#

#Полиморфизм

# class EnglishHello:
#     def speak(self):
#         print('Hello')

# class GermanyHallo:
#     def speak(self):
#         print('Hallo')

# class RussianPrivet:
#     def speak(self):
#         print('Привет')

# greeting = [EnglishHello(), GermanyHallo(), RussianPrivet()]
# for hi in greeting:
#     hi.speak() # Одинаковый вызов во всех ф-циях