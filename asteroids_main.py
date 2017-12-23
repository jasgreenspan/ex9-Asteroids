##############################################################################
# FILE : asteroids_main.py
# WRITER : Jason Greenspan, jasonmg, 336126362; Yonatan Chamudot, ychamudot,
#  312516289
# EXERCISE : intro2cs ex9 2017-2018
# DESCRIPTION: Runs the asteroid game.
##############################################################################
import sys
import math
from screen import Screen
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo

DEFAULT_ASTEROIDS_NUM = 12
MAX_NUM_TORPEDOES = 15
CRASH_TITLE = 'You crashed!'
CRASH_MESSAGE = 'You lost a life'
TURN_DEG = 7
WIN_TITLE = 'You win!!!'
WIN_MESSAGE = 'All the asteroids were destroyed'
LOSE_TITLE = 'You lose!'
LOSE_MESSAGE = 'You lost all of your lives'
QUIT_TITLE = 'You Quit :('
QUIT_MESSAGE = 'Quitters never win'


class GameRunner:
    def __init__(self, asteroids_amnt):
        self.ship = Ship()
        self._screen = Screen()

        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        self.asteroids = []
        self.torpedoes = []

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
        self._screen.ontimer(self._do_loop, 5)

    def _end_game(self, title, message):
        Screen.show_message(self, title, message)
        Screen.end_game(self._screen)
        sys.exit()

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
            self._screen.draw_asteroid(asteroid, asteroid.get_x(),
                                       asteroid.get_y())
            if asteroid.has_intersection(self.ship):
                Screen.show_message(self, CRASH_TITLE, CRASH_MESSAGE)
                self._screen.remove_life()
                self._screen.unregister_asteroid(asteroid)
                self.asteroids.remove(asteroid)
            for torpedo in self.torpedoes:
                if asteroid.has_intersection(torpedo):
                    self._screen.unregister_asteroid(asteroid)
                    self.asteroids.remove(asteroid)
                    self._screen.unregister_torpedo(torpedo)
                    self.torpedoes.remove(torpedo)

        if (Screen.is_space_pressed(self._screen) 
            and len(self.torpedoes) <= MAX_NUM_TORPEDOES):
            current_tor = Torpedo()
            current_tor.set_heading(self.ship.get_heading())
            current_tor.set_x(self.ship.get_x())
            current_tor.set_y(self.ship.get_y())
            Screen.register_torpedo(self._screen, current_tor)
            Screen.draw_torpedo(self._screen, current_tor, Torpedo.get_x(
                current_tor), Torpedo.get_y(current_tor),
                                 Torpedo.get_heading(current_tor))
            self.torpedoes.append(current_tor)

        for torpedo in self.torpedoes:
            torpedo.move()
            self._screen.draw_torpedo(torpedo, torpedo.get_x(),
                                       torpedo.get_y(), torpedo.get_heading())

        if len(self.asteroids) == 0:
            self._end_game(WIN_TITLE, WIN_MESSAGE)

        if len(self._screen._lives) == 0:
            self._end_game(LOSE_TITLE, LOSE_MESSAGE)

        if Screen.should_end(self._screen):
            self._end_game(QUIT_TITLE, QUIT_MESSAGE)



def main(amnt):
    runner = GameRunner(amnt)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
