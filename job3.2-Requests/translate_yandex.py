import requests
import os


def translate_file(file, lang_in, lang_out='ru'):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    with open(file, encoding='utf-8') as f:
        text = f.read()

    params = {
        'key': key,
        'lang': f'{lang_in}-{lang_out}',
        'text': text
    }
    response = requests.get(url, params=params).json()
    translate_text = ' '.join(response.get('text', []))
    return translate_text


def translate_it(input_folder=input('Введите путь к исходному файлу: '),
                 output_folder=input('Введите путь к конечному файлу: ')):
    if len(os.listdir(input_folder)) > 0:
        print('В папке несколько файлов. Вы хотите перевести все или конкретный файл? Вот эти файлы - ',
              *os.listdir(input_folder))
        n = input('Перевести все - введите all. Отдельный файл - введите его имя(с расширением): ')
    if n == 'all':
        for lang_file in os.listdir(input_folder):
            print(lang_file)
            lang_in = input('Введите язык оригинала: ')
            translate_text = translate_file(os.path.join(input_folder, lang_file), lang_in)
            with open(os.path.join(output_folder, f'{lang_in.upper()}-RU.txt'), 'w',
                      encoding='utf-8') as fw:
                fw.write(translate_text)

    else:
        lang_in = input('Введите язык оригинала: ')
        translate_text = translate_file(os.path.join(input_folder, n), lang_in)
        with open(os.path.join(output_folder, f'{lang_in.upper()}-RU.txt'), 'w',
                  encoding='utf-8') as fw:
            fw.write(translate_text)


translate_it()

