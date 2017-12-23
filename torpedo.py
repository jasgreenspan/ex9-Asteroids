##############################################################################
# FILE : torpedo.py
# WRITER : Jason Greenspan, jasonmg, 336126362; Yonatan Chamudot, ychamudot,
#  312516289
# EXERCISE : intro2cs ex9 2017-2018
# DESCRIPTION: Creates the torpedoes for asteroids game.
##############################################################################
from moveable_object import MoveableObject

INITIAL_HEADING = 0.0
TORPEDO_RADIUS = 4
TORPEDO_SPEED = 10

class Torpedo(MoveableObject):
    def __init__(self):
        MoveableObject.__init__(self)
        self.__heading = INITIAL_HEADING
        self.__radius = TORPEDO_RADIUS
        self.set_x_speed(TORPEDO_SPEED)
        self.set_y_speed(TORPEDO_SPEED)

    def get_heading(self):
        return self.__heading

    def get_radius(self):
        return self.__radius

    def set_heading(self, heading):
        self.__heading = heading

    def new_tor_speed_x(self):
        pass
