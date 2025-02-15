from abc import ABC, abstractmethod

class DiscountCalculator(ABC):
    def __init__(self, cost: float, discount: float):
        self.cost = cost
        self.discount = discount  # % знижки у вигляді десяткового дробу (наприклад, 0.1 = 10%)

    @abstractmethod
    def get_discounted_product(self) -> float:
        """Обчислює знижку та повертає кінцеву ціну"""
        return self.cost - (self.cost * self.discount)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.get_discounted_product():.2f} грн"


class DiscountCalculatorShirt(DiscountCalculator):
    def __init__(self, cost: float):
        super().__init__(cost, 0.10)  # 10% знижки

    def get_discounted_product(self) -> float:
        return super().get_discounted_product()


class DiscountCalculatorTShirt(DiscountCalculator):
    def __init__(self, cost: float):
        super().__init__(cost, 0.15)  # 15% знижки

    def get_discounted_product(self) -> float:
        return super().get_discounted_product()


class DiscountCalculatorPant(DiscountCalculator):
    def __init__(self, cost: float):
        super().__init__(cost, 0.20)  # 20% знижки

    def get_discounted_product(self) -> float:
        return super().get_discounted_product()


# 🔹 Створення об'єктів
items = [
    DiscountCalculatorShirt(100),
    DiscountCalculatorTShirt(1000),
    DiscountCalculatorPant(500),
]

# 🔹 Вивід результату
for item in items:
    print(item)
