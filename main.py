import pygame


def textname(screen):
    screen.fill((0, 0, 0))
    text = pygame.font.Font(None, 50).render("a game", True, (255, 255, 255))
    text_x, text_y = width // 2 - text.get_width() // 2, 80
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 0, 255), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)
    text = pygame.font.Font(None, 30).render("yeah, just a game (there soon will be buttons, nevermind)<3",
                                             True, (255, 255, 255))
    text_x, text_y = width // 2 - text.get_width() // 2, 130
    screen.blit(text, (text_x, text_y))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 700, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        textname(screen)
        clock.tick(10)
        pygame.display.flip()
    pygame.quit()
