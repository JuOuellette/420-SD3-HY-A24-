from PySide6.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QWidget

import csv

class Modele:
    def __init__(self):
        super().__init__()

    def read_file(self):
        with open("computer_games.csv", "r") as csv_file:
            csv_dict_reader = csv.DictReader(csv_file)
            for i in csv_dict_reader:
                print(f'{i["Name"]} , {i["Developer"]} , {i["Producer"]} , {i["Genre"]}) , {i["Operating System"]} , {i["Date Released"]})

        #changer pour pouvoir naviguer d'une ligne à l'autre

class Vue(QMainWindow):
    def __init__(self):
        super().__init__()

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

