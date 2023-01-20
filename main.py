import random

import pygame
from random import randint, choice
import time
import sys
from tools import load_image


pygame.init()
width, height = 1070, 600
screen = pygame.display.set_mode((width, height))


class Playerstay(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, sprite_group, right=True):
        super().__init__(sprite_group)
        self.r = right
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

    def update_pos(self):
        if self.r:
            self.rect = self.rect.move(pl2_pos[0] - self.rect[0], pl2_pos[1] - self.rect[1])
        else:
            self.rect = self.rect.move(pl1_pos[0] - self.rect[0], pl1_pos[1] - self.rect[1])


class Playerrun(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, sprite_group, right=True):
        super().__init__(sprite_group)
        self.r = right
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.something = 1
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame * self.something]
        if self.something == 1:
            self.rect = self.rect.move(-30, 0)
            if self.r:
                pl2_pos[0] -= 30
            else:
                pl1_pos[0] += 30
        else:
            self.rect = self.rect.move(30, 0)
            if self.r:
                pl2_pos[0] += 30
            else:
                pl1_pos[0] -= 30

    def update_pos(self):
        if self.r:
            self.rect = self.rect.move(pl2_pos[0] - self.rect[0], pl2_pos[1] - self.rect[1])
        else:
            self.rect = self.rect.move(pl1_pos[0] - self.rect[0], pl1_pos[1] - self.rect[1])


class Playerjump(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, sprite_group, right=True):
        super().__init__(sprite_group)
        self.r = right
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        if right:
            self.r = right
            self.mask = pygame.mask.from_surface(self.frames[6])
        else:
            self.mask = pygame.mask.from_surface(self.frames[3])
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.is_jumping = False

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        x = 3
        y = 5
        if self.r:
            x = 6
            y = 10
        if self.cur_frame < x:
            self.rect = self.rect.move(0, -55)
        else:
            self.rect = self.rect.move(0, 45)
        if self.cur_frame == y:
            self.is_jumping = False

    def update_pos(self):
        if not self.is_jumping:
            if self.r:
                self.rect = self.rect.move(pl2_pos[0] - self.rect[0], pl2_pos[1] - self.rect[1])
            else:
                self.rect = self.rect.move(pl1_pos[0] - self.rect[0], pl1_pos[1] - self.rect[1])


class Playersit(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, sprite_group, right=True):
        super().__init__(sprite_group)
        self.r = right
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = -1
        self.is_sitting = False
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        x = 4
        if self.r:
            x = 5
        if self.cur_frame != x:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.is_sitting = True

    def update_pos(self):
        if self.r:
            self.rect = self.rect.move(pl2_pos[0] - self.rect[0], pl2_pos[1] - self.rect[1])
        else:
            self.rect = self.rect.move(pl1_pos[0] - self.rect[0], pl1_pos[1] - self.rect[1])


class Playerattack(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, sprite_group, right=True):
        super().__init__(sprite_group)
        self.r = right
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.is_attacking = False
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        x = 4
        if self.r:
            x = 10
        if self.cur_frame == x:
            self.is_attacking = False

    def update_pos(self):
        if self.r:
            self.rect = self.rect.move(pl2_pos[0] - self.rect[0], pl2_pos[1] - self.rect[1])
        else:
            self.rect = self.rect.move(pl1_pos[0] - self.rect[0], pl1_pos[1] - self.rect[1])


