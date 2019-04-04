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


class FrutoWindow(arcade.Window):
    FRUITS_LIST = ['images/apple.png','images/pineapple.png','images/banana.png','images/orange.png','images/watermelon.png']

    def __init__(self, width, height):
        super().__init__(width, height)


        arcade.set_background_color(arcade.color.BABY_BLUE)
        self.background = arcade.load_texture('images/background.png')
        self.world = World(width, height)
        self.set_mouse_visible(False)
        self.current_state = GAME_RUNNING


        self.player_sprite = ModelSprite('images/girl.png', model=self.world.player)
        self.block1_sprite = ModelSprite(FrutoWindow.FRUITS_LIST[randint(0,4)],model=self.world.block_1)
        self.block2_sprite = ModelSprite(FrutoWindow.FRUITS_LIST[randint(0,4)],model=self.world.block_2)
        self.block3_sprite = ModelSprite(FrutoWindow.FRUITS_LIST[randint(0,4)],model=self.world.block_3)
        self.block4_sprite = ModelSprite(FrutoWindow.FRUITS_LIST[randint(0,4)],model=self.world.block_4)
        self.block5_sprite = ModelSprite(FrutoWindow.FRUITS_LIST[randint(0,4)],model=self.world.block_5)
        self.enemies_1_sprite = ModelSprite('images/durian.png', model = self.world.enemies_1)
        self.enemies_2_sprite = ModelSprite('images/durian.png', model = self.world.enemies_2)
        self.bomb_1_sprite = ModelSprite('images/bomb.png', model = self.world.bomb_1)
        self.bomb_2_sprite = ModelSprite('images/bomb.png', model = self.world.bomb_2)
        #self.bomb_3_sprite = ModelSprite('images/bomb.png', model = self.world.bomb_3)

    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """
        output = "Game Over"
        arcade.draw_text(output, 350, 300, arcade.color.WHITE, 54)

        
        

        #output = "Click to restart"
        #arcade.draw_text(output, 310, 300, arcade.color.WHITE, 24)

    def draw_game(self) :
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.block1_sprite.draw()
        self.block2_sprite.draw()
        self.block3_sprite.draw()
        self.block4_sprite.draw()
        self.block5_sprite.draw()
        self.enemies_1_sprite.draw()
        self.enemies_1_sprite.draw()
        self.bomb_1_sprite.draw()
        self.bomb_2_sprite.draw()
        #self.bomb_3_sprite.draw()

        self.player_sprite.draw()

        arcade.draw_text("Score : " + str(self.world.score),
                         50, self.height - 50,
                         arcade.color.WHITE, 20)
        arcade.draw_text("Highest Score : " + str(self.world.highest_score),
                         50, self.height - 100,
                         arcade.color.WHITE, 20)

        w = self.width - 100
        for i in range(self.world.life):
            arcade.draw_text("O",
                         w, self.height - 50,
                         arcade.color.WHITE, 20)

            w += 20


    def on_draw(self):
        arcade.start_render()
        if self.world.game_over == False:
            self.draw_game()
        elif self.world.game_over == True : 
            #self.draw_game()
            self.draw_game_over()
            
    def on_mouse_motion(self, x, y , dx, dy):
        self.world.on_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, button, modifiers):
        #self.world.on_key_press(key, modifiers)
        if self.world.game_over == True :
            # Restart the game.
            self.world.game_over = False
        

        
    def update(self, delta):
        self.world.update(delta)





if __name__ == '__main__':
  window = FrutoWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
  arcade.run()
