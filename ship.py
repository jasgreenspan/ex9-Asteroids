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

class Ship(MoveableObject):
    def __init__(self):
        MoveableObject.__init__(self)
        self.__heading = INITIAL_HEADING
        self.__radius = SHIP_RADIUS

    def get_heading(self):
        return self.__heading

    def set_heading(self, heading):
        self.__heading = heading

    def get_radius(self):
        return self.__radius
