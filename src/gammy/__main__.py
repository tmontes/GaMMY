"""
GaMMY's entry point and single module.
"""

import sys

import importlib_metadata as ilm
import importlib_resources as ilr
import pygame


def main():

    # Adapted from https://www.pygame.org/docs/tut/PygameIntro.html

    pygame.init()

    meta = ilm.metadata(__package__)
    name = meta['name']
    version = meta['version']
    pygame.display.set_caption(f'{name} {version}')

    size = width, height = (800, 600)
    speed = [2, 1]
    background_color = (0, 192, 224)

    screen = pygame.display.set_mode(size)

    logo_filename = ilr.files(__package__) / 'logo.png'
    ball = pygame.image.load(str(logo_filename))
    ballrect = ball.get_rect()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                speed[0] = -speed[0]

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]

        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(background_color)
        screen.blit(ball, ballrect)

        pygame.display.flip()


if __name__ == '__main__':

    main()
