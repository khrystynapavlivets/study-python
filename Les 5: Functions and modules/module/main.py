# import my_module
# my_module.hello("Tom")

import calculator


def main():
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        print(f"Перше число: {a}")
        print(f"Друге число: {b}")
        print("Оберіть операцію: +, -, *, /")
        operation = input("Введіть операцію: ")

        # Обробка операції
        if operation == "+":
            print(f"Результат: {calculator.add(a, b)}")
        elif operation == "-":
            print(f"Результат: {calculator.subtract(a, b)}")
        elif operation == "*":
            print(f"Результат: {calculator.multiply(a, b)}")
        elif operation == "/":
            if b != 0:
                print(f"Результат: {calculator.divide(a, b)}")
            else:
                print("Помилка: ділення на нуль!")
        else:
            print("Невідома операція.")
    except ValueError:
        print("Помилка: введено не число!")

main()
