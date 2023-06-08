# 1 Создать lambda функцию, которая принимает на вход имя и выводит его в формате “Hello, {name}

name = "Oleg"
func = lambda: "Hello" + "," + name
print(func())

# 2 Создать lambda функцию, которая принимает на вход
# список имен и выводит их в формате “Hello, {name}” в
# другой список

names = ["kate", "mike", "alex"]
same = []

for i in names:
    f = lambda i: "Hello" + " " + i
    same.append(f(i))
    print(same)
