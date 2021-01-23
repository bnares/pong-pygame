import pygame, sys
import random

pygame.init()

clock = pygame.time.Clock()

#setting up the main window
width = 700
height = 600

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong")

bg_color = pygame.Color("grey12")

#basic values

ballSpeedX = 7
ballSpeedY = 7
playerSpeed = 0
playerScore = 0
oponentScore =0

#game rectangles
ball = pygame.Rect(width/2 - 15, height/2 -15,30,30)
player = pygame.Rect(width-20, height/2 - 70,10,140)
oponent = pygame.Rect(10, height/2-70,10,140)


def displayResult():
    game_font = pygame.font.Font("freesansbold.ttf",32)
    playerText = game_font.render(f"{oponentScore} : {playerScore}", True, (200,200,200))
    screen.blit(playerText, (width/2-33, height/2))

def playerAnimation():
    player.y+=playerSpeed
    if player.top <=0:
        player.top =0
    if player.bottom >= height:
        player.bottom = height


def oponentAnimation():
    if oponent.top < ball.y:
        oponent.y +=7
    if oponent.bottom > ball.y:
        oponent.y -=7

    if oponent.top<=0:
        oponent.y =0

    if oponent.bottom >= height:
        oponent.y = height


def ballRestart():
    global ballSpeedX, ballSpeedY, scoreTimer

    currentTime = pygame.time.get_ticks()
    ball.center = (width / 2, height / 2)

    if currentTime - scoreTimer < 2100:
        ballSpeedX, ballSpeedY = 0,0

    else:
        ballSpeedY = 7 * random.choice((1, -1))
        ballSpeedX = 7 * random.choice((1, -1))
        scoreTimer = None









def drawRectangles():

        mylist = [ball, player, oponent]
        for i in mylist:
            pygame.draw.rect(screen, (200,200,200), i)


def ballSpeed():
    global  oponentScore, playerScore, scoreTimer
    global ballSpeedX, ballSpeedY
    if ball.x >= width or ball.x <=0:
        if ball.x >=width:
           oponentScore+=1
           scoreTimer = pygame.time.get_ticks()
        if ball.x <=0:
            playerScore+=1
            scoreTimer = pygame.time.get_ticks()
        #ballSpeedX *=-1
        #ballRestart()

    if ball.y>=height or ball.y <=0:
        ballSpeedY *=-1

    ball.left += ballSpeedX
    ball.top += ballSpeedY


def checkCollision():
    global ballSpeedX
    if ball.colliderect(player) or ball.colliderect(oponent):
        ballSpeedX *=-1
        print("ball hit the front of the desk")


#score timer

scoreTimer = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerSpeed=7

            if event.key == pygame.K_UP:
                playerSpeed = -7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerSpeed=0

            if event.key == pygame.K_UP:
                playerSpeed = 0



    screen.fill(bg_color)
    drawRectangles()
    ballSpeed()
    checkCollision()
    playerAnimation()
    if scoreTimer:
        ballRestart()
    oponentAnimation()
    pygame.draw.aaline(screen, (200,200,200), (width/2, 0), (width/2, height))
    displayResult()
    pygame.display.update()
    clock.tick(60)