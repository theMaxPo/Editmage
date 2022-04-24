from Canvas import Canvas
from Utils.Constants import Position

class Window(Canvas):
    def __init__(self, xy = (0, 0), size = (1, 1), color = (255, 255, 255, 255), blur = 0, margin = (0, 0, 0, 0), padding = (0, 0, 0, 0), position = (Position.CENTER, Position.CENTER), auto_update = True):
        super().__init__(xy, size, color, blur, margin, padding, position, auto_update)

