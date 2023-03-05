# Задание №1
a = -1.6
b = 2.99
print(round(a))
print(round(b))
# Задание №2
a = "www.my_site.com#about"
print(a.replace("#", "/"))
# Задание №3
a = "stroka" + "ing"
print(a)
b = "stroka"
c = "ing"
print(b + c)
# думаю сойдет за 3-й способ)
f = ["stroka", "ing"]
print("".join(f))
# Задание №4
a = "ivan ivanov"
b = a.split()
b.reverse()
print(" ".join(b))

# Задание №5
a = "    hello    "
print(a.strip())
# Задание №6
school = {
    "7Б": "23",
    "8А": "21",
    "2Е": "19",
    "3А": "15",
    "4Б": "17",
    "4В": "16",
    "7А": "15",
    "9В": "24",
    "10Д": "22",
    "11В": "15",
}
print(type(school))
print(len(school))
# Задание №7
list1 = [1, 17, 5, 177, 95, 11, 8, 12, 4545, 878, 989]
print(type(list1))

# Задание №8
print(str.__contains__("employment", "employ"))
# 2 способ
a = "employ"
b = "employment"
print("b" in "a")
# Задание 9
x = "My name is Agent Smith"
print(x[1])
print(x[3:16:3])
