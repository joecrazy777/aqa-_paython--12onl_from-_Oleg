# 1.Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No".
# 2. Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза,
# результат свяжите с переменной big_int.
# 3. Измените значение, хранимое в переменной var_float, уменьшив его на единицу,
# результат свяжите с той же переменной.
# 4. Разделите var_int на var_float, а затем big_int на var_float. Результат данных
# выражений не привязывайте ни к каким переменным.
# 5. Измените значение переменной var_str на "NoNoYesYesYes". При формировании
# нового значения используйте операции конкатенации (+) и повторения строки (*).
# 6. Выведите значения всех переменных.


# 1
var_int = 10
var_float = 8.4
var_str = "No"


# 2
# var_int = 10
# big_int = var_int*3
# print(big_int)


def check(a=10):
    print(a * 3)


check()


# 3
# var_float = 8.4
# big_int = var_float -1
# print(big_int)
def minus(vaar=8.4):
    print(vaar - 1)


minus()
# 4
# print(var_int/var_float)
# print(big_int/var_float)
# 5

# print(var_str + "No"+"Yes"*3)


def str_yesno(a="No", b="Yes"):
    print(a + "No" + b * 3)


str_yesno()
