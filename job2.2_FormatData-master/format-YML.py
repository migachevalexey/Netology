import yaml
import pprint


def cook_book_input():
    with open("recipe.yml") as fin:
        cook_book = yaml.load(fin)
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = cook_book_input()
    for dish in dishes:
        for new_shop_list_item in cook_book[dish]:
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += \
                new_shop_list_item['quantity']
    return list(shop_list.values())


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): '). \
        split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    pprint.pprint(shop_list)
    with open('recipe_final.yml', 'w') as f:
        yaml.dump(shop_list, f, allow_unicode=True)
    print('---------------')
    print('Так же данные были переданы в файл - recipe_final.yml')

create_shop_list()
