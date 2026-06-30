from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6.QtCore import Qt
from petWindow import PetWindow

app = QApplication(sys.argv)

pet = PetWindow()

pet.show()


sys.exit(app.exec())