# Завдання 1: Принцип єдиного обов'язку (Single Responsibility Principle - SRP)
# Спроектуйте і реалізуйте клас "Користувач" (User), який відповідає принципу SRP.
# В цьому класі повинні бути методи для створення користувача, оновлення даних користувача та видалення користувача.
# Переконайтеся, що кожен метод відповідає за одну конкретну функцію.
#
# import json
#
#
# class User:
#     def __init__(self, user_id, name, email):
#         self.user_id = user_id
#         self.name = name
#         self.email = email
#
#     def update_user_name(self, new_user):
#         """Updates name data and return update data."""
#         self.name = new_user
#         return self.get_user_info()
#
#     def update_user_email(self, new_email):
#         """Updates email data and return update data."""
#         self.email = new_email
#         return self.get_user_info()
#
#     def get_user_info(self):
#         """Returns information about the user."""
#         return {
#             "user_id": self.user_id,
#             "name": self.name,
#             "email": self.email
#         }
#
#
# class UserStorage:
#     def __init__(self, filename="users.json"):
#         self.filename = filename
#
#     def save_users(self, users):
#         """Save a list of users to a JSON file."""
#         with open(self.filename, "w") as f:
#             json.dump({uid: user.get_user_info() for uid, user in users.items()}, f)
#
#     def load_users(self):
#         """Load a list of users from a JSON file."""
#         try:
#             with open(self.filename, "r") as f:
#                 users_data = json.load(f)
#                 return {
#                     int(uid): User(data["user_id"], data["name"], data["email"])
#                     for uid, data in users_data.items()
#                 }
#         except (FileNotFoundError, json.JSONDecodeError):
#             return {}
#
#
# class UserManager:
#     def __init__(self, storage: UserStorage):
#         self.users = {}
#         self.storage = storage
#
#     def create_user(self, user_id: int, name: str, email: str):
#         """Create a new user"""
#         self.users[user_id] = User(user_id, name, email)
#         self.storage.save_users(self.users)
#         return self.users[user_id]
#
#     def delete_user(self, user_id: int):
#         """Видаляє користувача."""
#         if user_id in self.users:
#             del self.users[user_id]  # Видаляємо користувача
#             self.storage.save_users(self.users)
#             print(f"Користувача з ID {user_id} видалено.")
#         else:
#             print(f"Користувача з ID {user_id} не знайдено.")
#
#     def load_users(self):
#         """Load users from file."""
#         self.users = self.storage.load_users()
#
#
# storage = UserStorage()
# manager = UserManager(storage)
# user = manager.create_user(1, "Oleg", "oleg@example.com")
# print(user.get_user_info())
# user_1 = manager.create_user(2, "Dima", "dima@gmail.com")
# manager.delete_user(1)
#
# print(user_1.get_user_info())
# print("Current list of users:", {uid: user.get_user_info() for uid, user in manager.users.items()})
#
# manager.delete_user(1)

# Завдання 2: Принцип відкритості/закритості (Open/Closed Principle - OCP)
# Створіть інтерфейс "Фігура" (Shape) та два класи, які реалізують цей інтерфейс, наприклад, "Коло" (Circle) та "Прямокутник" (Rectangle).
# Потім додайте новий клас, який розраховує площу будь-якої фігури, не модифікуючи існуючі класи.
# Використовуйте принцип OCP для розширення функціональності.

# Завдання 3: Принцип підстановки Лісков (Liskov Substitution Principle - LSP)
# Створіть ієрархію класів для геометричних фігур, де кожен підклас (наприклад, "Квадрат" і "Круг") може замінити базовий клас "Фігура" без порушення функціональності.
# Переконайтеся, що ці підкласи можуть використовуватися замість базового класу у всіх контекстах без проблем.

