##############################################################################
# FILE : torpedo.py
# WRITER : Jason Greenspan, jasonmg, 336126362; Yonatan Chamudot, ychamudot,
#  312516289
# EXERCISE : intro2cs ex9 2017-2018
# DESCRIPTION: Creates the torpedoes for asteroids game.
##############################################################################
from moveable_object import MoveableObject

INITIAL_HEADING = 0.0

class Torpedo(MoveableObject):
    def __init__(self):
        MoveableObject.__init__(self)
        self.__heading = INITIAL_HEADING

    def get_heading(self):
        return self.__heading
