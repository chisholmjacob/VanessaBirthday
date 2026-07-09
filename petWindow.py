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

        self.dragging = False
        self.drag_start = None

        self.favorite_spot = None

        screen = QApplication.primaryScreen()
        geometry = screen.geometry()

        screen_width = geometry.width()
        screen_height = geometry.height()

        pet_width = 200
        pet_height = 200
        taskbar_gap = 50

        x = screen_width - pet_width
        y = screen_height - pet_height - taskbar_gap

        self.move(x, y)

        print("Screen:", screen_width, screen_height)
        print("Starting pet at:", x, y)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = True
            self.drag_start = event.globalPosition()
    
    def mouseMoveEvent(self, event):
        if self.dragging:
            current_position = event.globalPosition()
            delta = current_position - self.drag_start

            self.move(self.pos() + delta.toPoint())

            self.drag_start = current_position
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = False
            self.drag_start = None
