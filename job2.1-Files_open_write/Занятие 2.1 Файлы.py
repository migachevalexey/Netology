def cook_book_input():
    cook_book = {}
    cook_book_constituent = ['ingridient_name', 'quantity', 'measure']
    with open('recipe.txt') as f:
        for line in f:
            dish_name = line.upper().strip() # ВОПРОС - Как правильно?: правильнее через переменную
            cook_book[dish_name] = []
            for s in range(int(f.readline().strip())):
                d = f.readline().strip().split(' | ')
                d[1] = int(d[1])
                cook_book[dish_name].append(dict(zip(cook_book_constituent, d)))
                # cook_book[dish_name][s]['quantity'] = int(cook_book[dish_name][s]['quantity'])
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = cook_book_input()
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=\
                new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
     for shop_list_item in shop_list.values():
         print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                 shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): '). \
        upper().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)
    with open('recipe_final.txt' , 'w', encoding='cp1251') as f:
        f.write('Для приготовления выбранных блюд, а именно ({}) на {} человек'.format(', '.join(dishes), person_count)
                +'\n'+'Нам потребуются следующие ингридиенты:\n')
        for i, shop_list_item in enumerate(shop_list.values(), start=1):
            f.write('{}.{} - {} {}\n'.format(i, shop_list_item['ingridient_name'].capitalize(), shop_list_item['quantity'],
                            shop_list_item['measure']))

create_shop_list()
