from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtCore import Qt, QTimer

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
        ############# size of window #########################################################################################################################
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.resize(200, 200)
        self.show()
        ############# conditions to see if it is clicked on or not ###########################################################################################
        self.dragging = False
        self.drag_start = None

        self.favorite_spot = None
        ############# this is to see the screen height and width then it finds the x and y position and spawns pet at position ###############################
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
        self.favorite_spot = self.pos()

        print("Screen:", screen_width, screen_height)
        print("Starting pet at:", x, y)
        ############# walk back to spot ######################################################################################################################
        self.walk_timer = QTimer()
        self.walk_timer.timeout.connect(self.walk_to_favorite_spot)


        ##################### functions ######################################################################################################################
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
            self.walk_timer.start(16)
        elif event.button() == Qt.MouseButton.RightButton:
            self.favorite_spot = self.pos()
            print("New favorite spot:", self.favorite_spot)

    def walk_to_favorite_spot(self):
        current = self.pos()
        target = self.favorite_spot

        dx = target.x() - current.x()
        dy = target.y() - current.y()

        step = 5

        if abs(dx) <= step and abs(dy) <= step:
            self.move(target)
            self.walk_timer.stop()
            return
        
        new_x = current.x()
        new_y = current.y()

        if dx > 0:
            new_x += step
        elif dx < 0:
            new_x -= step
        
        if dy > 0:
            new_y += step
        elif dy < 0:
            new_y -= step
        
        self.move(new_x, new_y)
