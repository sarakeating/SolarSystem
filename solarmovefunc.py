'''
Functions for setting up and moving planets
'''

import pygame
import random
import math


def set_screen():
    '''Setting size and creating window'''
    size = (1280, 720)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Solar System")
    return screen


def create_centre():
    '''Creating a centre point for planets to rotate around'''
    SCREENW = 1280
    SCREENH = 720
    centre_of_rotation_x = SCREENW / 2
    centre_of_rotation_y = SCREENH / 2
    return centre_of_rotation_x, centre_of_rotation_y


def create_angvel(varSpeed):
    '''Creating each planets' angular velocity'''
    omega = []
    # making them so they go at different speeds
    for o in range(1, 5):
        omega_values = 0.1 / o + varSpeed
        omega.append(omega_values)
    return omega


def create_angles():
    '''Creating a list of an angle for each planet'''
    angles = []
    for a in range(4):
        # using the same angle, but each value will be altered with omega later
        angle = math.radians(45)
        angles.append(angle)
    return angles


def create_stars():
    '''Randomly creating stars'''
    SCREENW = 1280
    SCREENH = 720
    stars = []
    for s in range(160):
        x_star1 = random.randrange(0, SCREENW)
        y_star1 = random.randrange(0, SCREENH)
        s_star1 = random.randrange(2, 5)
        x_star2 = random.randrange(0, SCREENW)
        y_star2 = random.randrange(0, SCREENH)
        s_star2 = random.randrange(2, 5)
        stars.append([x_star1, y_star1, s_star1])
        stars.append([x_star2, y_star2, s_star2])
    return stars


def create_planets(centre, angle):
    '''Creating 4 planets to go around sun'''
    centre_of_rotation_x = centre[0]
    centre_of_rotation_y = centre[1]
    cons_angle = angle[0]
    planets = []
    for p in range (80, 291, 70):
        # different x and y radius so orbit will be elliptical
        x_radius = p * 2
        y_radius = p
        x = centre_of_rotation_x + x_radius * math.cos(cons_angle)
        y = centre_of_rotation_y - y_radius * math.sin(cons_angle)
        planets.append([x_radius, y_radius, x, y])
    return planets


def move_planets(omegas, angles, planets):
    '''Moving the planets in orbit'''
    for v in range(4):
        # altering each planet's angle with it's own omega value
        angles[v] -= omegas[v]
        # changing x and y value for each planet to where it should go
        planets[v][2] = planets[v][0] * math.cos(angles[v]) + create_centre()[0]
        planets[v][3] = planets[v][1] * math.sin(angles[v]) + create_centre()[1]


def move_ring(planets):
    '''Making a ring move with blue planet'''
    back_ring = [planets[1][2] - 30, planets[1][3] - 10, 60, 20]
    front_ring = [planets[1][2] - 30, planets[1][3] - 10, 60, 20]
    return back_ring, front_ring
