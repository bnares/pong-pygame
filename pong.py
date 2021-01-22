import pygame, sys

pygame.init()

clock = pygame.time.Clock()

width = 700
height = 600

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill((0,0,0))
    pygame.display.update()
    clock.tick(60)