import arcade
from Models import *
from random import randint,random
import time

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

GAME_START = 7
INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
GAME_RUNNING_NORMAL = 2
GAME_RUNNING_CHALLENGE =3
GAME_OVER_NORMAL = 4
GAME_OVER_CHALLENGE = 5
GAME_WIN = 6

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()


class HoHoHoWindow(arcade.Window):
    LIST = ['images/bear.png','images/snowman.png','images/gift.png','images/gift.png','images/gift.png']

    def __init__(self, width, height):
        super().__init__(width, height)


        #self.background = arcade.set_background_color(arcade.color.BABY_BLUE)
        self.game_cover = arcade.load_texture('images/inst/inst1_1.png')
        self.game_instruction = [arcade.load_texture('images/inst/inst1_2.png'),arcade.load_texture('images/inst/inst2.png')]
        self.background = arcade.load_texture('images/bg.png')
        self.world = World(width, height)
        self.set_mouse_visible(True)
        self.current_state = GAME_START

        #self.snow_sprite = ModelSprite('images/snow.png',model = self.world.snow)
        self.player_sprite = ModelSprite('images/santa.png', model=self.world.player)
        self.block1_sprite = ModelSprite(HoHoHoWindow.LIST[randint(0,4)],model=self.world.block_1)
        self.block2_sprite = ModelSprite(HoHoHoWindow.LIST[randint(0,4)],model=self.world.block_2)
        self.block3_sprite = ModelSprite(HoHoHoWindow.LIST[randint(0,4)],model=self.world.block_3)
        self.block4_sprite = ModelSprite(HoHoHoWindow.LIST[randint(0,4)],model=self.world.block_4)
        self.block5_sprite = ModelSprite(HoHoHoWindow.LIST[randint(0,4)],model=self.world.block_5)
        self.bomb_1_sprite = ModelSprite('images/bomb.png', model = self.world.bomb_1)
        self.bomb_2_sprite = ModelSprite('images/bomb.png', model = self.world.bomb_2)
        self.heart_sprite = ModelSprite('images/life.png',model = self.world.heart)

    def draw_score(self,score,w,h,sc,d):
        x = str(score)
        for i in range(len(x)):
            num = arcade.Sprite(f'images/number/{int(x[i])}.png',scale= sc)
            num.set_position(w+(i+1)*d, self.height - h)
            num.draw()

    def draw_goal(self,goal,w,h,sc,d):
        goal = str(goal)
        for i in range(len(goal)):
            num = arcade.Sprite(f'images/number/{int(goal[i])}.png',scale=sc)
            num.set_position(w+(i+1)*d,self.height - h)
            num.draw()

    def draw_game_over_normal(self):
        x = arcade.load_texture('images/gameover_normal.png')
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT,x)
        self.draw_score(self.world.latest_score,500,335,0.8,45)
        self.draw_score(self.world.highest_score,500,425,0.8,45)
        

    def draw_game_over_challenge(self):
        x = arcade.load_texture('images/gameover_challenge.png')
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT,x)
        self.draw_goal(self.world.latest_goal,500,335,0.8,45)
        self.draw_score(self.world.latest_score,500,425,0.8,45)
        

    def draw_game_win(self):
        x = arcade.load_texture('images/gamewin.png')
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT,x)

    
    def draw_game(self) :
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.block1_sprite.draw()
        self.block2_sprite.draw()
        self.block3_sprite.draw()
        self.block4_sprite.draw()
        self.block5_sprite.draw()
        self.bomb_1_sprite.draw()
        self.bomb_2_sprite.draw()
        self.heart_sprite.draw()
        self.player_sprite.draw()
        
        w = self.width - 200
        for i in range(self.world.life):
            x = arcade.Sprite('images/life.png')
            x.set_position(w,550)
            x.draw()  
            w += 60

    def draw_game_normal(self) :
        self.draw_game()
        score = arcade.Sprite('images/number/score.png',scale = 0.7)
        score.set_position(100,550)
        score.draw()
        self.draw_score(self.world.score,180,52,0.5,30)
        

    def draw_game_challenge(self) :
        self.draw_game()
        mins = int(self.world.time.total_time) // 60
        minutes = f"{mins:02d}"
        sec = int(self.world.time.total_time) % 60
        seconds = f"{sec:02d}"
        for i in range(len(str(minutes))) :
            num1 = arcade.Sprite(f'images/number/{int(minutes[i])}.png',scale=0.5)
            num1.set_position(450+(30*i),550)
            num2 = arcade.Sprite(f'images/number/{int(seconds[i])}.png',scale=0.5)
            num2.set_position(530+(30*i),550)
            num1.draw()
            num2.draw()
        n = arcade.Sprite('images/number/n.png',scale = 0.6)
        n.set_position(507,550)
        n.draw()
        goal = arcade.Sprite('images/number/goal.png',scale = 0.6)
        goal.set_position(100,550)
        goal.draw()
        self.draw_goal(self.world.goal,160,52,0.4,30)
        score = arcade.Sprite('images/number/score.png',scale = 0.6)
        score.set_position(100,490)
        score.draw()
        self.draw_score(self.world.score,160,112,0.4,30)
        
        

    def draw_game_cover(self) :
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.game_cover) 
            

    def draw_instruction(self,n) :
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.game_instruction[n])
        

    def on_draw(self):
        arcade.start_render()
        if self.current_state == GAME_START:
            self.draw_game_cover()
        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.draw_instruction(0)
        if self.current_state == INSTRUCTIONS_PAGE_1:
            self.draw_instruction(1)
        if self.current_state == GAME_RUNNING_NORMAL:
            self.draw_game_normal()
        if self.current_state == GAME_RUNNING_CHALLENGE:
            self.draw_game_challenge()
        if self.current_state == GAME_OVER_NORMAL:
            self.draw_game_over_normal()
        if self.current_state == GAME_OVER_CHALLENGE:
            self.draw_game_over_challenge()
        if self.current_state == GAME_WIN:
            self.draw_game_win()
            
    def on_mouse_motion(self, x, y , dx, dy):
        self.world.on_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, button, modifiers):
        
        if self.current_state == GAME_START: 
            self.current_state = INSTRUCTIONS_PAGE_0
        elif self.current_state == INSTRUCTIONS_PAGE_0: 
            self.current_state = INSTRUCTIONS_PAGE_1
        elif self.current_state == INSTRUCTIONS_PAGE_1: 
            if 100<= x <= 400 and 100 < y < 500 :
                self.current_state = GAME_RUNNING_NORMAL
                self.world.time.status = True
            if 600 <= x <= 900 and 100 < y < 500 :
                self.current_state = GAME_RUNNING_CHALLENGE
                self.world.time.status = True         
        elif self.current_state == GAME_OVER_NORMAL :
            self.world.game_over_normal = False
            self.current_state = INSTRUCTIONS_PAGE_1
        elif self.current_state == GAME_OVER_CHALLENGE :
            self.world.game_over_challenge = False
            self.current_state = INSTRUCTIONS_PAGE_1
            self.world.time.status = True
        elif self.current_state == GAME_WIN :
            self.world.game_win = False
            self.current_state = GAME_RUNNING_CHALLENGE
            self.world.time.status = True
        
    def update(self, delta):
        if self.current_state == GAME_RUNNING_NORMAL :
            self.world.update_normal(delta)
            if self.world.game_over_normal == True :
                self.current_state = GAME_OVER_NORMAL
        if self.current_state == GAME_RUNNING_CHALLENGE :
            self.world.update_challenge(delta)
            if self.world.game_over_challenge == True :
                self.current_state = GAME_OVER_CHALLENGE
            if self.world.game_win == True :
                self.current_state = GAME_WIN
               

if __name__ == '__main__':
  window = HoHoHoWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
  arcade.run()