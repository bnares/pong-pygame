import pygame, sys

pygame.init()

clock = pygame.time.Clock()

#setting up the main window
width = 700
height = 600

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong")

bg_color = pygame.Color("grey12")

#game rectangles

ball = pygame.Rect(width/2 - 15, height/2 -15,30,30)
player = pygame.Rect(width-20, height/2 - 70,10,140)
oponent = pygame.Rect(10, height/2-70,10,140)


def drawRectangles():

        mylist = [ball, player, oponent]
        for i in mylist:
            pygame.draw.rect(screen, (200,200,200), i)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    screen.fill(bg_color)
    drawRectangles()
    pygame.display.update()
    clock.tick(60)