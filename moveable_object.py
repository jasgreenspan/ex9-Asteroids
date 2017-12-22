##############################################################################
# FILE : moveable_object.py
# WRITER : Jason Greenspan, jasonmg, 336126362; Yonatan Chamudot, ychamudot, 312516289
# EXERCISE : intro2cs ex# 2017-2018
# DESCRIPTION: Defines a parent-class for moveable objects.
##############################################################################
import random
from screen import Screen

MAX_SPEED = 3

class MoveableObject:    
    
    def __init__(self, x_speed = 0, y_speed = 0):
        self.__x = random.randint(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X)
        self.__y = random.randint(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y)
        self.__x_speed = x_speed
        self.__y_speed = y_speed
        
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_x_speed(self):
        return self.__x_speed

    def get_y_speed(self):
        return self.__y_speed

    def set_x_speed(self, xspeed):
        if xspeed <= MAX_SPEED and xspeed >= -MAX_SPEED:
            self.__x_speed = xspeed

    def set_y_speed(self, yspeed):
        if yspeed <= MAX_SPEED and yspeed >= -MAX_SPEED:
            self.__y_speed = yspeed

    def move(self):
        new_x_coord = (self.__x_speed + self.__x - Screen.SCREEN_MIN_X) %(
            Screen.SCREEN_MAX_X- Screen.SCREEN_MIN_X) + Screen.SCREEN_MIN_X
        new_y_coord = (self.__y_speed + self.__y - Screen.SCREEN_MIN_Y) %(
            Screen.SCREEN_MAX_Y- Screen.SCREEN_MIN_Y) + Screen.SCREEN_MIN_Y

        self.set_x(new_x_coord)
        self.set_y(new_y_coord)
