from PySide6.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QWidget, QApplication, QPushButton
from computer_model import Jeux_Sorties, Modele
import csv

class Vue(QMainWindow):
    def __init__(self):
        super().__init__()

        self.modele = Modele()
        self.controleur = Gestion_Controleur(self.modele)

        bouton = QPushButton("test")
        bouton.clicked.connect(self.controleur.bouton_enregistrer_click())

        self.SetWindowTitle = "Computer Games"
        self.disposition = QHBoxLayout()
        widget_central = QWidget()
        widget_central.setLayout(self.disposition)
        self.setCentralWidget(widget_central)

        self.name = self.creer_libellés("Name")
        self.developer = self.creer_libellés("Developer")
        self.producer = self.creer_libellés("Producer")
        self.genre = self.creer_libellés("Genre")
        self.operation = self.creer_libellés("Operating System")
        self.date = self.creer_libellés("Date released")

    def creer_libellés(self, nom_propriete: str):
        disposition_libelle = QHBoxLayout()
        libelle_titre = QLabel(nom_propriete + ":")
        libelle_valeur = QLabel("")
        disposition_libelle.addWidget(libelle_titre)
        disposition_libelle.addWidget(libelle_valeur)
        self.disposition.addLayout(disposition_libelle)
        return libelle_valeur

    def creer_widget_valeur(self):
        pass

class Gestion_Controleur():
    def __init__(self, modele: Modele):
        pass

    def bouton_enregistrer_click(self):
        pass




app = QApplication()
vue = Vue()
vue.show()
app.exec()
