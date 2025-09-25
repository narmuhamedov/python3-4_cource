#ООП - Объектно-Орентированное-Программирование

#Наследие классов 

#Родительский класс 
#Дочерний класс


class Car:
    #Метод для создания атрибутов класса!
    def __init__(self, title, age, volume, color):
       self.title = title
       self.age = age
       self.volume = volume
       self.color = color

    #Метод
    def air_conditioner(self,Yes_NO):
        return f'Кондер - {Yes_NO}'
    
    def __str__(self):
        return f'Марка машины - {self.title}\n{self.age}\n{self.volume}\n{self.color}'

car_1 = Car(title='Ваз 2107', age=20, volume=1.6, color='black')
car_2 = Car(title='Toyota Camry', age=5, volume=2.5, color='White')
#Вызов метода
print(car_1.air_conditioner(Yes_NO=False))
print(car_1)
#Вызов метода
print(car_2.air_conditioner(True))
print(car_2)

print('-'*20)

class GermanyCar(Car):
    def __init__(self, title, age, volume, color, esp, airbag, abs):
        super().__init__(title, age, volume, color)
        self.esp = esp
        self.airbag = airbag
        self.abs = abs
    
    def __str__(self):
        return super(GermanyCar, self).__str__()+f"ESP-{self.esp}\nAIRBAG-{self.airbag}\nABS-{self.abs}"
    
    def turbo(self, mark):
        return f'Турбина марки - {mark}'


car_germany_1 = GermanyCar(title='Volkswagen', age=15, volume=2.0, color='black', esp=True, airbag=True, abs=True)
print(car_germany_1.air_conditioner(True))
print(car_germany_1.turbo(mark='BorgWarner'))
print(car_germany_1)


class ElectricCar(GermanyCar):
    def __init__(self, title, age, volume, color, esp, airbag, abs, battery):
        super().__init__(title, age, volume, color, esp, airbag, abs)
        self.battery = battery

    
    def __str__(self):
        return super(ElectricCar, self).__str__()+f'Батарея{self.battery} Км'
    
car_electrik_1 = ElectricCar(title='Lixiang', age=2, volume=333, color='green', esp=True, airbag=True,abs=True, battery=450)
print(car_electrik_1)
print(car_electrik_1.air_conditioner(True))
print(car_electrik_1.turbo(False))