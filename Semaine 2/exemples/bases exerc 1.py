import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QStatusBar, QPushButton, QVBoxLayout, QWidget, QDialog
from PySide6.QtGui import QAction, QKeySequence

class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()

        #titre
        self.setWindowTitle("Mon application")

        #statut
        self.barre_statut = QStatusBar(self)
        self.barre_statut.setStatusTip("statut")
        self.setStatusBar(self.barre_statut)

        #menus
        barre_menus = self.menuBar()
        self.creer_menu(barre_menus)

        #bouton dans barre outils
        action_test = QPushButton("bouton rouge")
        action_test.pressed.connect(self.action_executee)
        #outils
        barre_outils = QToolBar("barre_d'outils")
        barre_outils.setIconSize(QSize(16, 16))
        barre_outils.addWidget(action_test)
        self.addToolBar(barre_outils)

        #bouton du layout
        self.bouton_surprise = QPushButton("YOU DID NOT SEE ME COMING")
        self.bouton_surprise.clicked.connect(self.call_dialog)

        #ajout du layout
        layout = QVBoxLayout()
        layout.addWidget(self.bouton_surprise)
        container = QWidget()
        container.setLayout(layout)
        #ceci sera au central
        self.setCentralWidget(container)
        self.show()



    def creer_menu(self, a_menu):
        menu_fichier = a_menu.addMenu("M&enu1")
        action_conseil = QAction(text ="n'oublie pas de respirer", parent= self)
        action_conseil.setStatusTip("cliquez ici pour un conseil")
        menu_fichier.addAction(action_conseil)

        menu_second = a_menu.addMenu("&Menu2")
        action_advice = QAction(text= "drink water", parent=self)
        action_advice.setStatusTip("ose cliquer pour un conseil")
        menu_second.addAction(action_advice)

    def action_executee(self):
        print("click!!!")
        self.barre_statut.setStatusTip("click!!!!!!!")

    def call_dialog(self):
        self.dialogue = QDialog()
        self.dialogue.setWindowTitle("ceci est un dialogue")
        self.bouton = QPushButton("close?")
        self.bouton.clicked.connect(self.close_dialog)
        disposition = QVBoxLayout()
        disposition.addWidget(self.bouton)
        self.dialogue.setLayout(disposition)
        self.dialogue.exec()

        #pour fermer le dialog


    def close_dialog(self):
        print("Close")
        self.dialogue.close() #ferme le dialogue
        self.close() #ferme la fenetre
        # action_quitter = QAction(text= "quitter", parent=self)
        # action_quitter.triggered.connect(self.close) #close le dialogue??
        # action_quitter.setShortcut(QKeySequence("Ctrl+Q"))



app = QApplication(sys.argv)
f = Fenetre()
f.show()
app.exec()