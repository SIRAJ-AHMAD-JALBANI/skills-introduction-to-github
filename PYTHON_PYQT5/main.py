import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(400, 150, 500, 500)
        self.setWindowIcon(QIcon('yt.png'))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 400, 100)
        label.setStyleSheet("color: #292929;"
                            "background-color:blue;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        label.setAlignment(Qt.HAlignRight)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Youtube")
        self.setGeometry(400,150,500,500)
        self.setWindowIcon()