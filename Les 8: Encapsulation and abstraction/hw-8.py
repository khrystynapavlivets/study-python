# Завдання 1: Інкапсуляція
#
# Створіть клас "Користувач" (User), який має такі приватні поля (інкапсульовані дані):
#
# Ім'я (name)
# Електронна пошта (email)
# Пароль (password)
# Напишіть публічні методи для установки і отримання значень цих полів (геттери і сеттери).
# Потім створіть об'єкт класу "Користувач" і встановіть значення полів, а також виведіть їх на екран.
# import math
# from tkinter.font import names

# class User:
#     def __init__(self, name: str, email: str, password: str):
#         self.__name = name
#         self.__email = email
#         self.__password = password
#
#     def get_name(self):
#         return self.__name
#
#     def get_email(self):
#         return self.__email
#
#     def get_password(self):
#         return self.__password
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_email(self, email):
#         self.__email = email
#
#     def set_password(self, password):
#         self.__password = password
#
#     def __getattr__(self, item):
#         if item == "name":
#             return self.__name
#         elif item == "email":
#             return self.__email
#         elif item == "password":
#             return self.__password
#         else:
#             raise AttributeError(f"Object has no attribute '{item}'")
#
#
# user = User("Іван", "ivan@example.com", "securepassword")
# print(user.get_name())
# print(user.get_email())
# print(user.__getattr__("name"))
# print(user.__dict__)


##################################
##################################


# Завдання 2: Абстракція
#
# Створіть клас "Фігура" (Shape), який буде абстрактним класом.
# У цьому класі визначіть абстрактний метод "обчислити_площу" (calculate_area).
# Створіть підкласи цього класу для різних геометричних фігур, наприклад, "Коло" (Circle), "Прямокутник" (Rectangle) і "Трикутник" (Triangle).
# У кожному з підкласів реалізуйте метод "обчислити_площу" відповідно до формули для обчислення площі кожної фігури.
# Створіть об'єкти кожного з підкласів і використайте метод "обчислити_площу", щоб вивести площу кожної фігури на екран.




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


