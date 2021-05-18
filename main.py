import MySQLdb
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


def initDataBase():
    conn = MySQLdb.connect('localhost', 'username', 'password', 'table_name')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM table_name")

class MainWindow(QMainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      uic.loadUi('gui.ui', self)

      pixmap = QPixmap("1.jpg")
      pixmap = pixmap.scaledToWidth(780)
      print(pixmap.width())

      self.photoLabel.setPixmap(pixmap)
      self.setWindowTitle('PyQt5 Image Viewer')




if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта самого приложения
    window = MainWindow()



    window.show()
    sys.exit(app.exec_())