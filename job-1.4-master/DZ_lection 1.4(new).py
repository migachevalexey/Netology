Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def input_information():
	n = input('''Нужно ввести букву,которая подразумевает под собой выполнение команды:
p - спросит номер документа и выведет имя человека, которому он принадлежит;
l - выводит список всех документов;
s - спросит номер документа и выведет № полки, на которой он находится;
a - добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
  Введите букву: ''')
    return n

def input_doc_number():
    n = input('Ведите номер документа: ')
    return n

def input_document():
    n = input_doc_number()
    type_doc = input('Тип документа: ')
    fio_name = input('Введите имя: ')
    shelf_number = input('Номер полки: ')
    return n, type_doc, fio_name, shelf_number

def command_people (documents):
    n = input_doc_number()
    for i in documents:
        for values in i.values():
            if values == n:
                print(i["name"])

def command_list (documents): 
    print('Cписок всех документов')
    for i in documents:
        print(*i.values())

def command_shelf (directories):
    n = input_doc_number()
    for key, items in directories.items():
        for i in items:
            if i == n:
                print('Документ лежит на полке c № {}!'.format(key))

def add_shelf(directories): 
    shelf_number_new = input('Ведите номер новой полки: ')
    directories[shelf_number_new] = []				

def command_add(documents,directories):
    n, type_doc, fio_name, shelf_number = input_document()
    documents.append({"type": type_doc, "number": n, "name": fio_name})
    if shelf_number not in directories:
        print('Такой полки нет,создадим')
        add_shelf(directories)
        directories[shelf_number].append(n)
    else:
        directories[shelf_number].append(n)
    print(documents, '\n', directories)

def choice_leter(n):
    if n == 'p':
        command_people(documents)
    elif n == 'l':
        command_list(documents)
    elif n == 's':
        command_shelf(directories)
    elif n == 'a':
        command_add(documents, directories)

def main():
    n = input_information()
    if n not in 'plsad':
        print('Ошибка!Нет такой команды!!!')
    else:
        choice_leter(n)
main()
