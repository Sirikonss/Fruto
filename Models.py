class Player :
    def __init__(self,x,y) :
        self.x = x
        self.y = y

    def update(self,delta):
        if self.x > 1000:
            self.x = 0
        self.x += 0


class World :
    def __init__(self,width,height) :
        self.width = width
        self.height = height
        self.player = Player( 500, 150)

    def update(self,delta) :
        self.player.update(delta)



