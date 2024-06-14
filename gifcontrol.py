from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QMovie

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.movie = QMovie("spinner.gif")  # Gif dosyanızın tam yolu veya adı
        self.label = QLabel(self)
        self.label.setGeometry(100, 100, 300, 300)
        self.label.setMovie(self.movie)

        self.movie.start()

if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec_()