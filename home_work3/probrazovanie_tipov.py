# 1. Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
# 2. Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
# 3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
# строку => "I love arrays they are my favorite"
# 4. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
# 5.
# Есть 2 словаря
# a = { 'a': 1, 'b': 2, 'c': 3}
# b = { 'c': 3, 'd': 4,'e': 5}
# Необходимо их объединить по ключам, а значения ключей поместить в список, если у
# одного словаря есть ключ "а", а у другого нету, то поставить значение None на
# соответствующую позицию(1-я позиция для 1-ого словаря, вторая для 2-ого)
# ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}
# *1) Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число
# *2) Дан текст, который содержит различные английские буквы и знаки препинания. Вам
# необходимо найти самую частую букву в тексте. Результатом должна быть буква в
# нижнем регистре.
# При поиске самой частой буквы, регистр не имеет значения, так что при подсчете
# считайте, что "A" == "a". Убедитесь, что вы не считайте знаки препинания, цифры и
# пробелы, а только буквы.
# Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет
# буква, которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по
# одному разу, так что мы выбираем "e".
# "a-z" == "a"
# "Hello World!" == "l"
# "How do you do?" == "o"
# "One" == "e"
# "Oops!" == "o"
# "AAaooo!!!!" == "a"
# "a" * 9000 + "b" * 1000 == "a"


# 1

a = "Robin Singh"
list1 = "I love arrays they are my favorite"
# b = a.split()
# list2 = list1.split()
# print(b)
# print(list2)


def massive():
    bob = a.split()
    text1 = list1.split()
    print(bob)
    print(text1)


massive()


# 2
# name = ["Ivan", "Ivanou"]
# a = "Minsk"
# b = "Belarus"
# print("Привет" + " " + " ".join(name) + "!" + "Добро пожаловать в" + " " + a + " " + b)


def name1():
    name = ["Ivan", "Ivanou"]
    a = "Minsk"
    b = "Belarus"
    print(
        "Привет" + " " + " ".join(name) + "!" + "Добро пожаловать в" + " " + a + " " + b
    )


name1()

# 3
a = ["I", "love", "arrays", "they", "are", "my", "favorite"]
b = " ".join(a)
print(b)


def conn():
    print(b)


conn()


# 4
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list3.insert(2, 11)
# list3.pop(6)
# print(list3)


def delete():
    list3.insert(2, 11)
    list3.pop(6)
    print(list3)


delete()
# 5
a = {"a": 1, "b": 2, "c": 3}
b = {"c": 3, "d": 4, "e": 5}
ab = {}

for key, value in a.items():
    if key in b:
        ab[key] = [a[key], b[key]]
    else:
        ab[key] = [value, None]

for key, value in b.items():
    if key in a:
        ab[key] = [a[key], b[key]]
    else:
        ab[key] = [None, value]

print(ab)
#
list22 = [1, 5, 2, 9, 2, 9, 1]


text = [1, 5, 2, 9, 2, 9, 1]
# unique_numbers = list(set(text))
# print(unique_numbers)
