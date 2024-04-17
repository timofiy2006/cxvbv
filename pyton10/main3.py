class Calculator:
    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Помилка: Ділення на нуль!"

# Створення об'єкту класу Calculator і використання методів для різних арифметичних операцій
calculator = Calculator()
print("Додавання:", calculator.addition(5, 3))
print("Віднімання:", calculator.subtraction(10, 4))
print("Множення:", calculator.multiplication(7, 2))
print("Ділення:", calculator.division(20, 5))
