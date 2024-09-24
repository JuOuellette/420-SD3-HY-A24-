import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QToolBar, QToolButton, QLabel, QStatusBar, QPushButton, QApplication
from PySide6.QtGui import QAction, QKeySequence, QIcon

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        barre_menus = self.menuBar()
        self.creer_menus(barre_menus)

    def creer_menus(self, barre_menu):
        menu_fichier = barre_menu.addMenu("image")
        action_jouer = QAction(text="open", parent=self)
        action_jouer.setStatusTip("power")
        action_jouer.triggered.connect(action_jouer.setIcon(QIcon("jouer.png")))
        menu_fichier.addAction(action_jouer)





app = QApplication(sys.argv)
f = Window()
f.show()
app.exec()