class Playerdeath(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, sprite_group, right=True):
        super().__init__(sprite_group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.is_right = right
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        if self.cur_frame != 5:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            if not self.is_right:
                self.rect = self.rect.move(-80, 0)
        self.image = self.frames[self.cur_frame]

    def update_pos(self):
        x = 0
        if self.is_right:
            x = 120
        self.rect = self.rect.move(pl1_pos[0] - self.rect[0] + x, pl1_pos[1] - self.rect[1])


class HPbar:
    def __init__(self, x, y, right=True):
        self.hp = 10
        self.x = x
        self.y = y
        self.is_right = right

    def render(self, screen):
        pygame.draw.rect(screen, pygame.Color('Grey'), (self.x, self.y, 680, 100), 5)
        pygame.draw.rect(screen, pygame.Color('Green'), (self.x + 5, self.y + 5, 670, 90))
        if self.hp < 0:
            self.hp = 0
        for i in range(10 - self.hp):
            if self.is_right:
                pygame.draw.rect(screen, pygame.Color('Red'), (self.x + 5 + i * 67, self.y + 5, 67, 90))
            else:
                pygame.draw.rect(screen, pygame.Color('Red'), ((self.x + 5 + 9 * 67) - i * 67,
                                                               self.y + 5, 67, 90))
        hp_font = pygame.font.Font(None, 100)
        hp_text = hp_font.render(f"100 / {self.hp * 10}", True, 'White')
        if self.is_right:
            hp_text = hp_font.render(f"{self.hp * 10} / 100", True, 'White')
        hp_text_x = self.x + 200
        hp_text_y = self.y + 20
        screen.blit(hp_text, (hp_text_x, hp_text_y))


class Blood(pygame.sprite.Sprite):
    fire = [load_image("blood.png", -1)]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites_blood)
        self.image = choice(self.fire)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = GRAVITY

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()


class HP10(pygame.sprite.Sprite):
    heart = load_image('10hp.png', -1)

    def __init__(self):
        super().__init__(all_sprites_heart)
        self.image = HP10.heart
        self.is_active = False
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = height


