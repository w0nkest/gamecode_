import pygame
import os
import sys


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def winscreen(name):
    intro_text = [f'{name} is win!',
                  'Congratulations!']

    fon = pygame.transform.scale(load_image('endscreenbg.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.SysFont('comicsansms', 60)
    text_coord = 50

    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 50
        intro_rect.top = text_coord
        intro_rect.x = 80
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

        pygame.display.flip()
        clock.tick(FPSM)


if __name__ == '__main__':
    pygame.init()
    STARTGAME = False
    FPSM = 60
    clock = pygame.time.Clock()
    width, height = 1070, 600
    screen = pygame.display.set_mode((width, height))
    button_objects = []
    winscreen('Cody')
