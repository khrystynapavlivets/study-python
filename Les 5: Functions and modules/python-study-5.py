# def say_hello():
#     print("Hello world")
# 
# 
# def say_hello_user(username, age):
#     print(f"Hello {username}, welcome to the club, buddy!")
#     print(f"Your age is {age}, you are so beautiful!")
#     print("-----------------------------------------")
# 
# 
# def print_numbers():
#     for num in range(1, 11):
#         print(f"Current number is: {num}")
# 
#     print("------------------------------")
# def print_numbers_with_params(start, stop):
#     for num in range(start, stop):
#         print(f"Current number is: {num}")
# 
# print("------------------------------")
# 
# 
# say_hello()
# print_numbers()
# print_numbers_with_params(2,4)
# print("<<<------->>>")
# 
# user_data = {"Dima": 25, "Sarah": 34, "Tom": 11}
# list_of_ranges = [(1, 10), (2, 9), (0, 100)]
# 
# 
# 
# 
# for name, age in user_data.items():
#     say_hello_user(name, age)
# 
# print("<<<------->>>")
# for start_pos, stop_pos in list_of_ranges:
#     print_numbers_with_params(start_pos, stop_pos)
# 

# def check_connection(username, count_tries, priority):
#     if priority >= 10:
#         finish = 5
#         for attemt in range(1, count_tries + 1):
#             if attemt == finish:
#                 print("Connect was successfully")
#                 break
#             print(f"Attemp: {attemt} to connect to {username}")
#
#     elif priority >= 5 and priority < 10:
#         finish = 3
#         for attemt in range(1, 6):
#             if attemt == finish:
#                 print("Connect was successfully")
#             print(f"Attemp: {attemt} to connect to username")
#
#     else:
#         print("Your username has so how priority")


# check_connection(count_tries=10, username="Oleg", priority=100)


# import turtle
#
# def draw_square(size,color):
#     turtle.speed(1)
#     turtle.color(color)
#     turtle.begin_fill()
#     def move(length):
#         turtle.forward(length)
#         turtle.left(90)
#
#     for _ in range(4):
#       move(size)
#
#     turtle.end_fill()
#
# draw_square(100, 'red')
# turtle.goto(100,200)
# draw_square(200,'blue')



######### HW #######

# **Завдання 1: Робота з функціями**

# Створіть Python-файл з ім'ям `calculator.py`. У цьому файлі створіть наступні функції:
# Пам'ятайте про можливість ділення на нуль і додайте перевірку цього варіанту.
# Після створення цих функцій, напишіть програму, яка імпортує модуль `calculator.py` і використовує його функції для виконання обчислень.
# Попросіть користувача ввести два числа і операцію (додавання, віднімання, множення або ділення), і виведіть результат обчислення.

