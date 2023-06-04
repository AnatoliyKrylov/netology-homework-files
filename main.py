# Задача 1
with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for dish_name in file:
        ingredients_count = int(file.readline())
        ingredients_list = []
        for i in range(ingredients_count):
            ingredient_name, quantity, measure = (file.readline()
                                                  .strip().split(' | '))
            ingredients_list.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish_name.strip()] = ingredients_list


# Задача 2
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book.get(dish):
            if ingredient['ingredient_name'] not in shop_list.keys():
                shop_list[ingredient['ingredient_name']] = (
                    {'measure': ingredient['measure'],
                     'quantity': int(ingredient['quantity']) * person_count})
            else:
                shop_list[ingredient['ingredient_name']] = (
                    {'measure': ingredient['measure'],
                     'quantity':
                         shop_list[ingredient['ingredient_name']]['quantity']
                         + int(quantity) * person_count})
    return shop_list


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)

# Задача 3
with (open('1.txt', 'r', encoding='utf-8') as input_file1,
      open('2.txt', 'r', encoding='utf-8') as input_file2,
      open('3.txt', 'r', encoding='utf-8') as input_file3,
      open('res.txt', 'w', encoding='utf-8') as output_file):
    file_text1 = input_file1.readlines()
    file_text2 = input_file2.readlines()
    file_text3 = input_file3.readlines()
    file_res1 = [f'{input_file1.name}\n', f'{len(file_text1)}\n']
    file_res1.extend(file_text1)
    file_res2 = [f'{input_file2.name}\n', f'{len(file_text2)}\n']
    file_res2.extend(file_text2)
    file_res3 = [f'{input_file3.name}\n', f'{len(file_text3)}\n']
    file_res3.extend(file_text3)
    file_res = [file_res1, file_res2, file_res3]
    file_res.sort(key=len)
    for el1 in file_res:
        for el2 in el1:
            output_file.write(el2)
