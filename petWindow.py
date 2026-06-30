from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class PetWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.petLabel = QLabel()
        petImage = QPixmap("assets/pet.png")
        petImage = petImage.scaled(100, 100)
        self.petLabel.setPixmap(petImage)
        layout = QVBoxLayout()
        layout.addWidget(self.petLabel)
        self.setLayout(layout)


        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.resize(200, 200)
        self.show()