import os
import re


def find_folder_migrations():
    if 'Migrations' in os.listdir('.'):
        path_migration = os.path.join(os.getcwd(), 'Migrations')
    else:
        for root, dirs, files in os.walk(r'C:\Users\934\PycharmProjects'):
            for _dir in dirs:
                if _dir == 'Migrations':
                    path_migration = os.path.join(root, _dir)
    sql_file = [i for i in os.listdir(path_migration) if re.match('.*\.sql$', i)]
    return path_migration, sql_file


def find_word(word, arr, path_migration):
    d = []
    word = word.lower()
    for file in arr:
        with open(os.path.join(path_migration, file)) as f: # ВОПРОС! Как правильно - через цикл считывать построчно или все сразу?
            for line in f:                                  # так - data = f.read() if word in data.lower() ...
                if word in line.lower():
                    d.append(file)
                    break
    return d, word


def main():
    path_migration, arr = find_folder_migrations()
    while True:
        word_input = input('Введите слово (для выхода - q): ')
        s, word = find_word(word_input, arr, path_migration)
        if not s:
            print('Данное слово в файлах не встречается')
            exit()
        elif word_input != 'q':
            print('Общее колво файлов содержащих слово - {2}: {0}. \nВот этот список: {1}'
                  .format(len(s), s, word.upper()))
        else:
            exit()
        arr = s

main()
