import chardet
import json


def input_file_name():
    file_name = input('Введите только имя файла(расширение не надо): ')
    return file_name


def encoding_file():
    file_name = input_file_name()
    with open(file_name + '.json', 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
    return file_name, result['encoding']


def list_dict():
    file_name, cod_name = encoding_file()
    with open(file_name + '.json', encoding=cod_name) as fin:
        data = json.load(fin)
    return data['rss']['channel']['items']  # Как правильно - обозначить переменную и ее в return или можно сразу ?


def generate_list():
    d_full = []
    for i in list_dict():  # !!ВОПРОС!! Я сразу поставил функцию в цикл, так делают?
        d_full += (i['description'] + ' ' + i['title']).split()
    d_small = [i for i in d_full if len(
        i) > 6]  # ВОПРОС!! С точки зрения памяти может лучше d_full = [i for i in d_full if len(i) > 6] ???
    return d_small


def main():
    a = {}
    for i in generate_list():
        a[i] = a.get(i, 0) + 1
    print('{},{},{},{},{},{},{},{},{},{}'.format(*sorted(a.items(), key=lambda x: x[1],
                                                         reverse=True)))


main()
