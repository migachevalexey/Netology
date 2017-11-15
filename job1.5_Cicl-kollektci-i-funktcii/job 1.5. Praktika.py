# Для меня очень ВАЖЕН ВОПРОС!! В этом ДЗ я старался минимизировать код по кол-ву строк, поэтому отдельные строки весьма длинные
# Так вот вопрос: как правильно - читабельный и понятный, но более длинный код или покороче, но менее читабельно?
# Я понимаю что тут допустима некая пропорция.
# Так вот -  в этом моем ДЗ эта пропроция нарушена или нет?
with open(r"C:\Users\934\PycharmProjects\Netology\job1.5_PraktikaCiklov\students.txt") as inf:
    students = []
    counter_male, counter_exp = 0, 0
    for line in inf:
        if 'муж' in line:
            counter_male += 1
        if line.split()[3] == '1':
            counter_exp += 1
        students.append(line.split())


def avg_rating(students):
    # Формируем list() из средних оценок за ДЗ по каждому студенту
    for l in students:
        l[4:] = map(int, l[4:])
    avg_rating = []
    for i in students:
        avg_rating.append(sum(i[j] for j in range(4,9))/5)
    return(avg_rating)


def input_leter():
    n = input('''Нужно ввести букву
     r - средняя оценка за домашние задания и за экзамен по всем в группе;     
     s - средняя оценка за домашние задания и за экзамен по группе в разрезе (пол или опыт программирования);
     b - увидеть лучшего студента;
     q - ВЫХОД из программы;
  Итак начнем: ''')
    return n


def group_rating(students):
    avg_rating_group = sum(avg_rating(students))/len(students)
    avg_rating_exam = sum(students[i][9] for i in range(0,len(students)))/len(students)
    print('Средняя оценка за домашние задания по группе: {:.3}'.format(avg_rating_group))
    print('Средняя оценка за экзамен: {:.3}'.format(avg_rating_exam))
    print('-' * 2 * len(students))


def avg_rating_gen_exp_choice(students,n): # Вот тут особенно важно понять - можно так или ВООБЩЕ ТАК НЕЛЬЗЯ??
    avg_rating_group = avg_rating(students)
    if n == 'g':
        temp = ['муж', 'жен', 'мужчин', 'женщин', 2, counter_male, len(students)-counter_male]
    elif n == 'e':
        temp = ['1', '0', 'программистов', 'начинающих', 3, counter_exp, len(students)-counter_exp]
    avg_r = sum(students[i][9] for i in range(0,len(students)) if students[i][temp[4]] == temp[0])/temp[5]#sum(1 for i in students if i[temp[4]] == temp[0])  <- так вначале сделал
    avg_r1 = sum(students[i][9] for i in range(0,len(students)) if students[i][temp[4]] == temp[1])/temp[6]#sum(1 for i in students if i[temp[4]] == temp[1]) <- оставил для понимания
    sum_avg_r = 0
    for i in range(len(students)):
        if students[i][temp[4]] == temp[0]:
            sum_avg_r += avg_rating_group[i]
    print('Средняя оценка за ДЗ у {}: {:.3}'.format(temp[2], sum_avg_r / temp[5]))
    print('Средняя оценка за экзамен у {}: {:.3}'.format(temp[2], avg_r))
    print('Средняя оценка за ДЗ у {}: {:.3}'.format(temp[3], (sum(avg_rating_group) - sum_avg_r) / temp[6]))
    print('Средняя оценка за экзамен у {}: {:.3}'.format(temp[3], avg_r1))
    print('-' * 2 * len(students))


def avg_rating_gender_experience():
    n = input('В каком разрезе вы хотите посмотереть статистику? \n'
              'пол - нажмите g; опыт - нажмите e \n'
    'ВВЕДИТЕ букву(для выхода нажмите q): ')
    if n in 'ge':
        avg_rating_gen_exp_choice(students, n)
    elif n == 'q':
        return
    else:
        print("Будьте ВНИМАТЕЛЬНЕЕ!!")
    avg_rating_gender_experience()


def best_student(students):
    avg_rating_group = avg_rating(students)
    integral_rating = []
    for i in range(len(avg_rating_group)): # знаю, что так не верно делать цикл, но зато в 1 строку и сразу
        integral_rating.append(round(avg_rating_group[i]*0.6 + students[i][9]*0.4, 2))
    count_best = integral_rating.count(max(integral_rating)) # Вот тут ВОПРОС: КАК правильнее - заводить отдельную переменную или
    if count_best == 1: # подсовывать count сразу в if integral_rating.count(max(integral_rating)) == 1
        print('Лучший студент: {} {}'.format(students[integral_rating.index(max(integral_rating))][0],
              students[integral_rating.index(max(integral_rating))][1]), 'с интегральной оценкой {}'.format(max(integral_rating)))
    else:
        best_students = []
        for i in range(len(integral_rating)):
            if integral_rating[i] == max(integral_rating):
                best_students.append(students[i][0] + ' ' + students[i][1])
        print('Лучшие студенты: ' + ', '.join(best_students), 'c интегральной оценкой {}'.format(max(integral_rating)))
    print('-' * 2 * len(students))


def choice_leter(n): # пришлось сделать эту функцию, т.к. в main() предусмотрена ошибка ввода буквы и защита от Тролей!
    if n == 'r':
        group_rating(students)
    elif n == 's':
        avg_rating_gender_experience()
    elif n == 'b':
        best_student(students)
    elif n == 'q':
        exit()

def main():
    n = input_leter()
    if n not in 'rsbq':
        print('Вы ошиблись! Попробуйте еще раз и будьте внимательны!!!')
        n = input_leter()
        if n not in 'rsbq':
            print('Иди учиcь читать!!')
            exit()
        else:
            choice_leter(n)
    else:
        choice_leter(n)
    main()

main()