jasonmg,ychamudot
336126362,312516289
Jason Greenspan,Yonatan Chamudot
=====================================
=     README for ex9: asteroids     =
=====================================

==================
=  Description:  =
==================
An implementation of the classic game asteroids, with a focus on object
oriented programming.
Ship class:
__init__(self):
        """Initiates the ship class"""
get_heading(self):
        """Returns the heading of the ship"""
set_heading(self, heading):
        """Sets the heading of the ship"""
get_radius(self):
        """Returns the radius of the ship"""
set_ship_x_speed(self, x_speed):
        """Sets the speed of the ship along the x axis"""
set_ship_y_speed(self, y_speed):
        """Sets the speed of the ship along the y axis"""
MoveableObject Class:
__init__(self, x_speed=0, y_speed=0):
        """Initiates the moveable object class, a parent class for the
        torpedo, asteroid, and ship classes"""
get_x(self):
        """Returns the object's location along the x axis"""
get_y(self):
        """Returns the object's location along the x axis"""
set_x(self, x):
        """Sets the object's location along the x axis"""
set_y(self, y):
        """Sets the object's location along the y axis"""
get_x_speed(self):
        """Returns the object's speed along the x axis"""
get_y_speed(self):
        """Returns the object's speed along the y axis"""
set_x_speed(self, x_speed):
        """Sets the object's speed along the x axis"""
set_y_speed(self, y_speed):
        """Sets the object's speed along the y axis"""
move(self):
        """Moves the object on the x-y plane"""
Asteroid class:
__init__(self):
        """Initiate the asteroid class. The asteroid's initial position and
        speed are determined randomly, while its initial size is a constant"""
get_size(self):
        """Returns the size of the current asteroid"""
set_size(self, size):
        """Sets the size of the current asteroid"""
get_radius(self):
        """Returns the radius of the current asteroid (a function of its
        size and constant factors)"""
has_intersection(self, obj):
        """Returns True if the current asteroid crashes into another object,
        and False otherwise"""
GameRunner class:
__init__(self, asteroids_amnt):
        """Initiates the GameRunner class"""
run(self):
        """Run the asteroids game"""
get_screen(self):
        """Return a screen object"""
_do_loop(self):
        """Set a timer to repeat the game loop"""
_end_game(self, title, message):
        """Take a title and message related to the reason why the game is
        ending, display the message, close the gui and end the game"""
_remove_asteroid(self, asteroid):
        """Remove an asteroid from the game"""
_remove_torpedo(self, torpedo):
        """Remove a torpedo from the game"""
_fire_torpedo(self):
        """Fire a torpedo. The torpedo's location and heading are
        determined by the ship's location and heading, and its speed is
        affected by the ship's speed."""
_set_split_asteroid_speed(self, asteroid, torpedo_x_speed,
                                  torpedo_y_speed, asteroid_x_speed,
                                  asteroid_y_speed, positive=True):
        """Set the velocities for the two asteroids that break off of a
        larger asteroid when it is destroyed."""
_split_asteroid(self, asteroid, torpedo):
        """Split one large asteroid into two smaller asteroids"""
_turn_ship_left(self):
        """Turn the ship left (Increase its heading)"""
_turn_ship_right(self):
        """Turn the ship right (Decrease its heading)"""
_thrust_ship(self):
        """Fire the ships engine, adjusting its speed along both axes"""
_game_loop(self):
        """The main function that runs the game. Every loop, the ship is
        steered and thrusted, every asteroid and torpedo in the game is
        moved, intersections between the asteroids and torpedoes,
        and between the asteroids and ship are processed. The lifespan and
        number of torpedoes on screen is limited, and the player's score is
        adjusted if they destroy an asteroid. Finally, if the player wins,
        loses, or quits the game, the game ends."""
======================
=  Special Comments  =
======================
Three design decisions:
- We chose to use class inheritance and implement a fourth class
(moveable_object), that would act as the parent class for the torpedo,
asteroid, and ship classes. We could have chosen to implement all the classes
separately, but because they shared so many functions and attributes, we
thought it would be neater and also more interesting to try to use class
inheritance.
- We decided to split the main function responsible for running the game into
smaller functions, such as functions to turn the ship to the left and right, a
function to end the game, a function to split a large asteroid into two smaller
ones, etc. We could have left all the functions inside the main game loop, but
splitting it up makes the code much neater, more understandable to a reader,
and more modular.
- We had to set the initial speed for the asteroids at random. Since no
specific range of values was given for the speed, we set the initial speed to
be an integer between 1 and 3, and then randomly multiplied the speed by 1 or
-1 to determine if the asteroid would fly left/right or up/down. Initially we
tried setting the speed to be a random integer between -3 and 3, however this
caused two problems: first, the asteroid would sometimes receive a 0 value for
both its x and y speeds, causing it to remain still on the screen. And second,
when an asteroid with a 0 value for either its x or y speed was destroyed, the
speeds of the smaller resulting asteroids would be determined by a formula that
 would try to divide by 0, raising an exception and crashing the program.

