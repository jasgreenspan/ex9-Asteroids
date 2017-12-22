##############################################################################
# FILE : ship.py
# WRITER : Jason Greenspan, jasonmg, 336126362; Yonatan Chamudot
# EXERCISE : intro2cs ex9 2017-2018
# DESCRIPTION: Creates the ship for asteroids game.
##############################################################################
from moveable_object import MoveableObject

class Ship(MoveableObject):

    def __init__(self):
        MoveableObject.__init__(self)
        self.__heading = 0.0
        self.__radius = 1

    def get_heading(self):
        return self.__heading

    def set_heading(self, heading):
        self.__heading = heading
        
    def get_radius(self):
        return self.__radius