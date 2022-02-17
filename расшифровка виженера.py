elif self.comboBox_3.currentText() == 'Щифр Виженера' and self.slf8.text() == 'Расшифровки':
self.linechoise.show()
c = ''.join(self.linechoise.text().split())
n = self.line.text()
c = list(((len(n) // len(c)) + 1) * c)
print(c)
b = 0
for i in range(len(n)):
    if n[i] == ' ' or n[i] == '.' or n[i] == '!' or n[i] == ',' or n[i] == '?' or n[i] == '-':
        self.m += n[i]
        b += 1
    elif n[i] == n[i].upper():
        q = c[i - b]
        x = self.alf2[self.alf.index(q.upper()):] + self.alf2[:self.alf.index(q.upper())]
        self.m += x[self.alf.index(n[i])]
    else:
        q = c[i - b]
        x = self.alf2[self.alf.index(q.upper()):] + self.alf2[:self.alf.index(q.upper())]
        self.m += x[self.alf.index(n[i].upper())].lower()