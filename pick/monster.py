from pico2d import*
import math

class Spirit:
    image = None
    def __init__(self):
        self.x = 880
        self.y = 80
        self.speed = 0
        if Spirit.image == None:
            Spirit.image = load_image('spirit/small2.png')

    def draw(self):
        self.image.clip_draw(0, 0, 317, 292, self.x, self.y, 100, 80)
        pass

    def update(self):
        self.x -= 8
        self.y = 10 * math.sin(self.x/15) + 80
        pass


class Spirit2:
    image = None
    def __init__(self):
        self.x = 1900
        self.y = 80
        self.speed = 0
        if Spirit2.image == None:
            Spirit2.image = load_image('spirit/small2.png')

    def draw(self):
        self.image.clip_draw(0, 0, 317, 292, self.x, self.y, 100, 80)
        pass

    def update(self):
        self.x -= 8
        self.y = 10 * math.sin(self.x/15) + 80
        pass




class QKrzbals:
    image = None
    def __init__(self):
        self.x = 1600
        self.y = 80
        self.speed = 0
        # self.image = None
        # self.image = load_image('spirit/small2.png')
        if QKrzbals.image == None:
            QKrzbals.image = load_image('spirit/4.png')

    def draw(self):
        self.image.clip_draw(0, 0, 297, 340, self.x, self.y+25, 200, 150)
        pass

    def update(self):
        self.x -= 8
        self.y = 10 * math.sin(self.x/20) + 80
        pass
class Dust:
    image = None
    def __init__(self):
        self.x = 1000
        self.y = 80
        self.speed = 0
        # self.image = None
        # self.image = load_image('spirit/small2.png')
        if Dust.image == None:
            Dust.image = load_image('spirit/3.png')

    def draw(self):
        self.image.clip_draw(0, 0, 158, 204, self.x, self.y+150, 150, 150)
        pass

    def update(self):
        self.x -= 3
        self.y = 150 * math.sin(self.x/10) + 200
        pass

class Triangle:
    image = None
    def __init__(self):
        self.x = 3000
        self.y = 80
        self.speed = 0
        if Triangle.image == None:
            Triangle.image = load_image('spirit/2.png')

    def draw(self):
        self.image.clip_draw(0, 0, 223, 173, self.x, self.y, 300, 280)
        pass

    def update(self):
        self.x -= 8
        self.y = 10 * math.sin(self.x/15) + 150
        pass