#from typing import Dict, Any
import os as os

def get_cook_book():
    cook_book = {}
    with open('recipes.txt', 'r', encoding = 'utf-8') as f:
        i = 0
        for line in f:
            if line != '\n':
                line = line.rstrip()
                i += 1
                if i ==1:
                    recipes = []
                    cook_name = line
                elif i == 2:
                    number_ingredients = int(line)
                else:
                    recip = {}
                    l_recip = line.split('|')
                    recip['ingredient_name']= l_recip[0]
                    recip['quantity']= int(l_recip[1])
                    recip['measure']= l_recip[2]
                    recipes.append(recip)
            else:
                i = 0
                cook_book[cook_name] = recipes
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    name_ingredients_and_quantity = {}
    cook_book = get_cook_book()
    for dishe in dishes:
        for cooking in cook_book[dishe]:
            if cooking['ingredient_name'] in name_ingredients_and_quantity:
                ingredients = name_ingredients_and_quantity[cooking['ingredient_name']]
                ingredients['quantity'] += cooking['quantity'] * person_count
                name_ingredients_and_quantity[cooking['ingredient_name']] = ingredients
            else:
                ingredients = {'measure': cooking['measure'], 'quantity': cooking['quantity'] * person_count}
                name_ingredients_and_quantity[cooking['ingredient_name']] = ingredients
    return name_ingredients_and_quantity


dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
print(get_shop_list_by_dishes(dishes, person_count))


def get_sorted_files_tuple(path):
    list_name_files = os.listdir(path)
    files = {}
    sorted_files_list = []
    for i in list_name_files:
        with open(path + i, 'r', encoding = 'utf-8') as f:
            files[i] = len(f.readlines())
    sorted_files = sorted(files.items(),key=lambda item: item[1])
    for t in sorted_files:
        sorted_files_list.append(t[0])
    return tuple(sorted_files_list)


def get_final_structure(path):
    sorted_files_tuple = get_sorted_files_tuple(path)
    final_file = {}
    for i in sorted_files_tuple:
        path_i = path + i #'txt/' + i
        with open(path_i, 'r', encoding = 'utf-8') as f:
            lines = {}
            list_f = f.readlines()
            number_lines = len(list_f)
            lines[number_lines] = list_f
            final_file[i] = lines
    return final_file


def save_final_file(path, final_file):
    final_structure = get_final_structure(path)
    with open(final_file, 'w', encoding = 'utf-8') as f:
        for key, value in final_structure.items():
            f.write(key + '\n')
            for k, v in value.items():
                f.write(str(k) + '\n')
                f.write(''.join(v) + '\n')


save_final_file ('txt/', 'final_file.txt')






