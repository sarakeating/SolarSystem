'''
Drawing functions
'''

import pygame
import math


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
        pygame.draw.ellipse(screen, WHITE, [ell_x, ell_y, ell_w, ell_h], 2)


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
