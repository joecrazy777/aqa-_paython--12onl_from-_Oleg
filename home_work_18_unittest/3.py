import unittest


def factorial(n=21):
    result = 1
    if n < 0:
        raise ValueError("Error")
    for i in range(1, n + 1):
        result *= i
    return result

# 1. Убедиться, что функция работает корректно для любых значений n от 0 до 21.
# 2. Использовать изменяемую переменную вместо нескольких присвоений для увеличения читаемости кода.
# 3. Разместить код внутри функции, которая будет принимать на вход значение n и возвращать результат произведения всех чисел от 1 до n.
# 4. В случае, если на вход функции будет передано значение n меньше 0, возбудить исключение с соответствующим сообщением.


class TestFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_positive(self):
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_negative(self):
        self.assertRaises(ValueError, factorial, -5)