def create_particles(position, is_r=False):
    particle_count = 5
    x, y = -100, 5
    if is_r:
        x, y = -5, 100
    numbers = range(x, y)
    for _ in range(particle_count):
        Blood(position, choice(numbers), choice(numbers))


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
                  "(нажмите в любом месте окна для продолжения)", "", "",
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

    size = width, height = 1700, 800
    GRAVITY = 10
    screen_rect = (0, 0, width, height)
    screen = pygame.display.set_mode(size)
    all_sprites_stay2 = pygame.sprite.Group()
    all_sprites_run2 = pygame.sprite.Group()
    all_sprites_jump2 = pygame.sprite.Group()
    all_sprites_sit2 = pygame.sprite.Group()
    all_sprites_attack2 = pygame.sprite.Group()

    all_sprites_stay1 = pygame.sprite.Group()
    all_sprites_run1 = pygame.sprite.Group()
    all_sprites_jump1 = pygame.sprite.Group()
    all_sprites_sit1 = pygame.sprite.Group()
    all_sprites_attack1 = pygame.sprite.Group()

    all_sprites_blood = pygame.sprite.Group()

    all_sprites_heart = pygame.sprite.Group()

    all_sprites_cody_death = pygame.sprite.Group()
    all_sprites_akira_death = pygame.sprite.Group()

    pygame.display.set_caption('Name of game')
    num_fon = randint(1, 5)
    num_music = randint(1, 3)
    Cody_pain = pygame.mixer.Sound('data/pain2.mp3')
    Akira_pain = pygame.mixer.Sound('data/pain1.mp3')
    poof = pygame.mixer.Sound('data/poof.mp3')
    pygame.mixer.music.load(f'data/m{num_music}.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    image = pygame.transform.scale(load_image(f'fon{num_fon}.jpg'), (1700, 800))
    pl_stay2 = load_image('player_stay.png', -1)
    pl_run2 = load_image('player_run.png', -1)
    pl_jump2 = load_image('player_jump.png', -1)
    pl_sit2 = load_image('player_sit.png', -1)
    pl_at2 = load_image('player_attack.png', -1)
    pl_de2 = load_image('booom.png', -1)

    pl2_HPbar = HPbar(1000, 15)
    pl1_HPbar = HPbar(15, 15, False)
    hp10 = HP10()

    pl2_pos = [1300, 257]

    player_at2 = Playerattack(pl_at2, 11, 1, pl2_pos[0], pl2_pos[1], all_sprites_attack2)
    player_sit2 = Playersit(pl_sit2, 6, 1, pl2_pos[0], pl2_pos[1], all_sprites_sit2)
    player_ju2 = Playerjump(pl_jump2, 11, 1, pl2_pos[0], pl2_pos[1], all_sprites_jump2)
    player_st2 = Playerstay(pl_stay2, 10, 1, pl2_pos[0], pl2_pos[1], all_sprites_stay2)
    player_ru2 = Playerrun(pl_run2, 11, 1, pl2_pos[0], pl2_pos[1], all_sprites_run2)
    player_de2 = Playerdeath(pl_de2, 3, 2, pl2_pos[0], pl2_pos[1], all_sprites_akira_death)

    pl1_pos = [100, 300]

    pl_stay1 = load_image('player1_stay.png', -1)
    pl_run1 = load_image('player1_run.png', -1)
    pl_at1 = load_image('player1_attack.png', -1)
    pl_sit1 = load_image('player1_sit.png', -1)
    pl_jump1 = load_image('player1_jump.png', -1)
    pl1_death = load_image('cody_death.png', -1)

    player_de1 = Playerdeath(pl1_death, 6, 1, pl1_pos[0], pl1_pos[1], all_sprites_cody_death, False)
    player_ju1 = Playerjump(pl_jump1, 6, 1, pl1_pos[0], pl1_pos[1], all_sprites_jump1, False)
    player_sit1 = Playersit(pl_sit1, 5, 1, pl1_pos[0], pl1_pos[1], all_sprites_sit1, False)
    player_at1 = Playerattack(pl_at1, 5, 1, pl1_pos[0], pl1_pos[1], all_sprites_attack1, False)
    player_st1 = Playerstay(pl_stay1, 2, 1, pl1_pos[0], pl1_pos[1], all_sprites_stay1, False)
    player_ru1 = Playerrun(pl_run1, 8, 1, pl1_pos[0], pl1_pos[1], all_sprites_run1, False)

    timer = 100
    time = 0
    counter = 10
    is_pause = False

    font = pygame.font.Font(None, 150)
    font1 = pygame.font.Font(None, 100)
    name = font1.render('Akira', True, 'White')
    name1 = font1.render('Cody', True, 'White')
    text_x = 715
    text_y = 20
    safe_zone = 230
    fps = 9

    Cody_is_win = False
    Akira_is_win = False

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            is_pause = not is_pause
        if is_pause:
            screen.fill('black')
        else:
            screen.blit(image, (0, 0))
        txt1 = time // 1000 // 60
        if txt1 < 10:
            txt1 = '0' + str(txt1)
        txt2 = time // 1000 % 60
        if txt2 < 10:
            txt2 = '0' + str(txt2)
        text = font.render(f'{txt1}:{txt2}', True, (255, 200, 0))  # <---- итоговое время можно взять отсюда
        screen.blit(text, (text_x, text_y))
        screen.blit(name1, (15, 115))
        screen.blit(name, (1500, 115))
        pl1_HPbar.render(screen)
        pl2_HPbar.render(screen)
        if timer > 0:
            timer -= 1
        elif not hp10.is_active:
            hp10.is_active = True
            hp10.rect = (random.randint(0, 1000), 160)
        keys = pygame.key.get_pressed()
        if Cody_is_win:
            all_sprites_stay1.draw(screen)
            player_st1.update()
            if player_de2.cur_frame != 5:
                all_sprites_akira_death.draw(screen)
                player_de2.update()
            elif counter == 0:
                break
            counter -= 1
        elif Akira_is_win:
            all_sprites_stay2.draw(screen)
            player_st2.update()
            all_sprites_cody_death.draw(screen)
            player_de1.update()
            counter -= 1
            if counter == 0:
                break
        else:
            if (keys[pygame.K_UP] or player_ju2.is_jumping) and not player_at2.is_attacking:
                player_sit1.is_sitting = False
                player_ju2.is_jumping = True
                player_ju2.update()
                all_sprites_jump2.draw(screen)
                if pygame.sprite.collide_mask(player_ju2, hp10) and hp10.is_active and pl2_HPbar.hp < 10:
                    hp10.is_active = False
                    pl2_HPbar.hp += 1
                    timer = 100
            elif keys[pygame.K_RCTRL] or player_at2.is_attacking:
                player_sit2.is_sitting = False
                player_at2.is_attacking = True
                all_sprites_attack2.draw(screen)
                player_at2.update()
                if abs(pl1_pos[0] - pl2_pos[0]) < safe_zone + 25 and player_at2.cur_frame == 6 \
                        and not player_sit1.is_sitting:
                    Cody_pain.play()
                    create_particles((pl1_pos[0] + 100, pl1_pos[1] + 80), is_r=True)
                    pl1_HPbar.hp -= 1
                    if pl1_HPbar.hp == 0:
                        Akira_is_win = True
                        fps = 7
            elif keys[pygame.K_RIGHT] and pl2_pos[0] < 1450:
                player_sit2.is_sitting = False
                player_ru2.something = -1
                player_sit2.cur_frame = 0
                all_sprites_run2.draw(screen)
                player_ru2.update()
            elif keys[pygame.K_DOWN]:
                player_sit2.update()
                all_sprites_sit2.draw(screen)
            elif keys[pygame.K_LEFT] and 0 < pl1_pos[0] and abs(pl1_pos[0] - pl2_pos[0]) > safe_zone:
                player_sit2.is_sitting = False
                player_ru2.something = 1
                player_sit2.cur_frame = 0
                all_sprites_run2.draw(screen)
                player_ru2.update()
            else:
                player_sit2.is_sitting = False
                player_sit2.cur_frame = 0
                all_sprites_stay2.draw(screen)
                player_st2.update()
            player_at2.update_pos()
            player_ru2.update_pos()
            player_ju2.update_pos()
            player_sit2.update_pos()
            player_st2.update_pos()
            player_de2.update_pos()
            if (keys[pygame.K_w] or player_ju1.is_jumping) and not player_at1.is_attacking:
                player_sit1.is_sitting = False
                player_ju1.is_jumping = True
                player_ju1.update()
                all_sprites_jump1.draw(screen)
                if pygame.sprite.collide_mask(player_ju1, hp10) and hp10.is_active and pl1_HPbar.hp < 10:
                    hp10.is_active = False
                    pl1_HPbar.hp += 1
                    timer = 100
            elif keys[pygame.K_LALT] or player_at1.is_attacking:
                player_sit1.is_sitting = False
                player_sit1.cur_frame = 0
                player_at1.is_attacking = True
                player_at1.update()
                all_sprites_attack1.draw(screen)
                if abs(pl1_pos[0] - pl2_pos[0]) < safe_zone + 25 and player_at1.cur_frame == 4 \
                        and not player_sit2.is_sitting:
                    Akira_pain.play()
                    create_particles((pl1_pos[0] + 220, pl1_pos[1] + 80))
                    pl2_HPbar.hp -= 1
                    if pl2_HPbar.hp == 0:
                        poof.play()
                        Cody_is_win = True
            elif keys[pygame.K_d] and pl1_pos[0] < 1450 and abs(pl1_pos[0] - pl2_pos[0]) > safe_zone:
                player_sit2.cur_frame = 0
                player_ru1.something = 1
                player_sit2.cur_frame = 0
                all_sprites_run1.draw(screen)
                player_ru1.update()
            elif keys[pygame.K_s]:
                player_sit1.is_sitting = False
                player_sit1.update()
                all_sprites_sit1.draw(screen)
            elif keys[pygame.K_a] and 0 < pl1_pos[0]:
                player_sit1.is_sitting = False
                player_sit2.cur_frame = 0
                player_ru1.something = -1
                player_sit2.cur_frame = 0
                all_sprites_run1.draw(screen)
                player_ru1.update()
            else:
                player_sit1.is_sitting = False
                player_sit1.cur_frame = 0
                all_sprites_stay1.draw(screen)
                player_st1.update()
            player_de1.update_pos()
            player_ju1.update_pos()
            player_ru1.update_pos()
            player_st1.update_pos()
            player_at1.update_pos()
            player_sit1.update_pos()
            if hp10.is_active:
                all_sprites_heart.draw(screen)
            time += clock.get_time()
        all_sprites_blood.update()
        all_sprites_blood.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
