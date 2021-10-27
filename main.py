'''
Ｓｏｌａｒ Ｓｙｓｔｅｍ
This program uses pygame to make a cute little animation of planets in orbit.
The planets can be sped up or slowed down by pressing the arrow keys.
~Sara Keating~
'''

from solarmovefunc import *
from solardrawfunc import *


def main():
    '''Main Program'''
    pygame.init()
    # set up
    screen = set_screen()
    centre_points_list = create_centre()
    angles_list = create_angles()
    star_list = create_stars()
    planets = create_planets(centre_points_list, angles_list)

    speed = 0

    clock = pygame.time.Clock()

    done = False

    # main program loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    speed += 0.01
                elif event.key == pygame.K_DOWN:
                    speed -= 0.01

        omega = create_angvel(speed)

        move_planets(omega, angles_list, planets)
        ring_list = move_ring(planets)

        BLACK = (0, 0, 0)
        screen.fill(BLACK)

        draw_stars(screen, star_list)
        draw_sun(screen, centre_points_list)
        draw_orbits(screen, planets)
        draw_planets(screen, planets, ring_list)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
