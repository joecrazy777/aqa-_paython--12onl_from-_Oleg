import unittest

def fields(s1=10, s2=10):
    years = 0
    while s1 > s2 * 0.1:
        s1 *= 2
        s2 *= 3
        years += 1
    return years

# 1. Убедиться, что функция работает корректно для любых значений  s1 и s2
# 2. Убедиться, что функция работает корректно для  значений  когда  s1 > s2 и s1 > s2
# 2. Создать переменную years и присвоить ей значение 0.
# 3. Проверить, что условие while верно: s1 > s2 * 0.1.
# 4. Умножить s1 на 2 и присвоить это значение переменной s1.
# 5. Умножить s2 на 3 и присвоить это значение переменной s2.
# 6. Увеличить переменную years на 1.
# 7. Если условие while неверное, вывести значение переменной years.


class TestFields(unittest.TestCase):

    def test_example_values_1(self):
        self.assertEqual(fields(10, 10), 6)

    def test_example_values_2(self):
        self.assertEqual(fields(100, 10), 12)

    def test_example_values_3(self):
        self.assertEqual(fields(1000, 10), 18)

    def test_small_initial_difference(self):
        self.assertEqual(fields(10, 1), 12)

    def test_s2_greater_than_s1(self):
        self.assertEqual(fields(5, 10), 4)
