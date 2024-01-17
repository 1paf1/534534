# set
# users1 = {"Tom", "John", "Smith"}
# users2 = {"John", "Petya", "Kolya"}
# union() - обєднує наприклад users1 and usesr2
#
# discard() - видаляє значення якщо його немає то його немає
#
# remove() - видаляє значення якщо його немає то генерує виняток
#
# intersection() - перетин множин(що є у першої і у другої множин)

#intersection_update() - те саме, тільки зміни будуть записані в user1

# difference() - що є в першій і нема в другій множині, можна записати як user1 - user2

#symetric_difference() - що є унікального в першій і другій множині, можна записати як user1 ^ user2
# users3 = users1.union(users2)
# print(users3)
# users3 = users1.intersection(users2) # аналог print(users1 & users2)
# print(users3)
#
#
# users = {"Tom", "John", "Smith"}
# superusers = {"Tom", "John", "Smith", "Kolya", "Ebolya"}
# print(users.issubset(superusers)) # перевіряє чи юзерс є підмножиною суперюзерс: виводить тру
# print(superusers.issubset(users)) # перевіряє чи суперстарс є підмножиною юзерс: виводить фолс
# print(superusers.issuperset(users)) # перевіряє чи суперюзерс є надмножиною юзерс: виводить тру
# print(users.issuperset(superusers)) # перевіряє чи юзерс є надмножиною суперюзерс: виводить фолс


# 1. Створити список чисел. Заберіть дублікати значень. Вивести унікальні значення.

# numbers = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 9, 1, 10]
# unique_number = set(numbers)
# print(unique_number)

# # 2. Дано два списки чисел.
# #
# # Порахуйте, скільки унiкальних чисел міститься як у першому списку, і у другому.
#
# import random
#
# list1 = [random.randint(-10, 10) for _ in range(10)]
# print("First list:", list1)
#
# list2 = [random.randint(-10, 10) for _ in range(10)]
# print("Second list:", list2)
#
# list1_set = set(list1)
# list2_set = set(list2)
# list3 = list1_set.difference(list2_set)
# print("Difference list:", list3)
# print(f"Count of unique elements in : {len(list3)}")


# 3. Даний текст: у першому рядку записано число рядків, далі йдуть самі рядки.
#
# Визначте, скільки унiкальних слів міститься у цьому тексті.
#
# Словом вважається послідовність непробільних символів, що йдуть поспіль, слова розділені одним або більшим числом пробілів або символами кінця рядка.

# num_lines = int(input("Введіть кількість рядків: "))
# unique_words = set()
#
# for _ in range(num_lines):
#     line = input("Введіть рядок тексту: ")
#
#     words = line.split()
#
#     unique_words.update(words)
# print(unique_words)
# print("Кількість унікальних слів у тексті:", len(unique_words))


# 1. Наведено список країн і міст кожної країни. Для кожного міста вкажіть, в якій країні воно знаходиться.
# countries_and_cities = {
#     'Ukraine': ['Kyiv', 'Lviv', 'Dnipro'],
#     'USA': ['Los Angeles', 'Las Vegas'],
#     'Germany': ['Berlin', 'Munich', 'Hamburg']
# }
# result = {country: cities for country, cities in countries_and_cities.items()}
# print(result)
#

# last task

#v1
# keys = [1, 2, 3, 4, "key"]
# values = ["hello","world","data", True, 2]
#
# my_dict = {}
#
# for i in range(len(keys)):
#     my_dict[keys[i]] = values[i]
# print(my_dict)

#v2
# keys = [1, 2, 3, 4, "key"]
# values = ["hello","world","data", True, 2]
# my_dict = dict(zip(keys, values))
#
# print(my_dict)