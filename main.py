import sys, logging, arcade, open_color



#check to make sure we are running the right version of Python

version = (3,7)

assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])



#turn on logging, in case we have to leave ourselves debugging messages

logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)



SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600

SCREEN_TITLE = "Space Shooter"

NUM_ENEMIES = 5

STARTING_LOCATION = (400, 100)

BULLET_DAMAGE = 10

ENEMY_HP = 100

HIT_SCORE = 10

KILL_SCORE = 100

class Bullet(arcade.Sprite):
    def __init__(self, position, velocity, damage):
        super().__init__("assets/new_bullet.png", 0.5)
        (self.center_x, self.center_y) = position
        (self.dx, self.dy) = velocity
        self.damage = damage

    def update(self):
        self.center_x += self.dx
        self.center_y += self.dy

class Player(arcade.Sprite):

    def __init__(self):
        super().__init__("assets/SpaceShipNormal.png", 0.5)
        (self.center_x, self.center_y) = STARTING_LOCATION

class Enemy(arcade.Sprite):
    def __init__(self, position):
        super().__init__("assets/alien.png", 0.25)
        self.hp = ENEMY_HP
        (self.center_x, self.center_y) = position

class Window(arcade.Window):



    def __init__(self, width, height, title):



        # Call the parent class's init function

        super().__init__(width, height, title)
        


        # Make the mouse disappear when it is over the window.

        # So we just see our object, not the pointer.

        self.set_mouse_visible(False)


        arcade.set_background_color(open_color.black)
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player = Player()
        self.score = 0







    def setup(self):

        for i in range(NUM_ENEMIES):
            x = 120 * (i+1) + 40
            y = 500
            enemy = Enemy((x,y))
            self.enemy_list.append(enemy) 



    def update(self, delta_time):

        self.bullet_list.update()
        self.num = NUM_ENEMIES
        for e in self.enemy_list:
            if arcade.check_for_collision_with_list(e, self.bullet_list):
                for f in self.bullet_list:
                    f.kill()
                e.hp -= 10
                self.score += 10
                if e.hp == 0:
                    e.kill()
                    self.score += 100
                    self.num -= 1
        if self.num == 0:
            arcade.draw_text("You win!", 100, SCREEN_HEIGHT - 100, open_color.orange_0, 16)


    def on_draw(self):

        """ Called whenever we need to draw the window. """

        arcade.start_render()
        arcade.draw_text(str(self.score), 20, SCREEN_HEIGHT - 40, open_color.orange_0, 16)
        self.player.draw()
        self.bullet_list.draw()
        self.enemy_list.draw()









    def on_mouse_motion(self, x, y, dx, dy):

        """ Called to update our objects. Happens approximately 60 times per second."""

        self.player.center_x = x



    def on_mouse_press(self, x, y, button, modifiers):

        """

        Called when the user presses a mouse button.

        """

        if button == arcade.MOUSE_BUTTON_LEFT:
            x = self.player.center_x
            y = self.player.center_y + 15
            bullet = Bullet((x,y), (0,10), BULLET_DAMAGE)
            self.bullet_list.append(bullet)
            pass



    def on_mouse_release(self, x, y, button, modifiers):

        """

        Called when a user releases a mouse button.

        """

        pass



    def on_key_press(self, key, modifiers):

        """ Called whenever the user presses a key. """

        if key == arcade.key.LEFT:
            self.player.center_x -= 25
            print("Left")

        elif key == arcade.key.RIGHT:
            self.player.center_x += 25
            print("Right")

        elif key == arcade.key.UP:
            self.player.center_y += 25
            print("Up")

        elif key == arcade.key.DOWN:
            self.player.center_y -= 25
            print("Down")

        elif key == arcade.key.SPACE:
            x = self.player.center_x
            y = self.player.center_y + 15
            bullet = Bullet((x,y), (0,10), BULLET_DAMAGE)
            self.bullet_list.append(bullet)
            pass



    def on_key_release(self, key, modifiers):

        """ Called whenever a user releases a key. """

        pass





def main():

    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()





if __name__ == "__main__":

    main()