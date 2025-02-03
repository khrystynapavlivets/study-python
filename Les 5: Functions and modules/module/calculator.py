def add(a, b):
    """Додає два числа."""
    return a + b


def subtract(a, b):
    """Віднімає друге число від першого."""
    return a - b


def multiply(a, b):
    """Множить два числа."""
    return a * b


def divide(a, b):
    """Ділить перше число на друге, перевіряючи ділення на нуль."""
    if b == 0:
        return "Помилка: Ділення на нуль неможливе!"
    return a / b


def hello(name):
    print(f"Hello {name}")
