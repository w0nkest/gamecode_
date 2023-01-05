import pygame
import sys
import os


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["игрулька"]

    fon = pygame.transform.scale(load_image('bg_menu_shrek1.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text_coord = 50
    Button(width // 2 - 150 // 2, 380, 150, 70, 'play', playfunc)
    Button(30, 380, 150, 70, 'quit', terminate)
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = width//2-intro_rect.width//2
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
        clock.tick(FPS)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Button:
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = pygame.font.Font(None, 50).render(buttonText, True, (20, 20, 20))
        button_objects.append(self)

    def process(self):
        self.buttonSurface.fill((255, 255, 255))
        mousePos = pygame.mouse.get_pos()
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
                self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
                self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
            ])
        screen.blit(self.buttonSurface, self.buttonRect)


def playfunc():
    global STARTGAME
    STARTGAME = True


if __name__ == '__main__':
    pygame.init()
    STARTGAME = False
    FPS = 60
    clock = pygame.time.Clock()
    width, height = 855, 480
    screen = pygame.display.set_mode((width, height))
    button_objects = []
    start_screen()

    print(100)
