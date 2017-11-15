class Animal:
    type = 'животное с фермы'
    food = None
    sound = None

    def __init__(self):
        pass

    def speak(self):
        print('Я издаю звук "{}"'.format(self.sound))

    def about(self):
        print('Это {}. Оно ест {}.'.format(self.type, self.food))


class Hoofed(Animal):  # рогатые
    diff_type = 'рогатые'
    food = 'трава'

    def __init__(self):
        pass

    def about(self):
        super().about()
        print('Так как это {}, то у них есть и копыта!'.format(self.diff_type))


class Cow(Hoofed):  # корова
    subtype = 'корова'
    product = 'молоко'
    sound = 'Муууу'

    def __init__(self, name, quant_product, color='коричневый'):
        self.color = color
        self.name = name
        self.quant_product = quant_product

    def about(self):
        print(f'Я {self.subtype}, меня зовут {self.name}. '
              f'Мой рацион {self.food} и я даю {self.product}, {self.quant_product}л в день')


class Goat(Hoofed):  # коза
    subtype = 'коза'
    food = 'трава+сено'
    sound = 'Беее'
    product = 'козье молоко(оно полезнее)'

    def __init__(self, name, quant_product, color='белый'):
        self.name = name
        self.color = color
        self.quant_product = quant_product

    def about(self):
        print(f'Я {self.subtype}, меня зовут {self.name}. '
              f'Мой рацион {self.food} и я даю {self.product}, {self.quant_product}л в день')


class Bird(Animal):
    diff_type = 'птица'
    food = 'зерно'

    def __init__(self):
        pass

    def about(self):
        super().about()
        print('Так как это {}, то у них есть клюв!'.format(self.diff_type))


class Chicken(Bird):  # курица
    subtype = 'курица'
    food = 'зерно,червяки'
    sound = 'Ко-ко-ко'
    product = 'яйца'

    def __init__(self, quant_product, color='пестрый'):
        self.color = color
        self.quant_product = quant_product

    def about(self):
        print(f'Я {self.subtype}, меня никак не зовут. '
              f'Мой рацион {self.food} и я даю {self.product}, {self.quant_product}шт в день')


class Duck(Bird):  # утка
    subtype = 'утка'
    food = 'зерно,червяки,водросли'
    sound = 'Кря-кря'
    product = 'яйца'
    habitat = 'вода'

    def __init__(self, quant_product, color='серый'):
        self.color = color
        self.quant_product = quant_product

    def about(self):
        super().about()
        print(f'Я {self.subtype}, меня никак не зовут. '
              f'Я даю {self.product}, {self.quant_product}шт в день')
        print(f'У меня есть особенность, среда моего обитания - {self.habitat}!')


def main():
    dunya = Cow('Дунька', 10, 'black')
    dunya.about()
    burenka = Cow('Буренка', 12)
    burenka.about()
    burenka.speak()
    print('----------------')
    mashka = Goat('Машка', 3, )
    mashka.about()
    mashka.speak()
    print(f'{mashka.type} -> {mashka.diff_type} -> {mashka.subtype}')
    print(mashka.color)
    print('----------------')
    br = Bird()
    print('Основной рацион птиц - ', br.food)
    br.about()
    kur = Chicken(2, 'черный')
    kur.about()
    print(kur.color)
    print('----------------')
    ut = Duck(1)
    ut.about()


if __name__ == '__main__':
    main()
