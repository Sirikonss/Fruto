import arcade.key
from random import randint
import sys

DIR_STILL = 0
DIR_LEFT = 1
DIR_RIGHT = 2

DIR_OFFSETS = { DIR_STILL: (0,0),
                DIR_RIGHT: (1,0),
                DIR_LEFT: (-1,0) }

MOVEMENT_SPEED = 5

class Player :
    def __init__(self,x,y) :
        self.x = x
        self.y = y
        self.direction = DIR_STILL

    def move(self,direction):
        self.x += DIR_OFFSETS[direction][0] * MOVEMENT_SPEED
        self.y += DIR_OFFSETS[direction][1] * MOVEMENT_SPEED

    def hit(self, other):
        return (self.x-50 < other.x < self.x+50) and ( 200 <= other.y <= 300 )

    def update(self,delta):
        self.move(self.direction)

class Fruits :
    def __init__(self,x1,x2) :
        self.x = randint(x1,x2)
        self.y = randint(600,900)
        self.status = False
        self.is_collected = False

    def is_hit(self,x1,x2) :
        self.x = randint(x1,x2)
        self.y = randint(600,800)
        self.status = False


    def update(self,delta,x1,x2) :
        self.y -= 3
        if self.y <= 10 :
            self.x = randint(x1,x2)
            self.y = randint(500,800)




class World :
    def __init__(self,width,height) :
        self.width = width
        self.height = height
        self.player = Player( 500, 150)
        self.block_1 = Fruits(100,250)
        self.block_2 = Fruits(250,500)
        self.block_3 = Fruits(500,650)
        self.block_4 = Fruits(650,800)
        self.block_5 = Fruits(800,900)
        self.score = 0


    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.player.direction = DIR_LEFT
        elif key == arcade.key.RIGHT:
            self.player.direction = DIR_RIGHT
        elif key == arcade.key.DOWN:
            self.player.direction = DIR_STILL


    def update(self,delta) :
        self.player.update(delta)
        if not self.block_1.status and self.player.hit(self.block_1) :
            self.block_1.is_hit(100,250)
            self.score += 10
        elif not self.block_2.status and self.player.hit(self.block_2) :
            self.block_2.is_hit(250,500)
            self.score += 10
        elif not self.block_3.status and self.player.hit(self.block_3) :
            self.block_3.is_hit(500,650)
            self.score += 10
        elif not self.block_4.status and self.player.hit(self.block_4) :
            self.block_4.is_hit(650,800)
            self.score += 10
        elif not self.block_5.status and self.player.hit(self.block_5) :
            self.block_5.is_hit(800,900)
            self.score += 10
        self.block_1.update(delta,100,250)
        self.block_2.update(delta,250,500)
        self.block_3.update(delta,500,650)
        self.block_4.update(delta,650,800)
        self.block_5.update(delta,800,900)
