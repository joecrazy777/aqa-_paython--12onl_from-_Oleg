from main import remove_space
import unittest
# 1. Определите строку, с которой нужно работать
# 2. Убедитесь, что  корректно удаляются пробелы с обеих сторон строки
# 3. Убедитесь, что  корректно удаляются пробелы с левой  стороны строки
# 4. Убедитесь, что  корректно удаляются пробелы с правой стороны строки
# 5. Убедитесь, что  корректно удаляются пробелы из пустой  строки с пробелом
# 6. Проверить,что функция не возвращает None
# 7. Проверить,что функция возвращает новую строку, а не изменяет исходную строку
# 8. Убедиться,что функции будет возвращать ValueError ,если не задать ей аргумент






class TestString(unittest.TestCase):
    def test_remove_space(self):
        self.assertEqual(remove_space("  abc "), "abc")
        self.assertEqual(remove_space("  abc"), "abc")
        self.assertEqual(remove_space("abc  "), "abc")
        self.assertEqual(remove_space(" "), "")


    def test_remove_space_is_not_none(self):
        self.assertIsNotNone(remove_space("abc"), not None)

    def test_remove_space_not_new_string(self):
        text = "  hello  "
        self.assertEqual(remove_space(text), "hello")

    def test_remove_space_arguments(self):
        with self.assertRaises(TypeError):
            remove_space()

       
