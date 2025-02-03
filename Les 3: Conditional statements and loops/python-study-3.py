# -------------ДЗ--------------
# **Перевірка паролю:**
# Завдання: Напишіть програму, яка встановлює початковий пароль і перевіряє, чи введений користувачем пароль співпадає з ним.
# Якщо пароль дорівнює "password123", виведіть повідомлення "Ви увійшли в систему". В іншому випадку виведіть повідомлення "Неправильний пароль".

# password = "password123"
# user_input = input("Введіть пароль: ")
# if user_input == password:
#     print("Ви увійшли в систему")
# else:
#     print("Неправильний пароль")

# **Визначення днів тижня:**
# Завдання: Створіть програму, яка встановлює номер дня тижня і виводить назву відповідного дня тижня.
# Якщо номер дня недійсний (менше 1 або більше 7), виведіть повідомлення про помилку.

# weekdays = {
#     1: "Monday",
#     2: "Tuesday",
#     3: "Wednesday",
#     4: "Thursday",
#     5: "Friday",
#     6: "Saturday",
#     7: "Sunday"
# }
#
# try:
#
#     day_number = 4
#
#     if 1 <= day_number <= 7:
#         print(f"День тижня: {weekdays[day_number]}")
#     else:
#         print("Помилка: Номер дня має бути в діапазоні від 1 до 7.")
# except ValueError:
#     print("Помилка: Будь ласка, введіть ціле число.")

# ### Цикли:
#
# 1. **Таблиця множення:**
#    Завдання: Виведіть таблицю множення для заданого числа від 1 до 10.
# number = 6
#
# for i in range(1, 11):
#     result = number * i
#     print(f"{number} x {i} = {result}")
#


# 2. **Сума чисел:**
#    Завдання: Визначте список чисел і обчисліть їх суму.

# numbers = [3, 7, 12, 19, 25]
# total_sum = 0
# for number in numbers:
#     total_sum += number
#
#
# print(f"Список чисел: {numbers}")
# print(f"Сума чисел: {total_sum}")



# 3. **Факторіал числа:**
#    Завдання: Обчисліть факторіал заданого числа.

# number = 7
# factorial = 1 # початкове значення
# steps = []
#
# for i in range(1, number + 1):
#     factorial *= i
#     steps.append(str(i))
#     steps_str = " * ".join(steps)
# print(f"Факторіал числа {number}!= {steps_str}= {factorial}")




# 4. **Парні числа:**
#    Завдання: Виведіть всі парні числа від 1 до 50.

# for i in range(1, 51):
#     if i % 2 == 0:
#      print(i)




# for number in range(2, 51, 2):  # починаємо з 2, додаємо 2 на кожному кроці
#     print(number)



# 5. **Пошук простих чисел:**
#    Завдання: Знайдіть всі прості числа в заданому діапазоні.
#
# Створіть власні змінні або встановіть початкові значення, щоб виконати ці завдання без використання `input`.

# a = 2
# b = 50
#
# # Цикл для перебору чисел у діапазоні
# for number in range(a, b + 1):
#     is_prime = True  # Вважаємо, що число є простим
#     for i in range(2, int(number ** 0.5) + 1):  # Перевіряємо дільники до √number
#         if number % i == 0:  # Якщо знайдено дільник
#             is_prime = False  # Число не є простим
#             break  # Припиняємо перевірку
#     if is_prime and number > 1:  # Виводимо тільки прості числа
#         print(number)



# -------------Запис заняття--------------
# string = "Hello world!"
# if "Hello" not in string:
#     print("Hello in string")
# elif "world" in string:
#     print("World in string")
# else:
#     print("Word not in string")
#
#
# a = 10
# b = 20
#
# if a == 11 and b == 20 or b <30:
#     print(a + b)
# else:
#     print("Wrong condition")
#
# test_list = ["hello", "test", 1, 2, 3]
#
# if "hello" in test_list and 1 in test_list:
#     print("Hello 1")
# elif "test" in test_list and 4 not in test_list:
#     print("Test not 4")
# else:
#     print("Your conditions were wrong")
#
#
# a = 10
# b = 20
# c = "chat is active"
# d = "count of users"
# print(len(c), len(d), "--------<")
#
# if len(c) >= b:
#     print(c)
# elif len(d) <= a:
#     print(d)
# else:
#     print("Wrong conditions")
#
#
# user_1 = {
#     "name": "Tom",
#     "age": 21,
#     "balance": 20000,
#     "currency": "USD",
#     "status": True
# }
#
# user_2 = {
#     "name": "John",
#     "age": 17,
#     "balance": 5000,
#     "currency": "EUR",
#     "status": False
# }
#
# user_3 = {
#     "name": "Karine",
#     "age": 30,
#     "balance": 100000,
#     "currency": "UAH",
#     "status": True
# }
#
# list_of_currency = ["USD", "GBR", "UAH", "EUR"]
#
# if user_1.get("name", None) and user_1["age"] >= 18 and user_1["status"]:
#     if user_1["balance"] >= 10000 and user_1["currency"] in list_of_currency:
#         print(f"Hello! You can create your binance account, welcome {user_1['name']}")
#     elif user_1["balance"] >= 1000 and user_1["currency"] in list_of_currency:
#         print("You need more money!")
#     else:
#         print ("Money critical not enough")
# elif not user_1.get("name", None):
#     print("Please. unite voun name in voun account desenintion")
# elif user_1["age"] < 18:
#     print("For registry binance account you have to be 18 year old")
# else:
#     print("Something went wrong")
