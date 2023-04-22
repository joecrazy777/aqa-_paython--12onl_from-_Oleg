def area_calculation(s_one, s_two):
    if type(s_one) == int and type(s_two) == int:
        year = 1
        while s_one > 0.1 * s_two:
            s_one *= 2
            s_two *= 3
            year += 1
        return s_one, s_two, year
    else:
        return "Error"
#1
a = "  my name is Slim    "
def remove_space(a):
    return a.strip()

#2
def numms(a=5, b=25):
    if a > b:
        return "Error"
    if type(a) == float or type(b) == float:
        return "Error"
    summ = 0
    for i in range(a, b + 1):
        summ += i

    return summ

#3
def factorial(n=21):
    result = 1
    if n < 0:
        raise ValueError("Error")
    for i in range(1, n + 1):
        result *= i
    return result
#4

def fields(s1=10, s2=10):
    years = 0
    while s1 > s2 * 0.1:
        s1 *= 2
        s2 *= 3
        years += 1
    return years