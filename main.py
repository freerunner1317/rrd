import MySQLdb
import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

def finish():
    window.photoLabel.clear()
    window.first_answer.setEnabled(False)
    window.second_answer.setEnabled(False)
    window.third_answer.setEnabled(False)
    window.manage_but.setEnabled(False)

def checkAnswer(numberButton, objectsButton):
    global currentQuestion
    global numberRightAns
    global lenRows
    right_ans = rows[currentQuestion]['right_answer']
    window.explain_lable.setText(rows[currentQuestion]['explain'])
    window.manage_but.setEnabled(True)
    window.first_answer.setEnabled(False)
    window.second_answer.setEnabled(False)
    window.third_answer.setEnabled(False)

    if (right_ans == numberButton):
        objectsButton[numberButton].setStyleSheet("background-color: green; color: white;")
    else:
        objectsButton[numberButton].setStyleSheet("background-color: red; color: white;")
        objectsButton[right_ans].setStyleSheet("background-color: green; color: white;")
    print(lenRows)
    print(currentQuestion)
    if (currentQuestion == lenRows):
        finish()
    else:
        currentQuestion += 1

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
    window.manage_but.clicked.connect(getDatabase)

##### в начале сделать их некликабельными
    window.first_answer.setEnabled(False)
    window.second_answer.setEnabled(False)
    window.third_answer.setEnabled(False)
    window.manage_but.setText("Начать тестирование")


    window.show()
    cursor.close()
    sys.exit(app.exec_())