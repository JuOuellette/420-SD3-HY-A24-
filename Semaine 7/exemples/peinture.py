from PySide6.QtGui import QPainter, QPixmap, QColor, QPen, QBrush
from PySide6.QtCore import QSize, Qt, QPoint
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class MonPeintre(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("peinture")

        self.canevas = QPixmap(QSize(500,400))

        self.etiquette_central = QLabel()
        self.etiquette_central.setPixmap(self.canevas)
        self.setCentralWidget(self.etiquette_central)
        self.dessiner()


    def dessiner(self):
        canevas = self.canevas
        #canevas.fill(QColorConstants.DarkGreen)
        canevas.fill(QColor(87, 130, 99 ))
        painter = QPainter(canevas)

        crayon = QPen()
        crayon.setColor(QColor(234, 190, 235))
        crayon.setCapStyle(Qt.PenCapStyle.RoundCap)
        crayon.setWidth(15)
        pinceau = QBrush()
        pinceau.setStyle(Qt.BrushStyle.BDiagPattern)
        painter.setPen(crayon)

        painter.drawText(QPoint(125,125), "YOU")
        painter.drawEllipse(QPoint(28,150), 100, 50)
        painter.translate(25,20)
        painter.rotate(95) # degrées ici

        painter.end()

        self.etiquette_central.setPixmap(canevas)


app = QApplication()
window= MonPeintre()
window.show()
app.exec()