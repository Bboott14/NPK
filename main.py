import sys
import random

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QComboBox, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.inrus = ['Был понедельник и они шли к солнцу по канату', 'Вот маленький факт когда нибудь вы умрёте',
                      'Служить бы рад прислуживаться тошно', 'Лучшее путешествие то которое не имеет завершения',
                      'Сейчас или никогда', 'Умные нам не надобны надобны верные',
                      'Нельзя смешивать странное с таинственным',
                      'Ведь в медицине чаще всего лечит вера', 'Человек без сюрприза внутри в своём ящике неинтересен',
                      'Пустое сердце бьется ровно', 'Это всего лишь жизнь и мы прорвемся',
                      'Два хороших человека всегда могут договорится',
                      'Что хочешь помнить то всегда помнишь', 'Большой брат следит за тобой']
        self.letters = ['привет', 'солнце', 'счастье', 'любовь', 'знания', 'мир', 'вера', 'страна', 'будущее', 'путь',
                        'шкатулка', 'шакал', 'идея', 'глаза', 'телефон', 'забота', 'кубик', 'пересечение', 'полость',
                        'клоун', 'знамя', 'Королевство', 'Песня', 'зима', 'природа', 'пожалуйста', 'скрепление',
                        'программа', 'кино', 'пеликан']
        self.alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.alf2 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.alf2 = list(self.alf2)
        self.alf = list(self.alf)
        self.alfres = 'ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБА'
        self.alfres = list(self.alfres)

    def setupUi(self):
        self.setGeometry(300, 250, 1200, 750)
        self.setWindowTitle('Шифруля')

        self.label3 = QLabel(self)
        self.label3.setText("Тренажер для практики в шифровке и дешифровке"
                            " текста. \n\n\nСейчас вам предложенно два варианта практики.\n"
                            "В первом вариантам вы будете вводить фразу для шифровки"
                            " или дешифровки, а потом проверять правильность перевода.\n"
                            "Во втором варианте будет дан выбор уровня "
                            "сложности и фразы будут генерироваться автоматически.")
        self.label3.move(120, 200)

        self.slf1 = QPushButton(self)
        self.slf1.setGeometry(200, 400, 250, 40)
        self.label1 = QLabel(self)
        self.label1.setText("Интерективный вариант")
        self.label1.move(200, 370)
        self.slf1.setText("Начать")
        self.slf1.clicked.connect(self.run)

        self.slf2 = QPushButton(self)
        self.slf2.setGeometry(500, 400, 250, 40)
        self.label2 = QLabel(self)
        self.label2.setText("Режимный вариант")
        self.label2.move(500, 370)
        self.slf2.setText("Начать")
        self.slf2.clicked.connect(self.run2)

        self.line = QLineEdit(self)
        self.line.setGeometry(250, 250, 350, 30)
        self.line.hide()
        self.comboBox_3 = QComboBox(self)
        self.comboBox_3.setGeometry(20, 30, 250, 30)
        self.comboBox_3.hide()
        self.comboBox_3.addItem('Не выбрано')
        self.comboBox_3.addItem('Цезарь')
        self.comboBox_3.addItem('Шифр Хилла')
        self.comboBox_3.addItem('Щифр Виженера')
        self.comboBox_3.addItem('Атбаш')

        self.slf = QPushButton(self)
        self.slf.setGeometry(250, 300, 250, 40)
        self.slf.setText("Начать")
        self.slf.hide()
        self.slf.clicked.connect(self.run3)

        self.slf = QPushButton(self)
        self.slf.setGeometry(250, 300, 250, 40)
        self.slf.setText("Расшифровать")
        self.slf.hide()
        self.slf.clicked.connect(self.run3)

        self.slf4 = QPushButton(self)
        self.slf4.setGeometry(250, 500, 250, 40)
        self.slf4.setText("Вперед")
        self.slf4.hide()
        self.slf4.clicked.connect(self.run3)

        self.slf5 = QPushButton(self)
        self.slf5.setGeometry(350, 250, 250, 40)
        self.slf5.setText("Легко")
        self.slf5.hide()
        self.slf5.clicked.connect(self.run5)

        self.slf6 = QPushButton(self)
        self.slf6.setGeometry(350, 400, 250, 40)
        self.slf6.setText("Сложно")
        self.slf6.hide()
        self.slf6.clicked.connect(self.run5)

        self.slf9 = QPushButton(self)
        self.slf9.setGeometry(10, 700, 250, 40)
        self.slf9.setText("<=назад")
        self.slf9.hide()
        self.slf9.clicked.connect(self.run7)

        self.slf7 = QPushButton(self)
        self.slf7.setGeometry(550, 400, 250, 40)
        self.slf7.setText("Посмотреть ответ")
        self.slf7.hide()
        self.slf7.clicked.connect(self.run6)

        self.label8 = QLabel(self)
        self.label8.setText("")
        self.label8.move(550, 400)
        self.label8.hide()

        self.linechoise = QLineEdit(self)
        self.linechoise.setGeometry(280, 30, 250, 30)
        self.linechoise.setText("Введите ключ")
        self.linechoise.hide()

        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(280, 30, 250, 30)
        self.comboBox.hide()
        self.comboBox.addItems(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
        '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32'])

        self.label6 = QLabel(self)
        self.label6.setText("Программа работает в режиме")
        self.label6.move(500, 550)

        self.slf8 = QPushButton(self)
        self.slf8.setGeometry(500, 600, 250, 40)
        self.slf8.setText('Шифровки')
        self.slf8.clicked.connect(self.run8)

    def run8(self):
        if self.slf8.text() == 'Шифровки':
            self.slf8.setText('Расшифровки')
        else:
            self.slf8.setText('Шифровки')

    def run7(self):
        self.label2.show()
        self.label2.setText("Режимный вариант")
        self.label1.show()
        self.label6.show()
        self.slf8.show()
        self.comboBox.hide()
        self.linechoise.hide()
        self.line.setText('')
        self.line.setEnabled(True)
        self.slf4.hide()
        self.slf5.hide()
        self.slf6.hide()
        self.slf7.hide()
        self.slf9.hide()
        self.line.hide()
        self.comboBox_3.hide()
        self.label8.hide()
        self.slf1.show()
        self.slf2.show()
        self.label3.show()

    def run6(self):
        self.comboBox.hide()
        self.slf7.hide()
        self.linechoise.hide()
        self.label8.setText(f"{self.m}")
        self.label8.show()
        self.slf8.hide()

    def run5(self):
        self.label6.hide()
        self.slf8.hide()
        self.comboBox.hide()
        self.slf6.hide()
        self.linechoise.hide()
        self.slf5.hide()
        self.comboBox_3.show()
        self.line.show()
        self.slf4.show()
        self.line.setEnabled(False)
        if self.sender().text() == "Сложно":
            self.line.setText(f'{random.choice(self.inrus)}')
        else:
            self.line.setText(f'{random.choice(self.letters)}')

    def run(self):
        self.label6.hide()
        self.slf8.hide()
        self.comboBox.hide()
        self.slf9.show()
        self.label3.hide()
        self.label2.hide()
        self.label1.hide()
        self.slf2.hide()
        self.slf1.hide()
        self.linechoise.hide()
        self.slf4.show()
        self.line.show()
        self.comboBox_3.show()

    def run2(self):
        self.label6.hide()
        self.slf8.hide()
        self.label3.hide()
        self.label2.hide()
        self.label1.hide()
        self.slf2.hide()
        self.slf1.hide()
        self.slf9.show()
        self.slf5.show()
        self.linechoise.hide()
        self.slf6.show()
        self.comboBox.hide()

    def run3(self):
        self.slf8.hide()
        self.label6.hide()
        self.comboBox.hide()
        self.linechoise.hide()
        self.slf7.hide()
        self.label8.hide()
        self.label2.hide()
        self.m = ''
        if self.comboBox_3.currentText() == 'Цезарь' and self.slf8.text() == 'Шифровки':
            self.comboBox.show()
            a = int(self.comboBox.currentText())
            a = a % 33
            for i in self.line.text():
                if i == ' ':
                    self.m += ' '
                elif ord(i) >= 1040 and ord(i) <= 1103:
                    c = ord(i) + a
                    if ord(i) >= 1040 and ord(i) <= 1071:
                        if c > 1071:
                            self.m += chr(c - 32)
                        else:
                            self.m += chr(c)
                    elif ord(i) >= 1072 and ord(i) <= 1103:
                        if c > 1103:
                            self.m += chr(c - 32)
                        else:
                            self.m += chr(c)
                else:
                    self.m += i
        elif self.comboBox_3.currentText() == 'Цезарь' and self.slf8.text() == 'Расшифровки':
            self.comboBox.show()
            a = int(self.comboBox.currentText())
            a = a % 33
            for i in self.line.text():
                if i == ' ':
                    self.m += ' '
                elif ord(i) >= 1040 and ord(i) <= 1103:
                    c = ord(i) - a
                    if ord(i) >= 1040 and ord(i) <= 1071:
                        if c <= 1039:
                            self.m += chr(c + 32)
                        else:
                            self.m += chr(c)
                    elif ord(i) >= 1072 and ord(i) <= 1103:
                        if c <= 1071:
                            self.m += chr(c + 32)
                        else:
                            self.m += chr(c)
                else:
                    self.m += i
        elif self.comboBox_3.currentText() == 'Атбаш' and self.slf8.text() == 'Шифровки':
            self.linechoise.hide()
            for i in self.line.text():
                if i == ' ' or i == '.' or i == '!' or i == ',' or i == '?' or i == '-':
                    self.m += i
                elif i == i.upper():
                    q = self.alf.index(i)
                    self.m += self.alfres[q]
                else:
                    q = self.alf.index(i.upper())
                    self.m += self.alfres[q].lower()
        elif self.comboBox_3.currentText() == 'Атбаш' and self.slf8.text() == 'Расшифровки':
            self.linechoise.hide()
            for i in self.line.text():
                if i == ' ' or i == '.' or i == '!' or i == ',' or i == '?' or i == '-':
                    self.m += i
                elif i == i.upper():
                    q = self.alfres.index(i)
                    self.m += self.alf[q]
                else:
                    q = self.alfres.index(i.upper())
                    self.m += self.alf[q].lower()
        elif self.comboBox_3.currentText() == 'Щифр Виженера' and self.slf8.text() == 'Шифровки':
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
        elif self.comboBox_3.currentText() == 'Шифр Хилла' and self.slf8.text() == 'Расшифровки':
            self.alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
            self.alf = list(self.alf)
            e = 0
            e1 = 0
            c = 0
            if len(self.line.text()) % 2 == 1:
                n = self.line.text() + " "
            else:
                n = self.line.text()
            for i in n:
                if i == " ":
                    e1 = e
                    e = 33
                    c += 1
                elif i.upper() in self.alf:
                    e1 = e
                    print(e1)
                    e = self.alf.index(i.upper())
                    print(e)
                    c += 1
                if c % 2 == 0:
                    e2 = abs(7 * e1 - 3 * e)
                    e = -2 * e1 + e
                    e1 = e2
                    print(e1, e)
                    self.m += self.alf[e1 % 34].lower()
                    self.m += self.alf[e % 34].lower()
                    print(self.m)
        elif self.comboBox_3.currentText() == 'Шифр Хилла' and self.slf8.text() == 'Шифровки':
            self.alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
            self.alf = list(self.alf)
            e = 0
            c = 0
            e1 = 0
            if len(self.line.text()) % 2 == 1:
                n = self.line.text() + " "
            else:
                n = self.line.text()
            for i in n:
                if i == " ":
                    e1 = e
                    e = 33
                    c += 1
                elif i.upper() in self.alf:
                    e1 = e
                    print(e1)
                    e = self.alf.index(i.upper())
                    print(e)
                    c += 1
                if c % 2 == 0:
                    e2 = 1 * e1 + 3 * e
                    e = 2 * e1 + 7 * e
                    e1 = e2
                    print(e1, e)
                    self.m += self.alf[e1 % 34].lower()
                    self.m += self.alf[e % 34].lower()
                    print(self.m)
        self.slf7.show()

    def run4(self):
        self.slf7.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

