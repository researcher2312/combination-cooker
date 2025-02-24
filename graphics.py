import pyxel as px


def display_image(x: int, y: int, image):
    px.blt(x, y, 0, image[0], image[1], 16, 16, image[2])


class Block:
    def __init__(self, image, x=0, y=0):
        self.x = x
        self.y = y
        self.image = image

    def display(self):
        display_image(self.x, self.y, self.image)

    def set_coordinates(self, coords):
        self.x, self.y = coords

