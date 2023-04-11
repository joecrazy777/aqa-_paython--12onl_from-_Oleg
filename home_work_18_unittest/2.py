def numms(a=5, b=25):
    summ = 0
    for i in range(a, b + 1):
        summ += i
    return summ


print(numms())
#
# 1. Проверить, что функция принимает правильное количество аргументов (2).
# 2. Проверить, что аргументы являются числами и входят в диапазон допустимых значений (a < b,a > b, a и b - целые числа).
# 3. Создать переменную "summ" и присвоить ей значение 0.
# 4. Итерироваться по диапазону от a до b + 1, включительно, с помощью цикла for.
# 5. На каждой итерации добавлять значение i к переменной "summ".
# 6. После завершения цикла вернуть значение "summ".
# 7. Написать тесты для проверки работы функции с различными аргументами.
# 8. Проверить, что функция возвращает правильный результат для различных входных данных.


import unittest


def numms(a=5, b=25):
    if a > b:
        return "Error"
    if type(a) == float or type(b) == float:
        return "Error"
    summ = 0
    for i in range(a, b + 1):
        summ += i

    return summ


class TestNumms(unittest.TestCase):
    def test_numms(self):
        self.assertEqual(numms(2, 10), 54)
        self.assertEqual(numms(3, 12), 75)
        self.assertEqual(numms(4, 19), 184)


    def test_numms_great(self):
        self.assertEqual(numms(25, 5), "Error")
    #
    #
    def test_arguments_type(self):
        with self.assertRaises(TypeError):
            numms(4, 10.4)
