import math
a = input()
b = int(input())
if a[:2] == 'x^':
    print(round(int(a[-1]) * math.pow(b, int(a[-1]) - 1), 3))
if a[1:] == '^x':
    print(round(math.pow(int(a[0]), b) * math.log10(b), 3))
if a == 'ln(x)':
    print(round(1 / b, 3))
if a == 'tg(x)':
    print(round(1 / (math.cos(b) ** 2), 3))
if a == 'ctg(x)':
    print(round(- 1 / (math.sin(b) ** 2), 3))

