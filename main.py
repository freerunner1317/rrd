import MySQLdb
import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

# функция, которая вызывается при нажатии кнопки "показать результат"
def finish():
    window.manage_but.clicked.disconnect()
    window.manage_but.clicked.connect(getDatabase)
    global historyAns
    global currentQuestion
    window.photoLabel.setVisible(False)
    window.question_label.setVisible(False)
    window.first_answer.setVisible(False)
    window.second_answer.setVisible(False)
    window.third_answer.setVisible(False)
    window.manage_but.setVisible(False)
    window.explain_lable.setVisible(False)
    window.onceAgain.setVisible(True)

    if (historyAns == (lenRows + 1)):
        window.finishLabel.setText("Тест пройден")
    else:
        window.finishLabel.setText("Тест провален")
        #window.finishLabel.setText("Количество правильных ответов = " + str(round(historyAns/(lenRows + 1) * 100)) + "%")
# функция, которая вызывается при нажатии "еще раз" для отображения нужных элементов
def startAgain():
    global currentQuestion
    global historyAns
    window.finishLabel.clear()
    window.photoLabel.setVisible(True)
    window.question_label.setVisible(True)
    window.first_answer.setVisible(True)
    window.second_answer.setVisible(True)
    window.third_answer.setVisible(True)
    window.manage_but.setVisible(True)
    window.explain_lable.setVisible(True)
    window.onceAgain.setVisible(False)

    currentQuestion = 0
    historyAns = 0
    getDatabase()
# функция, которая вызвается при нажатии на любого вариант ответа для его проверки и занесения ответа в массив
def checkAnswer(numberButton, objectsButton):
    global currentQuestion
    global numberRightAns
    global lenRows
    global historyAns
    right_ans = rows[currentQuestion]['right_answer']
    window.explain_lable.setText(rows[currentQuestion]['explain'])
    window.manage_but.setEnabled(True)
    window.first_answer.setEnabled(False)
    window.second_answer.setEnabled(False)
    window.third_answer.setEnabled(False)

    if (right_ans == numberButton):
        objectsButton[numberButton].setStyleSheet("background-color: green; color: white;")
        historyAns += 1
    else:
        objectsButton[numberButton].setStyleSheet("background-color: red; color: white;")
        objectsButton[right_ans].setStyleSheet("background-color: green; color: white;")

    if (currentQuestion == lenRows):
        window.manage_but.setText("Показать результат")
        window.manage_but.clicked.connect(finish)
    else:
        currentQuestion += 1
# функция, которая вызывается при нажатии кнопки "далее" для получения следующего вопроса из базы данных
def getDatabase():
    global currentQuestion
    window.first_answer.setEnabled(True)
    window.second_answer.setEnabled(True)
    window.third_answer.setEnabled(True)
    window.first_answer.setStyleSheet("")
    window.second_answer.setStyleSheet("")
    window.third_answer.setStyleSheet("")
    window.explain_lable.clear()
    window.first_answer.setText(rows[currentQuestion]['first_answer'])
    window.second_answer.setText(rows[currentQuestion]['second_answer'])
    window.third_answer.setText(rows[currentQuestion]['third_answer'])
    window.question_label.setText(rows[currentQuestion]['question'])
    window.manage_but.setText("Далее")
    window.manage_but.setEnabled(False)

    pixmap = QPixmap("pictures/" + rows[currentQuestion]['picture_name'])
    pixmap = pixmap.scaledToWidth(780)
    window.photoLabel.setPixmap(pixmap)


class MainWindow(QMainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      uic.loadUi('gui.ui', self)
      self.setWindowTitle('Проверка знаний ПДД')

if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта самого приложения
    app.setWindowIcon(QtGui.QIcon('pictures/icon.png'))
    window = MainWindow()

    global currentQuestion
    global lenRows
    global historyAns
    historyAns = 0
    currentQuestion = 0

    conn = MySQLdb.connect('localhost', 'root', 'root', 'pdd', charset='utf8')
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM pdd.questions;")
    rows = cursor.fetchall()
    lenRows = len(rows) - 1

    objectsButton = [0] * 4
    objectsButton[1] = window.first_answer
    objectsButton[2] = window.second_answer
    objectsButton[3] = window.third_answer

    window.first_answer.clicked.connect(lambda: checkAnswer(1, objectsButton))
    window.second_answer.clicked.connect(lambda: checkAnswer(2, objectsButton))
    window.third_answer.clicked.connect(lambda: checkAnswer(3, objectsButton))
    window.onceAgain.clicked.connect(startAgain)
    window.manage_but.clicked.connect(getDatabase)

# в начале сделать кнопки некликабельными
    window.onceAgain.setVisible(False)
    window.first_answer.setEnabled(False)
    window.second_answer.setEnabled(False)
    window.third_answer.setEnabled(False)
    window.manage_but.setText("Начать тестирование")
# показать настроенное окно GUI
    window.show()
# завершение работы программы
    cursor.close()
    sys.exit(app.exec_())