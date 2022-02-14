import sys
import random

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QComboBox, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.alf2 = 'БВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯА'
        self.alf2 = list(self.alf2)
        self.alf = list(self.alf)
        self.alfres = 'ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБА'
        self.alfres = list(self.alfres)

    def setupUi(self):
        self.setGeometry(300, 250, 1000, 750)
        self.setWindowTitle('Шифруля')

        self.label3 = QLabel(self)
        self.label3.setText("   Тренажер для практики в шифровке текста. \n\n\nСейчас вам предложенно два варианта практики.\n"
        "В первом вариантам вы будете вводить фразу для шифровки, а потом проверять правильность перевода.\n"
        "Во втором варианте будет дан выбор уровня сложности и фразы будут генерироваться автоматически.")
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
        self.line1 = QLineEdit(self)
        self.line1.setGeometry(250, 450, 350, 30)
        self.line1.hide()
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
        self.slf4.clicked.connect(self.run4)

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

        self.slf7 = QPushButton(self)
        self.slf7.setGeometry(550, 400, 250, 40)
        self.slf7.setText("Посмотреть ответ")
        self.slf7.hide()
        self.slf7.clicked.connect(self.run6)

        self.label8 = QLabel(self)
        self.label8.setText("")
        self.label8.move(550, 400)
        self.label8.hide()

    def run6(self):
        self.slf7.hide()
        self.label8.setText(f"{self.m}")
        self.label8.show()


    def run5(self):
        self.slf6.hide()
        self.slf5.hide()
        self.slf.show()
        self.comboBox_3.show()
        self.line.show()
        self.line.setEnabled(False)
        self.line.setText('Цезарь был не дурак!')

    def run(self):
        self.label3.hide()
        self.label2.hide()
        self.label1.hide()
        self.slf2.hide()
        self.slf1.hide()
        self.slf.show()
        self.line.show()
        self.comboBox_3.show()


    def run2(self):
        self.label3.hide()
        self.label2.hide()
        self.label1.hide()
        self.slf2.hide()
        self.slf1.hide()
        self.slf5.show()
        self.slf6.show()


    def run3(self):
        self.slf7.hide()
        self.label8.hide()
        self.label2.hide()
        self.line1.show()
        a = 3
        self.m = ''
        if self.comboBox_3.currentText() == 'Цезарь':
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
        elif self.comboBox_3.currentText() == 'Атбаш':
            for i in self.line.text():
                if i == ' ':
                    self.m += ' '
                elif i == i.upper():
                    q = self.alf.index(i)
                    self.m += self.alfres[q]
                else:
                    q = self.alf.index(i.upper())
                    self.m += self.alfres[q].lower()
        elif self.comboBox_3.currentText() == 'Щифр Виженера':
            c = 'сигма'
            n = self.line.text()
            c = list(((len(n) // len(c)) + 1) * c)
            print(c)
            b = 0
            for i in range(len(n)):
                if n[i] == ' ':
                    self.m += ' '
                    b += 1
                elif n[i] == n[i].upper():
                    q = c[i - b]
                    x = self.alf2[self.alf.index(q.upper()):] + self.alf2[:self.alf.index(q.upper())]
                    self.m += x[self.alf.index(n[i])]
                else:
                    q = c[i - b]
                    x = self.alf2[self.alf.index(q.upper()):] + self.alf2[:self.alf.index(q.upper())]
                    self.m += x[self.alf.index(n[i].upper())].lower()
            elif self.comboBox_3.currentText() == 'Шифр Хилла':
                self.alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
                self.alf = list(self.alf)
                e = 0
                e1 = 0
                n = self.line.text()
                for i in n:
                    if i == " ":
                        e1 = e
                        e = "33"
                    elif i.upper() in self.alf:
                        e1 = e
                        e = self.alf.index(i.upper())
                    if self.alf.index(i.upper()) % 2 == 1:
                        e1 = 1 * e1 + 3 * e
                        e = 2 * e1 + 7 * e
                        self.m += self.alf[e1 % 33]
                        self.m += self.alf[e % 33]
        self.slf4.show()

    def run4(self):
        if self.m == self.line1.text():
            self.label2.setText("Все правильно, молодец!")
        else:
            self.label2.setText(f"Это не правильный ответ, попробуй снова или посмотри правильный ответ.")
            self.slf7.show()
        self.label2.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
