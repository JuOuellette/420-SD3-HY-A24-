from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog


class fenetre(QMainWindow):
   def __init__(self):
        super().__init__()


        self.setWindow_Title("qfiledialog")
        self.dialogue.setOption(QFileDialog.ShowDirsOnly)
        self.
