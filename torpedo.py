##############################################################################
# FILE : torpedo.py
# WRITER : Jason Greenspan, jasonmg, 336126362; Yonatan Chamudot, ychamudot,
#  312516289
# EXERCISE : intro2cs ex9 2017-2018
# DESCRIPTION: Creates the torpedoes for asteroids game.
##############################################################################
from moveable_object import MoveableObject
import math

TORPEDO_RADIUS = 4
ACCELERATION_FACTOR = 2

class Torpedo(MoveableObject):
    def __init__(self):
        MoveableObject.__init__(self)
        self.__radius = TORPEDO_RADIUS

    def get_heading(self):
        return self.__heading

    def get_radius(self):
        return self.__radius

    def set_heading(self, heading):
        self.__heading = heading

    def set_torpedo_speed(self):
        self.set_x_speed(self.get_x_speed() + (ACCELERATION_FACTOR *
                         math.cos(math.radians(self.get_heading()))))
        self.set_y_speed(self.get_y_speed() + (ACCELERATION_FACTOR *
                         math.sin(math.radians(self.get_heading()))))
