documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
	    {"type": "pass", "number": "33333", "name": "Иван Васин"}
      ]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': [],
    '4': ['333']
}

def input_leter():
    n = input('''Нужно ввести букву
     p - спросит № документа и выведет имя человека, которому он принадлежит;
     l - вывод списком всех документов;
     s - спросит номер документа и выведет № полки, на которой он находится;
     a - добавит новый документ в каталог и в перечень полок, спросив его №, тип, имя владельца и № полки, на котором он будет храниться.
     d - команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
  Итак начнем: ''')
    return n


def input_doc_number():
    n = input('Ведите номер документа: ')
    return n


def input_document():
    n = input_doc_number()
    type_doc = input('Тип документа: ')
    man_name = input('Введите имя: ')
    shelf_number = input('Номер полки: ')
    return n, type_doc, man_name, shelf_number


def people (documents):  # ВОТ ТУТ ВОПРОС. Как быстрее и правильнее - через 2-ой цикл или через in ??
    n = input_doc_number()
    for i in documents:
        if n in i.values():
        #for values in i.values():
         #   if values == n:
            print(i["name"])


def list (documents): # тут вроде покороче получилось
    print('Cписок всех документов')
    for i in documents:
        print(*i.values())


def shelf (directories):
    n = input_doc_number()
    for key, items in directories.items():
        if n in items:
            print('Документ лежит на полке c № {}!'.format(key))

				
# Не обязательная задача
def delete(documents,directories):
    n = input_doc_number()
    for key, items in directories.items():
            if n in items:
                items.remove(n)
                shelf_number = key
    for i in documents:
        if n in i.values():
            i['number'] = ''
            men_name = i['name']
    print('Документ № {} был удален с полки {} и у человека по имени - {}!'.format(n, shelf_number, men_name), '\n')
    print(documents, '\n', directories)

	
# добавление новой полки. Используется в функции add() !!
def add_shelf(directories): 
    shelf_number_new = input('Ведите № новой полки: ')
    directories[shelf_number_new] = []				


def add(documents,directories):
    n, type_doc, man_name, shelf_number = input_document()
    documents.append({"type": type_doc, "number": n, "name": man_name})
    if shelf_number not in directories: # Если полки нет, добавляем ее в словарь
        print('Такой полки в базе нет! Создаем!') # тут по хорошему надо сделать запрос к пользователю - "Создавать или нет?", но я не стал делать
        add_shelf(directories)
        directories[shelf_number].append(n)
    else:
        directories[shelf_number].append(n)
    print(documents, '\n', directories)


def choice_leter(n): # пришлось сделать эту функцию, т.к. в main() предусмотрена ошибка ввода буквы и защита от Тролей!
    if n == 'p':
        people(documents)
    elif n == 'l':
        list(documents)
    elif n == 's':
        shelf(directories)
    elif n == 'a':
        add(documents, directories)
    elif n == 'd':
        delete(documents, directories)


def main():
    n = input_leter()
    if n not in 'plsad':
        print('Вы ошиблись! Попробуйте еще раз и будьте внимательны!!!')
        n = input_leter()
        if n not in 'plsad':
            print('Иди учиcь читать!!')
            exit()
        else:
            choice_leter(n)
    else:
        choice_leter(n)

main()
