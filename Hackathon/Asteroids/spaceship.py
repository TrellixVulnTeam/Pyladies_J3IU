import pyglet

class Spaceship():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed_x = 0
        self.speed_y = 0
        self.rotation = 0

        image =  pyglet.image.load('./images/PNG/playerShip1_blue.png')
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        self.sprite = pyglet.sprite.Sprite(image)
    
    def draw(self):
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.draw()
    
    def tick(self, time):
        print('Tick tack.')