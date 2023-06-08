# 4 Даны два файла произвольного типа. Поменять местами их содержимое. Файлы должны быть бинарного типа
# 5 Все функции обработки файлов писать в новой папке, использовать пакеты, вызов методов использовать в файле main.py, использовать git, не забывать про читабельность ветки, описания коммитов и описания ПР
# 6 Добавить в созданные функцию аннотации и документирование
# 19 февраля 2023 г.


with open("new_file.txt", "a") as file:
    file.write("10 ,20, 30, 40")

# 1 Дан файл целых чисел, содержащий не менее четырех элементов. Вывести первый, второй, предпоследний и последний элементы данного

with open("new_file.txt", "r") as file:
    for line in file:
        a = line.split()
print(a[0:2:1])
print(a[-1:-3:-1])

# 2 Дан файл целых чисел. Создать два новых файла, первый из которых содержит четные числа из исходного файла, а второй — нечетные (в том же порядке).

with open("file_1", "r") as file1:
    a = open("file_2.txt", "w")
    b = open("file3.txt", "w")
    for line1 in file1:
        ab = line1.split(",")
        for i in ab:
            i2 = int(i)
            if i2 % 2 == 0:
                i3 = str(i2) + " "
                a.write(i3)
            if i2 % 2 != 0:
                i4 = str(i2) + " "
                b.write(i4)

# 3 Дан файл вещественных чисел. Заменить в нем все элементы на их квадраты.

with open("float_numbers") as f:
    number_lines = f.readlines()

with open("float_numbers", "w") as f:
    for line in number_lines:
        line = line.split()
        f.write(
            "{}\n".format(" ".join(map(lambda x: str(round(float(x) ** 2, 2)), line)))
        )
