# **Завдання 1: Наслідування**
# Створіть базовий клас `Vehicle` (транспортний засіб), який містить наступні атрибути:
# - `make` (виробник)
# - `model` (модель)
# - `year` (рік виробництва)
# Додайте конструктор класу `Vehicle`, який ініціалізує ці атрибути.
# Створіть підкласи (похідні класи) від `Vehicle` для різних видів транспорту, наприклад, `Car`, `Motorcycle`, `Bicycle`, тощо.
# Кожен підклас повинен мати додаткові атрибути та методи, які є специфічними для цього виду транспорту. Наприклад, для класу `Car` можна додати атрибут `fuel_type` та метод `start_engine()`.
# Створіть об'єкти для кожного з підкласів та виведіть їхні атрибути на екран.

# **Завдання 2: Поліморфізм**
# Створіть метод `display_info()` у базовому класі `Vehicle`, який виводить загальну інформацію про транспортний засіб (наприклад, "Це [виробник] [модель] [рік] року виробництва.").
# В кожному з підкласів перевизначте метод `display_info()` для виведення специфічної інформації про цей вид транспорту.
# Створіть список об'єктів з різних видів транспорту, викличте метод `display_info()` для кожного об'єкта, і спостерігайте за тим, як поліморфізм дозволяє викликати правильну версію методу для кожного об'єкта.

class Vehicle:
    """ Base class for vehicles."""

    def __init__(self, make, model, year=0):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Displays general information about the vehicle."""
        print(f"This is {self.make} {self.model} {self.year} of manufacture.")

    def get_attrs(self):
        print(self.__dict__)


class Car(Vehicle):
    """Class for car"""

    def __init__(self, make, model, year, fuel_type, doors):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type  # Fuel type (gasoline, diesel, electric)
        self.doors = doors  # Number of doors

    def start_engine(self):
        """Starts the car engine."""
        print(f"{self.make} {self.model} (Fuel: {self.fuel_type}) engine started!")

    def display_info(self):
        super().display_info()
        print(f"Fuel: {self.fuel_type}.")


class Motorcycle(Vehicle):
    """Class for motorcycle"""

    def __init__(self, make, model, year, engine_capacity, has_sidecar):
        super().__init__(make, model, year)
        self.engine_capacity = engine_capacity  # Engine capacity
        self.has_sidecar = has_sidecar  # Is there a sidecar?

    def rev_engine(self):
        """ Simulates the sound of a motorcycle engine"""
        print(f"{self.make} {self.model} goes Vroom Vroom!")

    def display_info(self):
        super().display_info()
        print(f"Engine capacity: {self.engine_capacity}.")


class Bicycle(Vehicle):
    """Class for bicycle"""

    def __init__(self, make, model, year, gear_count, bike_type):
        super().__init__(make, model, year)
        self.gear_count = gear_count  # Number of gears
        self.bike_type = bike_type  # Type (mountain, highway, city)

    def ring_bell(self):
        """ Simulates a bicycle bell """
        print(f"{self.make} {self.model} goes Ring Ring!")

    def display_info(self):
        super().display_info()
        print(f"Number of gears: {self.gear_count}.")


# car = Car("BMW", "X5", 2023, "Дизель", 4)
# car.start_engine()
# car.display_info()
#
# moto = Motorcycle("Honda", "CBR600RR", 2022, 599, False)
# moto.rev_engine()
# moto.display_info()
#
# bicycle = Bicycle("Trek", "Marlin 7", 2024, 21, "Mountain")
# bicycle.ring_bell()
# bicycle.display_info()

vehicles = [
    Car("Toyota", "Corolla", 2022, "Бензин", 4),
    Motorcycle("Yamaha", "MT-07", 2023, 689, False),
    Bicycle("Giant", "Defy", 2021, 18, "Шосейний"),
]

for vehicle in vehicles:
    vehicle.display_info()
