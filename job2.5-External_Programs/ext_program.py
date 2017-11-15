import os
import subprocess


def path_dirs():
    output_folder = 'result'
    input_folder = 'source'
    current_path = os.path.dirname(__file__)
    path_Source = os.path.join(current_path, input_folder)
    if os.path.isdir('./'+output_folder):
        path_Result = os.path.join(current_path, output_folder)
    else:
        os.mkdir(output_folder)
        path_Result = os.path.join(current_path, output_folder)
    return path_Source, path_Result

def main():
    counter = 0
    Source, Result = path_dirs()
    for image_file in os.listdir(Source):
        process = subprocess.run('convert.exe {0}\{1} -resize 200 {2}\{3}'.format(Source, image_file, Result, image_file))
        if process.returncode == 0:
            counter += 1
    print('Конвертирование выполнено успешно. Сконвертировано {} файлов из {}'.format(counter, len(os.listdir(Source))))

main()