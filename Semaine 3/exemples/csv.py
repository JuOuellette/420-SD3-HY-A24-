from PySide6.QtWidgets import QApplication, QMainWindow
import csv

class ReadText(QMainWindow):
    def __init__(self):
        super().__init__()
        with open("times.csv", "r") as csv_file:
            csv.dict_reader = csv.DictReader(csv_file)
