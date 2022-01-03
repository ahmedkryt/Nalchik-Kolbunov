import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 600)

        self.draw = False
        self.setMouseTracking(True)

        self.btn = QPushButton('Кнопка', self)
        self.btn.resize(800, 80)
        self.btn.move(0, 520)
        self.btn.clicked.connect(self.run)

    def paintEvent(self, event):
        if not self.draw:
            return
        qp = QPainter()
        qp.begin(self)
        self.draw_someth(qp)
        qp.end()

    def draw_someth(self, qp):
        qp.setBrush(QColor(255, 204, 0))  # цвет Яндекса))
        size = randint(20, 250)
        qp.drawEllipse(self.x - size // 2, self.y - size // 2, size, size)

    def run(self):
        self.x, self.y = 380, 275
        self.draw = True
        self.repaint()
        qp = QPainter()
        qp.begin(self)
        self.draw_someth(qp)
        qp.end()
        self.draw = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())