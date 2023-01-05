import pygame
from random import randint
from tools import load_image


pygame.init()
size = width, height = 1700, 800
screen = pygame.display.set_mode(size)
all_sprites_stay2 = pygame.sprite.Group()
all_sprites_run2 = pygame.sprite.Group()
all_sprites_jump2 = pygame.sprite.Group()
all_sprites_sit2 = pygame.sprite.Group()
all_sprites_attack2 = pygame.sprite.Group()


class Playerstay(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites_stay2)
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
        self.rect = self.rect.move(pl2_pos[0] - self.rect[0], pl2_pos[1] - self.rect[1])


class Playerrun(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites_run2)
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
            pl2_pos[0] -= 30
        else:
            self.rect = self.rect.move(30, 0)
            pl2_pos[0] += 30

    def update_pos(self):
        self.rect = self.rect.move(pl2_pos[0] - self.rect[0], pl2_pos[1] - self.rect[1])


class Playerjump(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites_jump2)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
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
        if self.cur_frame < 6:
            self.rect = self.rect.move(0, -55)
        else:
            self.rect = self.rect.move(0, 45)
        if self.cur_frame == 10:
            self.is_jumping = False

    def update_pos(self):
        if not self.is_jumping:
            self.rect = self.rect.move(pl2_pos[0] - self.rect[0], pl2_pos[1] - self.rect[1])


class Playersit(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites_sit2)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = -1
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.flag = True

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
            self.image = self.frames[self.cur_frame]

    def update_pos(self):
        self.rect = self.rect.move(pl2_pos[0] - self.rect[0], pl2_pos[1] - self.rect[1])


class Playerattack(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites_attack2)
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
        if self.cur_frame == 10:
            self.is_attacking = False

    def update_pos(self):
        self.rect = self.rect.move(pl2_pos[0] - self.rect[0], pl2_pos[1] - self.rect[1])


class HPbar:
    def __init__(self, x, y, right=True):
        self.hp = 10
        self.x = x
        self.y = y
        self.is_right = right

    def render(self, screen):
        pygame.draw.rect(screen, pygame.Color('Grey'), (self.x, self.y, 730, 100), 5)
        pygame.draw.rect(screen, pygame.Color('Green'), (self.x + 5, self.y + 5, 720, 90))
        if self.hp < 0:
            self.hp = 0
        for i in range(10 - self.hp):
            if self.is_right:
                pygame.draw.rect(screen, pygame.Color('Red'), (self.x + 5 + i * 72, self.y + 5, 72, 90))
            else:
                pygame.draw.rect(screen, pygame.Color('Red'), ((self.x + 5 + 9 * 72) - i * 72,
                                                               self.y + 5, 72, 90))


if __name__ == '__main__':
    num = randint(1, 5)
    image = pygame.transform.scale(load_image(f'fon{num}.jpg'), (1700, 800))
    pl_stay2 = load_image('player_stay.png', -1)
    pl_run2 = load_image('player_run.png', -1)
    pl_jump2 = load_image('player_jump.png', -1)
    pl_sit2 = load_image('player_sit.png', -1)
    pl_at2 = load_image('player_attack.png', -1)
    pl2_HPbar = HPbar(950, 15)
    pl1_HPbar = HPbar(15, 15, False)
    pl2_pos = [1300, 270]
    player_at2 = Playerattack(pl_at2, 11, 1, pl2_pos[0], pl2_pos[1])
    player_sit2 = Playersit(pl_sit2, 6, 1, pl2_pos[0], pl2_pos[1])
    player_ju2 = Playerjump(pl_jump2, 11, 1, pl2_pos[0], pl2_pos[1])
    player_st2 = Playerstay(pl_stay2, 10, 1, pl2_pos[0], pl2_pos[1])
    player_ru2 = Playerrun(pl_run2, 11, 1, pl2_pos[0], pl2_pos[1])
    clock = pygame.time.Clock()
    fps = 8

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(image, (0, 0))
        pl1_HPbar.render(screen)
        pl2_HPbar.render(screen)
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP] or player_ju2.is_jumping) and not player_at2.is_attacking:
            player_ju2.is_jumping = True
            player_ju2.update()
            all_sprites_jump2.draw(screen)
        elif keys[pygame.K_RALT] or player_at2.is_attacking:
            player_at2.is_attacking = True
            all_sprites_attack2.draw(screen)
            player_at2.update()
        elif keys[pygame.K_RIGHT]:
            player_ru2.something = -1
            player_sit2.cur_frame = 0
            all_sprites_run2.draw(screen)
            player_ru2.update()
        elif keys[pygame.K_DOWN]:
            player_sit2.update()
            all_sprites_sit2.draw(screen)
        elif keys[pygame.K_LEFT]:
            player_ru2.something = 1
            player_sit2.cur_frame = 0
            all_sprites_run2.draw(screen)
            player_ru2.update()
        elif keys[pygame.K_LALT]:
            pl1_HPbar.hp -= 1
        else:
            player_sit2.cur_frame = 0
            all_sprites_stay2.draw(screen)
            player_st2.update()
        player_at2.update_pos()
        player_ru2.update_pos()
        player_ju2.update_pos()
        player_sit2.update_pos()
        player_st2.update_pos()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


