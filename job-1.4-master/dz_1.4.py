Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять ни один документ. Каталог документов хранится в следующем виде:

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        
      ]
# Перечень полок, на которых находятся документы хранится в следующем виде:
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }
      
def main_list():
  print ("Введите команду l")
  command_input=input()
  if command_input=="l":
    print(documents[0]["type"],documents[0]["number"],documents[0]["name"])
    print(documents[1]["type"],documents[1]["number"],documents[1]["name"])
    print(documents[2]["type"],documents[2]["number"],documents[2]["name"])
  else:
    exit()
  
main_list()

def main_add():
  print ("Введите команду a")
  command_input=input()
  if command_input=="a":
    print ("Введите type:")
    type_input = input()
    print ("Введите number:")
    number_input = str(input())
    print ("Введите name:")
    name_input = input()
    print ("Укажите номер полки,на которой будет храниться новый документ:")
    number_stelage_input = input()
    c={"type":type_input,"number":number_input,"name":name_input}
    documents.append(c)
    print(documents[3])
    directories['1'].append(number_input)
    print(directories['1'])
  else:
    exit()
main_add()  
 
def main_shelf():
  print ("Введите команду s")
  command_input=input()
  if command_input=="s":
    print('введите номер документа')
    input_number_document=str(input())
    def get_key(directories,input_number_document):
      for k, v in directories.items():
        if v==input_number_document:
          return k
    print(get_key(directories,[input_number_document]))
main_shelf()
        








