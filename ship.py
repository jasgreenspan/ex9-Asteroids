##############################################################################
# FILE : ship.py
# WRITER : Jason Greenspan, jasonmg, 336126362; Yonatan Chamudot, ychamudot,
#  312516289
# EXERCISE : intro2cs ex9 2017-2018
# DESCRIPTION: Creates the ship for asteroids game.
##############################################################################
from moveable_object import MoveableObject

INITIAL_HEADING = 0.0
SHIP_RADIUS = 1
MAX_SPEED = 10


class Ship(MoveableObject):
    def __init__(self):
        """Initiates the ship class"""
        MoveableObject.__init__(self)
        self.__heading = INITIAL_HEADING
        self.__radius = SHIP_RADIUS

    def get_heading(self):
        """Returns the heading of the ship"""
        return self.__heading

    def set_heading(self, heading):
        """Sets the heading of the ship"""
        self.__heading = heading

    def get_radius(self):
        """Returns the radius of the ship"""
        return self.__radius

    def set_ship_x_speed(self, x_speed):
        """Sets the speed of the ship along the x axis"""
        if x_speed <= MAX_SPEED and x_speed >= -MAX_SPEED:
            self.set_x_speed(x_speed)

    def set_ship_y_speed(self, y_speed):
        """Sets the speed of the ship along the y axis"""
        if y_speed <= MAX_SPEED and y_speed >= -MAX_SPEED:
            self.set_y_speed(y_speed)
