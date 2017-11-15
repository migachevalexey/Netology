#https://github.com/bobrynya/netology5

class Animal:

    state_animal = ['live', 'sick', 'dead']

    def __init__(self, type_animal, name, state=state_animal[0]):
        self.type_animal = type_animal
        self.name = name
        self.state = state  # по сути оно не нужно. Атавизм

    def change_state(self, n=True):
        if not n:
            self.state[self.state.index('sick')] = 'dead'
            print('Умерла {} :-(. Осталось {}'.format(self.name))
        elif n:
            self.state = self.state_animal[1]
            print(f'Заболела {self.name}. Надо вызвать ветеринара!')

    def feed(self):
        if self.type_animal == 'рогатые':
            print('{}: корм сено'.format(self.name.title()))
        elif self.type_animal == 'водоплавающие':
            print('{}: корм зерно'.format(self.name.title()))
        else:
            print('Свиней кормим отходами')

    def walk(self, time, duration):
        print('Отправляем животных на прогулку в {0} {2} на {1} {2}'.format(time, duration, 'часов'))


class Animals(Animal):
    """
    quant - колво животных в стаде
    stado_state - тут состояние каждого животного в стаде
    stado_state_vsego - общее сотсояние стада - list('live', 'sick', 'dead', 'mix')
    
    """
    quant = 0
    Animal.state_animal.append('mix')
    stado_state = []

    def __init__(self, type_animal, name, stado_state_vsego='live'):
        self.stado_state_vsego = stado_state_vsego
        super().__init__(type_animal, name)

    def add(self, n):
        self.quant += n
        self.stado_state += [self.state] * n
        print('Добавилось {}шт {}. Теперь их в стаде {}'.format(n, self.name, self.quant))

    def kill(self, n):
        # n - сколько забили. Их сразу увозят с фермы!

        if self.quant >= n and self.stado_state.count('live') >= n:
            self.quant -= n
            for _ in range(n):
                self.stado_state.remove('live')
            print('Пришлось убить {}шт {} :-(. Кушать хочется. '
                  'Осталось {}шт. из них болееют {}'.format(n, self.name, self.quant, self.state.count('sick')))
        else:
            print('Столько({}шт) {} у нас просто нет. Их всего {}'.format(n, self.name, self.quant))

    def change_state(self, n=True, m=1):

        # n = False - умерло, True - заболело, m - колво для заболевших
        # умереть может только больное животное

        if not n and self.stado_state.count('sick') > 0:
            self.stado_state[self.stado_state.index('sick')] = self.state_animal[2]
            self.stado_state_vsego = 'mix'
            print('Умерла {} (болела бедняга), ветеринар не успел :-(. '
                  'Здоровых осталось {}, больных {}'.format(self.name, self.stado_state.count('live'), self.stado_state.count('sick')))
        elif not n and self.stado_state.count('sick') == 0:
            print(
                'Умертвить здоровое животное Нельзя, т.к. здоровое животное просто так умереть не может, а больных у нас нет!')
        elif n:  # заболело
            for _ in range(m):
                self.stado_state[self.stado_state.index('live')] = self.state_animal[1]
            self.stado_state_vsego = 'mix'
            print(f'Заболела {self.name} {m}шт. Итого у нас больных {self.stado_state.count(self.state_animal[1])}шт.',
                  end=' ')
            if self.stado_state.count(self.state_animal[1]) < 3:
                print('Надо бы вызвать ветеринара!')
            elif self.stado_state.count(self.state_animal[1]) > 2:
                print('СРОЧНО ВЫЗВАТЬ ВЕТЕРИНАРА!')

    def navedem_poryadok(self):
        self.quant = self.stado_state.count(self.state_animal[0]) + self.stado_state.count(self.state_animal[1])
        self.stado_state.clear()
        self.stado_state = [self.state_animal[0]] * self.quant
        self.stado_state_vsego = 'live'
        print('Приехал ветеринар, больных - вылечил, мертвых - забрал. '
              'Итого у нас сейчас {} {}'.format(self.quant, self.name))


stado = Animals('рогатые', 'коза')
# print(stado.__dict__)
# print(Animal.state_animal)
# stado.add(5)
# stado.change_state()
# stado.feed()
# print(stado.stado_state)
# stado.add(3)
# stado.feed()
# stado.kill(2)
# stado.change_state(False)
# stado.change_state(1, 2)
# stado.navedem_poryadok()


class Goats(Animals):
    product = 'milk'
    kolvo_product = 10  # per unit
    vsego_kolvo_product = 0
    nadoi = 0

    def __init__(self, type_animal='рогатые', name='коза'):
        super().__init__(type_animal, name)

    def feed(self, n, m):
        # Подукцию дают только здоровые животные
        super().walk(n, m)
        super().feed()
        self.vsego_kolvo_product = self.stado_state.count(self.state_animal[0]) * self.kolvo_product
        print(f'Покромили, погуляли, нагуляли - {self.vsego_kolvo_product}л {self.product}')

    def doika(self):
        self.nadoi += self.vsego_kolvo_product
        print(f'Надоили {self.vsego_kolvo_product}л {self.product}. Всего у нас {self.nadoi}л')
        self.vsego_kolvo_product = 0

    def sale(self, price, quant):
        if quant<=self.nadoi:
            print(f'Продали {quant}л. {self.product}. Получили за него {price*quant}руб.')
            self.nadoi -= quant
        else: print(f'{quant}л. молока мы еще не собрали. У нас всего {self.nadoi}')


# print('----------------------')
# g_dead = Goats()
# g_dead.stado_state_vsego = 'dead' # стадо мертвых коз
# print(g_dead.name, g_dead.stado_state, 'Состояние стада -', g_dead.stado_state_vsego)
# print(Goats.mro())
g = Goats()  # стадо здоровых коз
g.add(7)
g.kill(2)
g.change_state(True, 2)
print('Состяние всего стада - ', g.stado_state_vsego)
g.change_state(False)
print('----------------------')
g.feed(3, 4)
g.doika()
g.navedem_poryadok()
print('Состяние всего стада - ', g.stado_state_vsego)
g.feed(5, 6)
g.doika()
g.sale(45,1000)
print('----------------------')
g.add(1)
g.feed(7, 10)
