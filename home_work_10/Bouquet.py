# создаем класс Цветок
class Flower:
    def __init__(self, name, price, lifespan):
        self.name = name
        self.price = price
        self.lifespan = lifespan

    def print_flower(self):
        print("Цветок: {} Стоимость: {} Время жизни: {}".format(self.name, self.price, self.lifespan))


# создаем класс Букет
class Bouquet:
    def __init__(self, name, flowers):
        self.name = name
        self.flowers = flowers
        self.accessories = []
        self.cost = sum([flower.price for flower in self.flowers])

    # добавляем аксессуары
    def add_accessories(self, accessories):
        self.accessories = accessories
        self.cost += sum([accessory.price for accessory in accessories])

    # находим среднее время жизни цветов в букете
    def find_avg_lifespan(self):
        lifespan_sum = sum([flower.lifespan for flower in self.flowers])
        return lifespan_sum / len(self.flowers)

    # сортируем цветы по стоимости
    def sort_flowers(self):
        return sorted(self.flowers, key=lambda x: x.price)

    # проверяем, есть ли цветок в букете
    def has_flower(self, flower_name):
        for flower in self.flowers:
            if flower.name == flower_name:
                return True
        return False


# создаем цветы
rose = Flower("Роза", 100, 5)
tulip = Flower("Тюльпан", 50, 3)
lily = Flower("Лилия", 80, 7)

# создаем букет
bouquet = Bouquet("Весенний", [rose, tulip, lily])

# добавляем аксессуары
bouquet.add_accessories([Accessory("Лента", 10), Accessory("Упаковка", 5)])

# выводим информацию о букете и его стоимости
print("Название букета:", bouquet.name)
print("Цветы в букете:")
for flower in bouquet.flowers:
    flower.print_flower()
print("Аксессуары в букете:")
for accessory in bouquet.accessories:
    accessory.print_accessory()
print("Стоймость букета:", bouquet.cost)

# находим среднее время жизни цветов в букете
print("Среднее время жизни цветов в букете:", bouquet.find_avg_lifespan())

# сортируем цветы по стоимости
sorted_flowers = bouquet.sort_flowers()
print("Цветы в букете, отсортированные по стоимости:")
for flower in sorted_flowers:
    flower.print_flower()

# проверяем, есть ли цветок в букете
if bouquet.has_flower("Роза"):
    print("В букете есть розы")
else:
    print("В букете нет роз")
