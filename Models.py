import arcade.key
from random import randint
import sys

class Snow :
    def __init__(self) :
        self.x = 500
        self.y = 800

    def update(self,delta) :
        self.y -= 2
    


class Player :
    def __init__(self,x,y) :
        self.x = x
        self.y = y


    def hit(self, other):
        return (self.x-50 < other.x < self.x+50) and ( 50 <= other.y <= 200 )

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
        self.y = randint(700,900)
        self.status = False


    def update(self,delta,x1,x2,y) :
        self.y -= y
        if self.y <= 10 :
            self.x = randint(x1,x2)
            self.y = randint(600,900)
        

        

class Enemies :
    def __init__(self,x1,x2) :
        self.x = randint(x1,x2)
        self.y = randint(600,900)
        self.status = False
        self.is_collected = False

    def is_hit(self,x1,x2) :
        self.x = randint(x1,x2)
        self.y = randint(700,800)
        self.status = False


    def update(self,delta,x1,x2,y) :
        self.y -= y
        if self.y <= 10 :
            self.x = randint(x1,x2)
            self.y = randint(600,800)

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



    def update(self,delta,x1,x2,y) :
        self.y -= y
        if self.y <= 10 :
            self.x = randint(x1,x2)
            self.y = randint(1000,1200)





class World :
    def __init__(self,width,height) :

        self.width = width
        self.height = height
        self.score = 0
        self.latest_score = 0
        self.score_list = []
        self.highest_score = 0
        self.life = 3
        self.game_over = False

        self.snow = Snow()
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

    def on_mouse_motion(self, x, y, dx, dy) :
        self.player.x = x
        self.player.y = 100


    def game_over(self) :
        if self.life == 0 :
            self.score_list.append(self.score)
            self.latest_score = self.score
            self.highest_score = max(self.score_list)
            self.game_over =True
            self.score = 0
            self.life = 3

    def check_hit(self) :

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
            if self.score >= 20 :
                self.score -= 20
        elif not self.enemies_2.status and self.player.hit(self.enemies_2) :
            self.enemies_2.is_hit(800,900)
            if self.score >= 20 :
                self.score -= 20
        elif not self.bomb_1.status and self.player.hit(self.bomb_1) :
            self.bomb_1.is_hit(100,500)
            self.life -= 1
        elif not self.bomb_2.status and self.player.hit(self.bomb_2) :
            self.bomb_2.is_hit(500,900)
            self.life -= 1

    def up_speed(self,delta,y) :
        self.block_1.update(delta,100,250,y)
        self.block_2.update(delta,250,500,y)
        self.block_3.update(delta,500,650,y)
        self.block_4.update(delta,650,800,y)
        self.block_5.update(delta,800,900,y)
        self.enemies_1.update(delta,100,500,y)
        self.enemies_2.update(delta,500,800,y)
        self.bomb_1.update(delta,100,500,y)
        self.bomb_2.update(delta,500,900,y)

    def update(self,delta) :
        #self.player.update(delta)
        self.snow.update(delta)
        World.check_hit(self)
        World.game_over(self)
        if self.score >= 100 :
            World.up_speed(self,delta,5.2)
        if self.score >= 300 :
            World.up_speed(self,delta,5.4)
        if self.score >= 500 :
            World.up_speed(self,delta,5.6)
        if self.score >= 700 :
            World.up_speed(self,delta,5.8)
        if self.score >= 900 :
            World.up_speed(self,delta,6)
        else:
            World.up_speed(self,delta,5)

        
            
        
        
        
