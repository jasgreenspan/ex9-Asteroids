##############################################################################
# FILE : asteroids_main.py
# WRITER : Jason Greenspan, jasonmg, 336126362; Yonatan Chamudot
# EXERCISE : intro2cs ex9 2017-2018
# DESCRIPTION: Runs the asteroid game.
##############################################################################
import sys
import math
from screen import Screen
from ship import Ship
from asteroid import Asteroid

DEFAULT_ASTEROIDS_NUM = 5
CRASH_TITLE = 'You crashed!'
CRASH_MESSAGE = 'You lost a life'
TURN_DEG = 7

class GameRunner:

    def __init__(self, asteroids_amnt):
        self.ship = Ship()
        self._screen = Screen()

        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        self.asteroids = []

        for asteroid in range(asteroids_amnt):
            current_ast = Asteroid()
            Screen.register_asteroid(self._screen, current_ast,
                                     current_ast.get_size())
            Screen.draw_asteroid(self._screen, current_ast, Asteroid.get_x(
                current_ast), Asteroid.get_y(current_ast))
            self.asteroids.append(current_ast)
            
    def run(self):
        self._do_loop()
        self._screen.start_screen()

    def get_screen(self):
        return self._screen

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop,5)

    def _game_loop(self):
        if Screen.is_left_pressed(self._screen):
            self.ship.set_heading(self.ship.get_heading() + TURN_DEG)
        if Screen.is_right_pressed(self._screen):
            self.ship.set_heading(self.ship.get_heading() - TURN_DEG)
        if Screen.is_up_pressed(self._screen):
            new_x_speed = self.ship.get_x_speed() + math.cos(
                math.radians(self.ship.get_heading()))
            new_y_speed = self.ship.get_y_speed() + math.sin(
                math.radians(self.ship.get_heading()))   
            self.ship.set_x_speed(new_x_speed)
            self.ship.set_y_speed(new_y_speed)
        self.ship.move()
        Screen.draw_ship(self._screen, self.ship.get_x(), self.ship.get_y(),
                         self.ship.get_heading())
        
        for asteroid in self.asteroids:
            asteroid.move()
            self._screen.draw_asteroid(asteroid, asteroid.get_x(), asteroid.get_y())
            if asteroid.has_intersection(self.ship):
                Screen.show_message(self, CRASH_TITLE, CRASH_MESSAGE)
                self._screen.remove_life()
                self._screen.unregister_asteroid(asteroid)
                self.asteroids.remove(asteroid)


def main(amnt):
    runner = GameRunner(amnt)
    runner.run()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main( int( sys.argv[1] ) )
    else:
        main( DEFAULT_ASTEROIDS_NUM )