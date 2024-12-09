# my_string = 'Це рядок'
# print(my_string)
# my_integer = 42
# print(my_integer)
# my_float = 3.14
# print(my_float)
# my_boolean=True
# print(my_boolean)
# my_list=[1,5,8,6]
# print(my_list)
# my_dict={"ім'я": "Іван", "вік": 25}
# print(my_dict)
# my_tuple = (1, 2, 3)
# print(my_tuple)
# my_sets = {1, 2, 9, 3}
# print(my_sets)
# my_tuple = (1, 2, 3, 2)
# print(my_tuple)
# my_none = None
# print(my_none)

# a = 11
# b = 20
#
# print(a > b)
# print(a < b)
# print(a == b)
# print(a != b)
# print(a >= 10)
# print(b <= 30)


# a = "apple"
# b = "banana"
# c = "apple"

# print(a > b)
# print(a <= b)
# print(a == b)
# print(a != b)
# print(a != b)
# print(a == c)
#
# bool1 = True
# bool2= False
#
# print(bool1 > bool2)  # True (1 > 0)
# print(bool1 == bool2)  # False
# print(bool1 != bool2)  # True
#
# num_str = 125
# print(str(125))

# message = 'Hi, my name is Python!'
# message_1 = message.replace('y','o')
# print(message_1)
# message_2 = message.replace('i','1')
# print(message_2)


# test = 'This is a split test'
# split_test = test.split()
# print(split_test)
# string_join = ''.join(split_test)
# print(string_join)
# string_len = len(string_join)
# print(string_len)


# Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4, а потім 5

# list_append= [1, 2, 3]
# list_append.extend([4])
# list_append.extend([5])
# print(list_append)


# Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком[7, 8, 9] за допомогою функції extend()
# list_extend = [4, 5, 6]
# list_extend.extend([7, 8, 9])
# print(list_extend)


# Визначити індекс елемента 6 у списку list_extend за допомогою функції index()
#
# list_index = list_extend.index(6)
# print(list_index)


# Визначити довжину списку list_append за допомогою функції len()

# list_append_len = len(list_append)
# print(list_append_len)


# Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} та вивести на екран дані, які знаходяться в ключах car та where



# Метод keys() повертає лише список ключів словника, але для доступу до значень краще використовувати синтаксис dict_test['ключ']

# dict_test_keys = dict_test.keys()
# print(dict_test_keys)

# Метод values() повертає лише список значень, але для доступу до значень краще використовувати синтаксис dict_test['значення']

# dict_test_values = dict_test.values()
# print(dict_test_values)

# потрібно вивести всі значення зі словника dict_test через рядок, можна використати метод values() разом із функцією join().

# values_as_string = ", ".join(map(str, dict_test_values))
# print(values_as_string)

# За допомогою функції items() вивести на екран пари ключ - значення

# dict_test_items = dict_test.items()
# print(dict_test_items)
