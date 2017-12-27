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
INITIAL_LIFESPAN = 0


class Torpedo(MoveableObject):
    def __init__(self):
        """Initiates the torpedo class"""
        MoveableObject.__init__(self)
        self.__radius = TORPEDO_RADIUS
        self.__lifespan = INITIAL_LIFESPAN

    def get_heading(self):
        """Returns the torpedo's heading"""
        return self.__heading

    def get_radius(self):
        """Returns the torpedo's radius"""
        return self.__radius

    def set_heading(self, heading):
        """Sets the torpedo's heading"""
        self.__heading = heading

    def set_torpedo_speed(self):
        """Sets the x and y speed of the torpedo"""
        self.set_x_speed(self.get_x_speed() + (ACCELERATION_FACTOR *
                                               math.cos(math.radians(
                                                   self.get_heading()))))
        self.set_y_speed(self.get_y_speed() + (ACCELERATION_FACTOR *
                                               math.sin(math.radians(
                                                   self.get_heading()))))

    def get_lifespan(self):
        """Returns the lifespan of the torpedo"""
        return self.__lifespan

    def get_older(self):
        """Increases the lifespan of the torpedo by one"""
        self.__lifespan += 1
