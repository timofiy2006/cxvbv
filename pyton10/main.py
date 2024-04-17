class Car:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Рік випуску: {self.year}")
        print(f"Швидкість: {self.speed} км/год")

# Створення об'єкту класу Car і виведення інформації про автомобіль
car = Car("BMW", "X5", 2020, 250)
car.display_info()
