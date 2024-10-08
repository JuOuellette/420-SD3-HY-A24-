from csv import DictReader, DictWriter
from fileinput import filename


# changer pour pouvoir naviguer d'une ligne à l'autre
class Modele:
    def __init__(self):
        super().__init__()

    liste_de_sortie = []

    def read_file(self):
        with open("computer_games.csv", "rt", encoding= "utf-8") as csv_file:
            csv_dict_reader = DictReader(csv_file)
            for entry in csv_dict_reader:
                jeu = Jeux_Sorties()
                jeu.nom(entry["Name"])
                jeu.developer(entry["Developer"])
                jeu.editeur(entry["Producer"])
                jeu.genre(entry["Genre"])
                jeu.date(entry["Release Date"])
                jeu.operation(entry["Operating System"])
                self.liste_de_sortie.append(jeu)


    def mod_csv(self):
        pass


    def enregistrer_csv(self):
        liste_entrees_csv = []
        for jeu in self.liste_de_sortie:
            entree =  {"Name": jeu.nom,"Developer": jeu.developer,"Producer": jeu.editeur,"Genre": jeu.editeur,"Operating System":jeu.operation,"Date Released": jeu.date}
            liste_entrees_csv.append(entree)
        with open("computer_games.csv", "w", encoding="utf-8") as csv_writer:
            csv_writer = DictWriter(csv_writer, fieldnames  =) #wriiiiiiiiiiteeeee


    def statistiques(self):
        pass


class Jeux_Sorties:

    def __init__(self):
        pass

    @property
    def nom(self):
        return self.nom()

    @nom.setter
    def nom(self, nom):
        self.nom = nom

    @property
    def developer(self):
        return self.developer

    @developer.setter
    def developer(self, developer):
        self.developer = developer

    @property
    def editeur(self):
        return self.editeur

    @editeur.setter
    def editeur(self, editeur):
        self.editeur = editeur

    #faire pour genre, date et operations

    @property
    def genre(self):
        return self.genre

    @genre.setter
    def genre(self, genre):
        self.genre = genre

    @property
    def date(self):
        return self.date

    @date.setter
    def genre(self, date):
        self.date = date

    @property
    def operation(self):
        return self.operation

    @operation.setter
    def operation(self, operation):
        self.operation = operation

