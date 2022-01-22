alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alf = list(alf)
alf2 = 'БВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯА'
alfres = list(alf2)
m = ""
c = 'сигма'
n = 'Берегитесь феникса'
c = list(((len(n) // len(c)) + 1) * c)
print(c)
b = 0
for i in range(len(n)):
    if n[i] == ' ':
        m += ' '
        b += 1
    elif n[i] == n[i].upper():
        q = c[i - b]
        print(q)
        x = alf2[alf.index(q.upper()):] + alf2[:alf.index(q.upper())]
        print(x)
        m += x[alf.index(n[i])]
    else:
        q = c[i - b]
        print(q)
        x = alf2[alf.index(q.upper()):] + alf2[:alf.index(q.upper())]
        print(x)
        m += x[alf.index(n[i].upper())].lower()
print(m)
