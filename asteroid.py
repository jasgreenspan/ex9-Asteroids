##############################################################################
# FILE : asteroid.py
# WRITER : Jason Greenspan, jasonmg, 336126362; Yonatan Chamudot, ychamudot, 312516289
# EXERCISE : intro2cs ex9 2017-2018
# DESCRIPTION: Creates the asteroids for asteroids game.
##############################################################################
import random
import math
from moveable_object import MoveableObject

RADIUS_FACTOR = 10
RADIUS_CORRECTER = 5

class Asteroid(MoveableObject):

    def __init__(self):
        x_speed = random.randint(-3, 3)
        y_speed = random.randint(-3, 3)
        MoveableObject.__init__(self, x_speed, y_speed)
        self.__size = 3

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def get_radius(self):
        return (self.__size * RADIUS_FACTOR) - RADIUS_CORRECTER
    
    def has_intersection(self, obj):
        intersection = False
        distance = math.sqrt(((obj.get_x() - self.get_x()) ** 2) + (
            obj.get_y() - self.get_y()) ** 2)
        if distance <= self.get_radius() + obj.get_radius():
            intersection = True
        return intersection
