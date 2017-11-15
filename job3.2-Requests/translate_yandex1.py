import requests
import os

#
# def path_dirs():
#     input_folder = 'input_files'
#     output_folder = 'output_files'
#     current_path = os.path.dirname(__file__)
#     path_Source = os.path.join(current_path, input_folder)
#     if os.path.isdir('./' + output_folder):
#         path_Result = os.path.join(current_path, output_folder)
#     else:
#         os.mkdir(output_folder)
#         path_Result = os.path.join(current_path, output_folder)
#     return path_Source, path_Result


def lang_file_in(input_folder, text_file):
    with open(os.path.join(input_folder, text_file), encoding='utf-8') as f:
        text = f.read()
        lang_in = text_file[0:2].lower()
    return text, lang_in


def translate_it(input_folder = input('Введите путь к исходному файлу: '), output_folder = input('Введите путь к конечному файлу: ') , lang_out='ru'):
    #input_folder, output_folder = path_dirs()
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
     &key=<API-ключ>
     &text=<переводимый текст>
     & lang=<направление перевода>
    :return: <str> translated text write into output_folder/file(format name  - LANG_IN-LANG_OUT.txt)
    """

    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    for lang_file in os.listdir(input_folder):
        text, lang_in = lang_file_in(input_folder, lang_file)
        params = {
            'key': key,
            'lang': f'{lang_in}-{lang_out}',
            'text': text
        }
        response = requests.get(url, params=params).json()
        translate_text = ' '.join(response.get('text', []))

        with open(os.path.join(output_folder, f'{lang_file[0:2]}-{lang_out.upper()}.{lang_file[3:]}'), 'w',
                  encoding='utf-8') as fw:
            fw.write(translate_text)


translate_it()
translate_it(lang_out='it')