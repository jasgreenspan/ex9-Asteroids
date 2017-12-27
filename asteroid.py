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
ASTEROID_INITIAL_RADIUS = 3
MIN_ASTEROID_SPEED = 1
MAX_ASTEROID_SPEED = 2
POSITIVE_DIRECTION = 1
NEGATIVE_DIRECTION = -1


class Asteroid(MoveableObject):
    def __init__(self):
        """Initiate the asteroid class. The asteroid's initial position and
        speed are determined randomly, while its initial size is a constant"""
        x_speed = random.randint(MIN_ASTEROID_SPEED, MAX_ASTEROID_SPEED) * \
                  random.choice((NEGATIVE_DIRECTION, POSITIVE_DIRECTION))
        y_speed = random.randint(MIN_ASTEROID_SPEED, MAX_ASTEROID_SPEED) * \
                  random.choice((NEGATIVE_DIRECTION, POSITIVE_DIRECTION))
        MoveableObject.__init__(self, x_speed, y_speed)
        self.__size = ASTEROID_INITIAL_RADIUS

    def get_size(self):
        """Returns the size of the current asteroid"""
        return self.__size

    def set_size(self, size):
        """Sets the size of the current asteroid"""
        self.__size = size

    def get_radius(self):
        """Returns the radius of the current asteroid (a function of its
        size and constant factors)"""
        return (self.__size * RADIUS_FACTOR) - RADIUS_CORRECTER

    def has_intersection(self, obj):
        """Returns True if the current asteroid crashes into another object,
        and False otherwise"""
        intersection = False
        # Calcutate distance between asteroid and intersecting object.
        distance = math.sqrt(((obj.get_x() - self.get_x()) ** 2) + (
            obj.get_y() - self.get_y()) ** 2)
        if distance <= self.get_radius() + obj.get_radius():
            intersection = True
        return intersection
