import arcade.key
from random import randint
import sys


class Player :
    def __init__(self,x,y) :
        self.x = x
        self.y = y


    def hit(self, other):
        return (self.x-50 < other.x < self.x+50) and ( 150 <= other.y <= 250 )

    def update(self,delta):
        pass

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
        self.y -= 5
        if self.y <= 10 :
            self.x = randint(x1,x2)
            self.y = randint(500,800)

class Enemies :
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
        self.y -= 5
        if self.y <= 10 :
            self.x = randint(x1,x2)
            self.y = randint(500,800)

class Bomb :
    def __init__(self,x1,x2) :
        self.x = randint(x1,x2)
        self.y = randint(1000,1200)
        self.status = False
        self.is_collected = False

    def is_hit(self,x1,x2) :
        self.x = randint(x1,x2)
        self.y = randint(1000,1200)
        self.status = False



    def update(self,delta,x1,x2) :
        self.y -= 5
        if self.y <= 10 :
            self.x = randint(x1,x2)
            self.y = randint(1000,1200)





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
        self.enemies_1 = Enemies(100,500)
        self.enemies_2 = Enemies(500,800)
        self.bomb_1 = Bomb(100,500)
        self.bomb_2 = Bomb(500,900)



        self.score = 0
        self.life = 3
        self.game_over = False

    def on_mouse_motion(self, x, y, dx, dy) :
        self.player.x = x
        self.player.y = 100


    def update(self,delta) :
        #self.player.update(delta)
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
        elif not self.enemies_1.status and self.player.hit(self.enemies_1) :
            self.enemies_1.is_hit(800,900)
            self.score -= 20
        elif not self.enemies_2.status and self.player.hit(self.enemies_2) :
            self.enemies_2.is_hit(800,900)
            self.score -= 20
        elif not self.bomb_1.status and self.player.hit(self.bomb_1) :
            self.bomb_1.is_hit(100,500)
            self.life -= 1
        elif not self.bomb_2.status and self.player.hit(self.bomb_2) :
            self.bomb_2.is_hit(500,900)
            self.life -= 1


        self.block_1.update(delta,100,250)
        self.block_2.update(delta,250,500)
        self.block_3.update(delta,500,650)
        self.block_4.update(delta,650,800)
        self.block_5.update(delta,800,900)
        self.enemies_1.update(delta,100,500)
        self.enemies_2.update(delta,500,800)
        self.bomb_1.update(delta,100,500)
        self.bomb_2.update(delta,500,900)
