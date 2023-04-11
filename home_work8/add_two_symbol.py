# @typed(type=’str’)
# def add_two_symbols(a, b):
# return a + b
def check_type(choose_type):
    def decorate(func):
        def wrapper(*args):
            num = []
            for arg in args:
                if choose_type == "str":
                    num.append(str(arg))
                elif choose_type == "int":
                    num.append(int(arg))
            return func(*num)

        return wrapper

    return decorate


@check_type("str")
def add_symbol(a, b):
    return a + b


print(add_symbol("3", 5))


@check_type("str")
def add_two_symbols2(a, b):
    return a + b


print(add_two_symbols2(5, 5))


@check_type("str")
def add_two_symbols3(a, b):
    return a + b


print(add_two_symbols3("a", "b"))
