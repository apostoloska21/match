import pygame

pygame.init()

# screen setup
WIDTH = 600
HEIGHT = 600

white = (255, 255, 255)
black = (0, 0, 0)
green = (65, 216, 97)
fps = 60
timer = pygame.time.Clock()

# creating the screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("The Matching Game")


def draw_backgrounds():
    top_menu = pygame.draw.rect(screen, black, [0, 0, WIDTH, 100])
    board_space = pygame.draw.rect(screen, green, [0, 100, WIDTH, HEIGHT - 200])
    bottom_menu = pygame.draw.rect(screen, black, [0, HEIGHT - 100, WIDTH, 100])


# while the game is running
running = True
while running:
    timer.tick(fps)
    screen.fill(white)
    draw_backgrounds()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()
