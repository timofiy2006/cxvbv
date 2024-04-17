class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def display_info(self):
        print(f"Назва: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Рік видання: {self.year}")
        print(f"Жанр: {self.genre}")

# Створення об'єкту класу Book і виведення інформації про книгу
book = Book("Harry Potter", "J.K. Rowling", 1997, "Фентезі")
book.display_info()
