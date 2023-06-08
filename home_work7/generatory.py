numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

a = [nums for nums in numbers if nums > 0]
print(a)

pos = []


def pozitive_numbers(arr):
    for i in arr:
        if i > 0:
            yield i


for i in pozitive_numbers(numbers):
    pos.append(i)
print(pos)

# 2
test_string = "thequick brown fox jumps over the lazy dog"

res = list(map(len, test_string.split()))
# res = list(map(len, test_string.split()))
print(res)