# from abc import ABC, abstractmethod
# import math
#
#
# class Shape(ABC):
#     """Abstract class for all shapes"""
#
#     @abstractmethod
#     def calculate_area(self) -> float:
#         """Abstract method for calculating area"""
#         pass
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__()
#         self.__radius = radius
#
#     def calculate_area(self):
#         area = round(math.pi * self.__radius ** 2, 2)
#         return area
#         # return print(f"Area of the circle with radius {self.__radius} is equal to {area:.2f}")
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         super().__init__()
#         self.__width = width
#         self.__height = height
#
#     def calculate_area(self):
#         area = self.__height * self.__width
#         return area
#         # return  print(f"Area of the rectangle with sides {self.__width} and {self.__height} is equal to {area:.2f}")
#
#
# class Triangle(Shape):
#     def __init__(self, base_of_height, height):
#         super().__init__()
#         self.__base_of_height = base_of_height
#         self.__height = height
#
#     def calculate_area(self):
#         area = 0.5 * self.__base_of_height * self.__height
#         return area
#         # print(f"Area of the triangle with the base of the height {self.__base_of_height} and height {self.__height} is equal to {area:.2f}")
#
#
# class AreaShape:
#     @staticmethod
#     def area_shape(shape: Shape):
#         """Class for calculating the area of any shape"""
#         return shape.calculate_area()
#
#
# circle = Circle(5)
# rectangle = Rectangle(3, 5)
# triangle = Triangle(3, 8)
#
# print("Area of circle: ", AreaShape.area_shape(circle))
# print("Area of rectangle: ", AreaShape.area_shape(rectangle))
# print("Area of triangle: ", AreaShape.area_shape(triangle))


# Завдання 4: Принцип інтерфейсу користувача (Interface Segregation Principle - ISP)
# Розробіть інтерфейс "Мережевий принтер" (NetworkPrinter), який включає методи для друку, сканування та копіювання.
# Потім створіть два класи: "Принтер" (Printer) та "Сканер" (Scanner), які реалізують цей інтерфейс та використовують лише ті методи, які їм потрібні.
# Переконайтеся, що жоден з класів не має пустого методу.

from abc import ABC, abstractmethod

class Printable(ABC):
    """Separate interface for printing"""

    @abstractmethod
    def print_document(self, document: str):
        pass


class Scannable(ABC):
    """Separate interface for scanning"""

    @abstractmethod
    def scan_document(self):
        pass


class Copyable(ABC):
    """Separate interface for coping"""

    @abstractmethod
    def copy_document(self):
        pass


class Printer(Printable):
    """Printer class (implements printing only)"""

    def print_document(self, document: str):
        print(f"Printing: {document}")


class Scanner(Scannable):
    """Scanner class (implements scanning only)"""

    def scan_document(self):
        print("Scanning document...")


class MultiFunctionDevice(Printable, Scannable, Copyable):
    """Multifunction device (implements all functions)"""

    def print_document(self, document: str):
        print(f"Printing: {document}")

    def scan_document(self):
        print("Scanning document...")

    def copy_document(self):
        print("Copying document...")


printer = Printer()
printer.print_document("Report.pdf")

scanner = Scanner()
scanner.scan_document()

mfp = MultiFunctionDevice()
mfp.print_document("Contract.pdf")
mfp.scan_document()
mfp.copy_document()

# Завдання 5: Принцип залежностей (Dependency Inversion Principle - DIP)
# Використовуючи принцип DIP, переробіть код залежностей у вашому проекті так, щоб він використовував абстракції та інтерфейси замість конкретних реалізацій.
# Переконайтеся, що класи залежностей не знають про конкретну реалізацію інших класів.

from abc import ABC, abstractmethod

# 🔹 1. Створюємо абстракцію для БД
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

# 🔹 2. Конкретні реалізації бази даних
class MySQLDatabase(Database):
    def connect(self):
        return "Connected to MySQL Database"

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connected to PostgreSQL Database"

# 🔹 3. UserService залежить від інтерфейсу, а не від конкретного класу
class UserService:
    def __init__(self, database: Database):  # Впровадження залежності через конструктор
        self.db = database

    def get_users(self):
        connection = self.db.connect()
        return f"{connection}. Fetching users..."

# 🔹 4. Легко змінювати базу даних
mysql_db = MySQLDatabase()
user_service = UserService(mysql_db)
print(user_service.get_users())  # ✅ "Connected to MySQL Database. Fetching users..."

postgres_db = PostgreSQLDatabase()
user_service = UserService(postgres_db)
print(user_service.get_users())  # ✅ "Connected to PostgreSQL Database. Fetching users..."
