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


def create_angvel():
    '''Creating each planets' angular velocity'''
    omega = []
    # making them different so they go at different speeds
    for o in range(5, 9):
        omega_values = 0.1 / o
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
        # altering speeds
        angles[v] += omegas[v]
        # changing x and y value for each planet to where it should go
        planets[v][2] = planets[v][2] + planets[v][0] * omegas[v] * math.cos(angles[v] + math.pi / 2)
        planets[v][3] = planets[v][3] - planets[v][1] * omegas[v] * math.sin(angles[v] + math.pi / 2)


def move_ring(planets):
    '''Making a ring move with blue planet'''
    back_ring = [planets[1][2] - 30, planets[1][3] - 10, 60, 20]
    front_ring = [planets[1][2] - 30, planets[1][3] - 10, 60, 20]
    return back_ring, front_ring


def draw_stars(screen, list):
    '''Drawing stars to twinkle'''
    STARRY = (252, 252, 202)
    LYELLOW = (255, 255, 153)
    # slicing the star list into 2 lists of 80
    first_list = int(len(list) / 2)
    sec_list = len(list)
    stars1 = list[0:first_list]
    stars2 = list[first_list:sec_list]
    # getting time to make stars blink differently every 0.5 seconds
    current_time = pygame.time.get_ticks()
    star_time = math.floor(current_time / 500)
    for s in range(80):
        # 2 positions, 2 colours each
        if star_time % 4 == 0:
            pygame.draw.circle(screen, STARRY, [stars1[s][0], stars1[s][1]], stars1[s][2])
        elif star_time % 4 == 1:
            pygame.draw.circle(screen, LYELLOW, [stars1[s][0], stars1[s][1]], stars1[s][2])
        elif star_time % 4 == 2:
            pygame.draw.circle(screen, STARRY, [stars2[s][0], stars2[s][1]], stars2[s][2])
        elif star_time % 4 == 3:
            pygame.draw.circle(screen, LYELLOW, [stars2[s][0], stars2[s][1]], stars2[s][2])

def draw_sun(screen, centre):
    '''Drawing sun'''
    # drawing it in the centre of the screen
    centre_of_rotation_x = centre[0]
    centre_of_rotation_y = centre[1]
    YELLOW = (242, 242, 61)
    pygame.draw.circle(screen, YELLOW, [centre_of_rotation_x, centre_of_rotation_y], 40)


def draw_orbits(screen, planets):
    '''Drawing orbits of planets'''
    SCREENW = 1280
    SCREENH = 720
    WHITE = (255, 255, 255)
    for orb in range(4):
        # half the screen minus the x/y radius
        ell_x = SCREENW / 2 - planets[orb][0]
        ell_y = SCREENH / 2 - planets[orb][1]
        # x/y radius times 2
        ell_w = planets[orb][0] * 2
        ell_h = planets[orb][1] * 2
        pygame.draw.ellipse(screen, WHITE, [ell_x, ell_y, ell_w, ell_h], 1)

def draw_planets(screen, planets, rings):
    '''Drawing the planets'''
    PURPLE = (221, 160, 221)
    GREEN = (34, 139, 34)
    RED = (255, 0, 0)
    BROWN = (222, 184, 135)
    LBLUE = (152, 242, 245)
    back_ring = rings[0]
    front_ring = rings[1]

    # [p][2] and [p][3] are the respective x and y values
    # first planet
    pygame.draw.circle(screen, RED, [planets[0][2], planets[0][3]], 8)

    # blue planet with the ring
    pygame.draw.arc(screen, PURPLE, back_ring, 0, math.pi, 4)
    pygame.draw.circle(screen, LBLUE, [planets[1][2], planets[1][3]], 20)
    pygame.draw.arc(screen, PURPLE, front_ring, math.pi, 0, 4)

    # last 2 planets
    pygame.draw.circle(screen, BROWN, [planets[2][2], planets[2][3]], 15)
    pygame.draw.circle(screen, GREEN, [planets[3][2], planets[3][3]], 25)
