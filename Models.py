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

    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

    def update(self,delta):
        self.move(self.direction)

class Fruits :
    def __init__(self,x1,x2) :
        self.x = randint(x1,x2)
        self.y = randint(600,900)


    def has_apple_at(self, r, c):
        return self.map[r][c] == 'A'

    def has_pineapple_at(self, r, c):
        return self.map[r][c] == 'P'

    def update(self,delta,x1,x2) :
        self.y -= 1
        if self.y == 50 :
            self.x = randint(x1,x2)
            self.y = randint(600,900)






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

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.player.direction = DIR_LEFT
        elif key == arcade.key.RIGHT:
            self.player.direction = DIR_RIGHT
        elif key == arcade.key.DOWN:
            self.player.direction = DIR_STILL


    def update(self,delta) :
        self.player.update(delta)
        self.block_1.update(delta,100,250)
        self.block_2.update(delta,250,500)
        self.block_3.update(delta,500,650)
        self.block_4.update(delta,650,800)
        self.block_5.update(delta,800,900)
