# **Завдання 1: Створення класу і об'єктів**
#
# Створіть клас `Animal`, який представляє тварину. Кожний об'єкт класу `Animal` повинен мати наступні атрибути:
#
# - `name` (ім'я тварини)
# - `species` (вид тварини)
# - `age` (вік тварини)
#
# Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. Напишіть метод `make_sound()`,
# який буде виводити звук, який виділяє тварина.
#
# Створіть два об'єкта класу `Animal` з різними характеристиками та викличте їхні методи `make_sound()`.

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.get_animal()

    def get_animal(self):
        # Виведення інформації про тварин
        print(self.__dict__)

    def make_sound(self):
        match self.species:
            case "Dog":
                print(f"{self.species} says: Woof! Woof!")
            case "Cat":
                print(f"{self.species} says: Meow! Meow!")
            case "Parrot":
                print(f"{self.species} says: Squawk! Squawk!")


# # Створення об'єктів класу Animal
# dog = Animal("Buddy", "Dog", 3)  # Правильне створення об'єкта
# dog.make_sound()  # Виведе "Woof! Woof!"
# cat = Animal("Whiskers", "Cat", 2)
# cat.make_sound()  # Виведе "Meow! Meow!"
# parrot = Animal("Polly", "Parrot", 5)
# parrot.make_sound()


# **Завдання 2: Робота з об'єктами**
# Створіть клас `Rectangle`, який представляє прямокутник. Кожен об'єкт класу `Rectangle` повинен мати наступні атрибути:
# - `width` (ширина прямокутника)
# - `height` (висота прямокутника)
# Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта.
# Напишіть метод `calculate_area()`, який розраховує площу прямокутника (площа = ширина * висота).
# Створіть два об'єкта класу `Rectangle` з різними розмірами та викличте їхні методи `calculate_area()`, виведіть площу прямокутників на екран.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.get_rectangle()

    def get_rectangle(self):
            print(self.__dict__)


    def calculate_area(self):
        print(f"The area of a rectangle with sides {self.length} and {self.width} is {self.length * self.width}")


area_1 = Rectangle( 3, 4 )
area_1.calculate_area()