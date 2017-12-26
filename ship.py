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
        MoveableObject.__init__(self)
        self.__heading = INITIAL_HEADING
        self.__radius = SHIP_RADIUS

    def get_heading(self):
        return self.__heading

    def set_heading(self, heading):
        self.__heading = heading

    def get_radius(self):
        return self.__radius
    
    def set_ship_x_speed(self, x_speed):
        # Only update x_speed if new speed is below limit (in both directions).
        if x_speed <= MAX_SPEED and x_speed >= -MAX_SPEED:  
            self.set_x_speed(x_speed)
    
    def set_ship_y_speed(self, y_speed):
        # Only update y_speed if new speed is below limit (in both directions).
        if y_speed <= MAX_SPEED and y_speed >= -MAX_SPEED:
            self.set_y_speed(y_speed)
