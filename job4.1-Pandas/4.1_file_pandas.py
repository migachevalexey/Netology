import zipfile
import requests
import os
import pandas as pd


# r=requests.get('https://www.ssa.gov/oact/babynames/names.zip') # скачивал что то очень долго - 2мин
# with open('names.zip', 'wb') as f:
#     f.write(r.content)
# z = zipfile.ZipFile('names.zip', 'r')
# z.extractall('./names')
# os.remove('./names/NationalReadMe.pdf')
DATA_PATH = './names/'
cols = ['Name','Gender','Count']


def top3(*args):
    name_all = pd.DataFrame({})
    for i in args:
        r=pd.read_csv(DATA_PATH + f'yob{i}.txt', names=cols)
        name_all = pd.concat([r,name_all])
    df = name_all.groupby('Name').sum().sort_values(by=['Count'], ascending=False).head(3)
    del df.index.name # удаляем названия индексов
    print('3 cамых популярных имени за {} годы - {}'.format(args, ', '.join(df.index.tolist())) if len(args)>1
          else '3 Самых популярных имени за {} год - {}'.format(*args, ', '.join(df.index.tolist())))
    print(df)

top3(1900)
print('---------')
top3(1900, 1950, 2000)
# top3(*os.listdir(DATA_PATH)) - сразу все файлы в указаной директории. Нужно изменить yob{i}.txt -> i


def count_dynamics(*args):
    name_all = pd.DataFrame({})
    for i in args:
        r = pd.read_csv(DATA_PATH + f'yob{i}.txt', names=cols)
        r.insert(0, 'Year', i)  # r['Year']=i
        name_all = pd.concat([r, name_all])
    df = name_all.groupby(['Year', 'Gender']).sum()
    z = df.to_dict(orient='dict')
    a = {'F': [], 'M': []}  # В этой части покритикуйте. Чувствую, что можно намного короче
    for k, i in z['Count'].items():
        if k[1] == 'F': a['F'].append(i)
        else: a['M'].append(i)

    print(a)
    print(df)

print('-------------------\nЗадача 2')
count_dynamics(1900, 1950, 2000)