import os
from pprint import pprint

# Задача №1. Создание словаря блюд
path = os.path.join(os.getcwd(), 'recipes.txt')
with open(path, 'r', encoding='utf-8-sig') as recipes:
    cook_book = {}
    for string in recipes:
        dish = string.strip()
        ingredients_kol = int(recipes.readline().strip())
        lst_book = []
        for item in range(ingredients_kol):
            ingredient_name, quantity, measure = recipes.readline().strip().split('|')
            lst_book.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish] = lst_book
        recipes.readline() # Прописываем для чтения пустой строки, иначе у нас итерация будет
        # останавливаться и не считывать все позиции
print("Задача №1")
pprint(cook_book, sort_dicts=False, width=100)
print()

# Задача №2. Создание функции получения словаря ингредиентов
"""Создаём функцию для получения информации о покупках исходя из заказов и кол-ва покупателей"""

def get_shop_list_by_dishes(dishes, number_of_buyers):
    shopping_dict = {}
    for dish_ in dishes:
        for ingredient in cook_book[dish_]:
            ingredient_list = dict([(ingredient['ingredient_name'],
                                 {'quantity': int(ingredient['quantity']) * number_of_buyers,
                                  'measure': ingredient['measure']})])
            # Производим проверку если блюдо заказано повторно, то увеличиваем список
            # Иначе если блюдо ещё не заказывали добавляем ингредиенты в список покупок
            if shopping_dict.get(ingredient['ingredient_name']):
                merger = (int(shopping_dict[ingredient['ingredient_name']]['quantity']) +
                          int(ingredient_list[ingredient['ingredient_name']]['quantity']))
                shopping_dict[ingredient['ingredient_name']]['quantity'] = merger
            else:
                shopping_dict.update(ingredient_list)
    return shopping_dict
print("Задача №2")
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2), sort_dicts=False, width=100)
print()


# Задача №3. Создание и запись файла
"""Создаём функцию, которая будет заносить 3 файла в 1 при этом будет принимать на вход папку"""


def create_file(folder):
    file_lst = os.listdir(folder)  # считываем название файлов в папке
    merged_file_lst = []  # создаём список для добавления в неге содержимое файлов
    for file in file_lst:  # проходимся по списку содержимых файлов
        with open(folder + '/' + file, encoding='utf-8-sig') as file_in_temp:  # считываем файлы поочерёдно
            # Ниже добавляем в список 1) Название файла.file 2) Кол-во строк.(0) 3) Содержимое.[]
            merged_file_lst.append([file, 0, []])
            for lines in file_in_temp:  # построчно проходимся по файлам
                merged_file_lst[-1][2].append(lines.strip())  # добавляем построчно информацию
                merged_file_lst[-1][1] += 1  # с прохождением по каждой строке увеличиваем их кол-во для подсчёта
    return sorted(merged_file_lst, key=lambda x: x[1], reverse=False)  # возвращаем полученный файл,
    # при этом, используем ключ и лямбда функцию для сортировки


"""Создаём функцию, которая будет записывать итоговый файл, при этом она принимает на вход папку и имя файла"""


def create_merge_file(folder, result):
    with open(result + '.txt', 'w+', encoding='utf-8-sig') as merged_file:  # создаём результирующий файл с именем the_final_file
        merged_file.write(f'Даны файлы:\n')  # Добавляем строку в файл
        for write_3_files in create_file(
                folder):  # используя первую функцию мы занесём все значения в результирующий файл
            merged_file.write(f'Название файла: {write_3_files[0]}\n')  # Записываем название файла
            merged_file.write(f'Количество строк: {write_3_files[1]}\n')  # Записываем количество строк в type int
            for str_ in write_3_files[2]:  # Проходимся по файлу и по 2 индексу заносим информацию
                merged_file.write(str_ + '\n')  # Записываем эту информацию в файл
            merged_file.write('\n')  # Каждый раз делаем перенос строки, чтобы информация не было однострочной
    return print('Файл успешно создан')  # Возвращаем положительный результат файл успешно создан


create_merge_file('files', 'result')