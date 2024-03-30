a, b = map(int, input().split("x"))
radius = 6.5
diagonal = ((a ** 2 + b ** 2) ** 0.5)

if 2 * radius >= diagonal:
    print("Да")
else:
    print("Нет")