from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QLabel, QWidget, QPushButton,
                               QGridLayout, QVBoxLayout)


class GestionVue(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controlleur = Controlleur()  # missing self.modele

        widget_central = QWidget()
        disposition_grid = QGridLayout()
        widget_central.setLayout(disposition_grid)

        dispo_vertical_gauche = QVBoxLayout()

        humain_label = QLabel("Humain")
        roche_bouton = QPushButton("Roche")
        papier_bouton = QPushButton("Papier")
        ciseau_bouton = QPushButton("Ciseau")

        dispo_vertical_gauche.addWidget(humain_label)
        dispo_vertical_gauche.addWidget(roche_bouton)
        dispo_vertical_gauche.addWidget(papier_bouton)
        dispo_vertical_gauche.addWidget(ciseau_bouton)

        disposition_grid.addLayout(dispo_vertical_gauche, 0, 0)

        dispo_scores = QHBoxLayout()
        dispo_vertical_milieu = QVBoxLayout()
        self.score_humain = QLabel("0")
        # TODO
        self.score_cpu = QLabel("1")
        dispo_scores.addWidget(self.score_humain)
        dispo_scores.addWidget(self.score_cpu)
        choix_humain = QLabel("Choix Humain")
        choix_cpu = QLabel("Choix CPU")
        dispo_vertical_milieu.addLayout(dispo_scores)
        dispo_vertical_milieu.addWidget(choix_humain)
        dispo_vertical_milieu.addWidget(choix_cpu)
        disposition_grid.addLayout(dispo_vertical_milieu, 0, 1)

        disposition_droite = QVBoxLayout()
        bot = QLabel("CPU")
        roche_bouton_bot = QPushButton("Roche")
        roche_bouton_bot.setEnabled(False)
        papier_bouton_bot = QPushButton("Papier")
        papier_bouton_bot.setEnabled(False)
        ciseau_bouton_bot = QPushButton("Ciseau")
        ciseau_bouton_bot.setEnabled(False)

        disposition_droite.addWidget(bot)
        disposition_droite.addWidget(roche_bouton_bot)
        disposition_droite.addWidget(papier_bouton_bot)
        disposition_droite.addWidget(ciseau_bouton_bot)

        disposition_grid.addLayout(disposition_droite, 0, 2)
        self.setCentralWidget(widget_central)


class Controlleur:
    def __init__(self):
        super().__init__()

    def scores(self):
        pass


app = QApplication()
fenetre = GestionVue()
fenetre.show()
app.exec()
