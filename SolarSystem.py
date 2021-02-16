'''
Ｓｏｌａｒ Ｓｙｓｔｅｍ
This program uses pygame to make a cute little animation of planets in orbit
~Sara Keating~
'''

from SolarSystemFunc import *

def main():
    '''Main Program'''

    # set up

    pygame.init()

    screen = set_screen()

    centre_points_list = create_centre()

    omega = create_angvel()

    angles_list = create_angles()

    star_list = create_stars()

    planets = create_planets(centre_points_list, angles_list)

    clock = pygame.time.Clock()

    done = False

    # main program loop
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        move_planets(omega, angles_list, planets)

        ring_list = move_ring(planets)

        screen.fill((0, 0, 0))

        draw_stars(screen, star_list)

        draw_sun(screen, centre_points_list)

        draw_orbits(screen, planets)

        draw_planets(screen, planets, ring_list)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
