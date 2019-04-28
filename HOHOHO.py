import arcade
from Models import Player,World
from random import randint,random
import time

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

INSTRUCTIONS_PAGE_0 = 0
GAME_RUNNING = 1
GAME_OVER = 2

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
        self.game_cover = arcade.load_texture('images/inst1.png')
        self.background = arcade.load_texture('images/bg.png')
        self.world = World(width, height)
        self.set_mouse_visible(False)
        self.current_state = INSTRUCTIONS_PAGE_0

        self.snow_sprite = ModelSprite('images/snow.png',model = self.world.snow)
        self.player_sprite = ModelSprite('images/santa.png', model=self.world.player)
        self.block1_sprite = ModelSprite(HoHoHoWindow.LIST[randint(0,4)],model=self.world.block_1)
        self.block2_sprite = ModelSprite(HoHoHoWindow.LIST[randint(0,4)],model=self.world.block_2)
        self.block3_sprite = ModelSprite(HoHoHoWindow.LIST[randint(0,4)],model=self.world.block_3)
        self.block4_sprite = ModelSprite(HoHoHoWindow.LIST[randint(0,4)],model=self.world.block_4)
        self.block5_sprite = ModelSprite(HoHoHoWindow.LIST[randint(0,4)],model=self.world.block_5)
        self.bomb_1_sprite = ModelSprite('images/bomb.png', model = self.world.bomb_1)
        self.bomb_2_sprite = ModelSprite('images/bomb.png', model = self.world.bomb_2)
        self.heart_sprite = ModelSprite('images/life.png',model = self.world.heart)


    def draw_game_over(self):
        output = "Game Over"
        arcade.draw_text(output, 320, 350, arcade.color.WHITE, 54)
        arcade.draw_text("Your Score : " + str(self.world.latest_score),
                         380, 280,
                         arcade.color.WHITE, 24)
        arcade.draw_text("Highest Score : " + str(self.world.highest_score),
                         360,230,
                         arcade.color.WHITE_SMOKE, 24)
        output = "Click to restart"
        arcade.draw_text(output, 400, 150, arcade.color.WHITE, 24)


    def draw_game(self) :
        
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        #TIME
        minutes = int(self.world.time.total_time) // 60
        seconds = int(self.world.time.total_time) % 60
        output = f"Time: {minutes:02d}:{seconds:02d}"
        arcade.draw_text(output, 400, 550, arcade.color.WHITE, 20)

        self.block1_sprite.draw()
        self.block2_sprite.draw()
        self.block3_sprite.draw()
        self.block4_sprite.draw()
        self.block5_sprite.draw()
        self.bomb_1_sprite.draw()
        self.bomb_2_sprite.draw()
        self.heart_sprite.draw()
        self.player_sprite.draw()
        
        arcade.draw_text("Score : " + str(self.world.score),
                         50, self.height - 50,
                         arcade.color.WHITE, 20)

        w = self.width - 200
        for i in range(self.world.life):
            x = arcade.Sprite('images/life.png')
            x.set_position(w,550)
            x.draw()  
            w += 60

    def draw_instruction(self) :
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.game_cover)

        self.snow_sprite.draw()



    def on_draw(self):
        arcade.start_render()
        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.draw_instruction()
        elif self.current_state == GAME_RUNNING:
            self.draw_game()
        else:
            self.draw_game_over()
            
    def on_mouse_motion(self, x, y , dx, dy):
        self.world.on_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, button, modifiers):
        
        if self.current_state == INSTRUCTIONS_PAGE_0: 
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER :
            self.world.game_over = False
            self.current_state = GAME_RUNNING

        
    def update(self, delta):
        self.world.update(delta)
        if self.world.game_over == True :
            self.current_state = GAME_OVER
       

if __name__ == '__main__':
  window = HoHoHoWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
  arcade.run()