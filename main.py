import pygame
import sys
import os
import time


def terminate():
    pygame.quit()
    sys.exit()


# menu screen
def start_screen():
    intro_text = ["игрулька"]

    fon = pygame.transform.scale(load_image('bgmenu1.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text_coord = 50
    Button(width - int(175 * (width / 1070)), int(50 * (height / 600)), 150, 70, 'Играть', playfunc)
    Button(width - int(205 * (width / 1070)), height - int((70 * (height / 600))), 150, 50, 'выход', terminate)
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = width // 2 - intro_rect.width // 2
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif STARTGAME:
                return
        for obj in button_objects:
            obj.process()
        pygame.display.flip()
        clock.tick(FPSM)


# rules screen function
def rules_screen():
    intro_text = ["СВОДКА ПРАВИЛ",
                  "(нажмите в любом месте окна для продолжения)", "", ""
                  'Используйте "W", "A", "S", "D" для управления движением персонажем слева, "leftALT" для его атаки.',
                  'Используйте стрелочки для управления движением персонажа справа, "rightALT" для его атаки.',
                  'Проигрывает игрок, у которого закончилось здоровье.', '', '', '', 'Удачи!'
                  ]

    fon = pygame.transform.scale(load_image('pixelroad_bg2.jpg'), (width, height))
    screen.blit(fon, (0, 0))

    # head text of rules screen
    mainfont = pygame.font.SysFont('comicsansms', 40)
    font = pygame.font.SysFont('comicsansms', 20)
    string_rendered = mainfont.render(intro_text[0], True, (252, 0, 0))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 50
    intro_rect.x = width // 2 - string_rendered.get_width() // 2
    text_coord = intro_rect.height + 50
    screen.blit(string_rendered, intro_rect)
    heightmaintext = string_rendered.get_height()

    # tip to skip rules screen
    string_rendered = font.render(intro_text[1], True, (252, 40, 71))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 50 + heightmaintext
    intro_rect.x = width // 2 - string_rendered.get_width() // 2
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)

    # rules text
    for line in intro_text[2:]:
        string_rendered = font.render(line, True, (0, 0, 0))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = width // 2 - string_rendered.get_width() // 2
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN or \
                    int(time.time() - timerules) >= 10:
                return
        pygame.display.flip()
        clock.tick(FPSM)


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Button:
    def __init__(self, x, y, width_b, height_b, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width_b
        self.height = height_b
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.buttonText = buttonText

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = pygame.font.Font(None, 50).render(self.buttonText, True, (255, 255, 255))
        button_objects.append(self)

    def process(self):
        # self.buttonSurface.fill((255, 255, 255))
        self.buttonSurf = pygame.font.Font(None, 50).render(self.buttonText, True, (255, 255, 255))
        mousePos = pygame.mouse.get_pos()
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurf = pygame.font.Font(None, 50).render(self.buttonText, True, self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurf = pygame.font.Font(None, 50).render(self.buttonText, True, self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        screen.blit(self.buttonSurf, (self.x, self.y))
        '''self.buttonSurface.blit(self.buttonSurf, [
                self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
                self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
            ])'''
        screen.blit(self.buttonSurf, self.buttonRect)


def playfunc():
    global STARTGAME
    STARTGAME = True


if __name__ == '__main__':
    pygame.init()
    STARTGAME = False
    FPSM = 60
    clock = pygame.time.Clock()
    width, height = 1070, 600
    screen = pygame.display.set_mode((width, height))
    button_objects = []
    start_screen()
    timerules = time.time()
    rules_screen()
    print(100)
