import arcade.key
from random import randint
import time

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


class Gifts :
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

class Heart :
    def __init__(self,x1,x2) :
        self.x = randint(x1,x2)
        self.y = randint(3000,5000)
        self.status = False
        self.is_collected = False

    def is_hit(self,x1,x2) :
        self.x = randint(x1,x2)
        self.y = randint(3000,5000)
        self.status = False


    def update(self,delta,x1,x2,y) :
        self.y -= y
        if self.y <= 10 :
            self.x = randint(x1,x2)
            self.y = randint(1000,1200)

class Time :
    def __init__(self,time) :
        self.total_time = time
        self.status = None
        
    def update(self, delta_time):
        if self.status == True :
            self.total_time -= delta_time
            if self.total_time <= 0 :
                self.status = False
        

class World :
    TIME = 30

    def __init__(self,width,height) :

        self.width = width
        self.height = height
        self.score = 0
        self.latest_score = 0
        self.score_list = []
        self.highest_score = 0
        self.life = 3
        self.game_over = False
        self.game_win = False
        self.goal = 300

        self.int_time = 30
        self.time = Time(30)
        self.snow = Snow()
        self.player = Player( 500, 150)
        self.block_1 = Gifts(100,250)
        self.block_2 = Gifts(250,500)
        self.block_3 = Gifts(500,650)
        self.block_4 = Gifts(650,800)
        self.block_5 = Gifts(800,900)
        self.bomb_1 = Bomb(100,500)
        self.bomb_2 = Bomb(500,900)
        self.heart = Heart(200,800)
        

    def on_mouse_motion(self, x, y, dx, dy) :
        self.player.x = x
        self.player.y = 100

    def set_up(self) :
        self.score = 0
        self.life = 3
        self.time = Time(30)

    def level_up(self) :
        self.goal += 200
        self.int_time += 15
        self.time = Time(self.int_time)

        

    def game_over(self) :
        if self.time.status == False :
            self.score_list.append(self.score)
            self.latest_score = self.score
            self.highest_score = max(self.score_list)
            self.game_over =True
            self.set_up()
        if self.life == 0 :
            self.score_list.append(self.score)
            self.latest_score = self.score
            self.highest_score = max(self.score_list)
            self.game_over =True
            self.set_up()
    
    def game_win(self) :
        if (self.time.status == False) or (self.score >= self.goal) :
            self.score_list.append(self.score)
            self.latest_score = self.score
            self.highest_score = max(self.score_list)
            self.game_win = True
            self.set_up()
            self.level_up()
            
                


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
        elif not self.bomb_1.status and self.player.hit(self.bomb_1) :
            self.bomb_1.is_hit(100,500)
            self.life -= 1
        elif not self.bomb_2.status and self.player.hit(self.bomb_2) :
            self.bomb_2.is_hit(500,900)
            self.life -= 1
        elif not self.heart.status and self.player.hit(self.heart) :
            self.heart.is_hit(200,800)
            if self.life < 3 :
                self.life += 1
            self.life += 0

    def up_speed(self,delta,y) :
        self.block_1.update(delta,100,250,y)
        self.block_2.update(delta,250,500,y)
        self.block_3.update(delta,500,650,y)
        self.block_4.update(delta,650,800,y)
        self.block_5.update(delta,800,900,y)
        self.bomb_1.update(delta,100,500,y)
        self.bomb_2.update(delta,500,900,y)
        self.heart.update(delta,200,800,y)

    def update(self,delta) :
        self.snow.update(delta)
        self.time.update(delta)
        World.check_hit(self)
        World.game_over(self)
        World.game_win(self)
        if self.score >= 100 :
            World.up_speed(self,delta,5.05)
        if self.score >= 300 :
            World.up_speed(self,delta,5.1)
        if self.score >= 500 :
            World.up_speed(self,delta,5.15)
        if self.score >= 700 :
            World.up_speed(self,delta,5.2)
        if self.score >= 900 :
            World.up_speed(self,delta,5.25)
        else:
            World.up_speed(self,delta,5)

        
            
        
        
        
