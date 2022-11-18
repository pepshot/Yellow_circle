import sys
from random import randrange

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.go_paint = False

    def run(self):
        self.go_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.go_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
            self.go_paint = False

    def draw_circle(self, qp):
        qp.setBrush(QColor(254, 254, 34))
        a = randrange(50, 400)
        qp.drawEllipse(70, 150, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())