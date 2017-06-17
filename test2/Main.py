import pygame
import time
import random
from Colors import *

pygame.init()

displayWidth = 800
displayHeight = 600

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

pygame.display.set_caption("Slytherin'")

img = pygame.image.load('head.png')

clock = pygame.time.Clock()
fps = 25

direction = "right"
font = pygame.font.SysFont(None, 25)

#modify the snake character, i.e. make him bigger when he eats an apple
def snake(blockSize, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)


    gameDisplay.blit(head, (snakelist[-1][0],snakelist[-1][1]))

    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, blue, [XnY[0], XnY[1], blockSize, blockSize])

def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def msg_to_scrn(msg, color):

    # screen_text = font.render(msg, True, color)
    # gameDisplay.blit(screen_text, [displayWidth/2, displayHeight/2])
    textSurf, textRect = text_objects(msg, color)
    textRect.center = (displayWidth/2), (displayHeight/2)
    gameDisplay.blit(textSurf, textRect)


blockSize = 20  # size of each square of the snake

# **Logical Game loop that runs the controls and changes of your game**
def gameLoop():
    global direction
    gameExit = False
    gameOver = False

    lead_x = displayWidth / 2
    lead_y = displayHeight / 2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, displayWidth-blockSize))#/10.0) * 10.0 # so apple not offscreen and only appears in multiples of 10
    randAppleY = round(random.randrange(0, displayHeight-blockSize))#/10.0) * 10.0 # so apple not offscreen and only appears in multiples of 10

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            msg_to_scrn("Game Over, Press c to play Again! or q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if the event is a quit event
                gameExit = True
            if event.type == pygame.KEYDOWN:  # if the keyboard was clicked
                if event.key == pygame.K_LEFT:  # if the left arrow was clicked
                    lead_x_change = -blockSize
                    lead_y_change = 0  # avoids diagonal movement
                    direction = "left"

                elif event.key == pygame.K_RIGHT:  # if the right arrow was clicked
                    lead_x_change = blockSize
                    lead_y_change = 0 # avoids diagonal movement
                    direction = "right"

                elif event.key == pygame.K_UP:  # if the up arrow was clicked
                    lead_y_change = -blockSize
                    lead_x_change = 0 # avoids diagonal movement
                    direction = "up"

                elif event.key == pygame.K_DOWN:  # if the down arrow was clicked
                    lead_y_change = blockSize
                    lead_x_change = 0 # avoids diagonal movement
                    direction = "down"

            #  **Stops Movements when the button click is over (EVENT KEYUP), THIS IS AN EXAMPLE, NOT USEFUL FOR SNAKE GAME**
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         lead_x_change = 0

            # game over if snake passes the window of the screen
            if lead_x >= displayWidth or lead_x < 0 or lead_y < 0 or lead_y >= displayHeight:
                gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        # gameDisplay.fill(red, rect=[200, 200, 50, 50])
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, blockSize, blockSize])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        # check if the snake ran into itself, check all coordinates except the last one (snake head)
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(blockSize, snakeList)
        pygame.display.update()

    #Snake intersects the apple in any way even slightly for any apple size, much more accurate than previous if statement
        # if lead_x >= randAppleX and lead_x <= randAppleX + blockSize:
        #     if lead_y >= randAppleY and lead_y <= randAppleY + blockSize:
        #
        #         randAppleX = round(random.randrange(0,displayWidth - blockSize))# / 10.0) * 10.0  # so apple not offscreen and only appears in multiples of 10
        #         randAppleY = round(random.randrange(0,displayHeight - blockSize))# / 10.0) * 10.0  # so apple not offscreen and only appears in multiples of 10
        #
        #         snakeLength += 1

        if lead_x >= randAppleX and lead_x <= randAppleX + blockSize or lead_x + blockSize >= randAppleX and lead_x + blockSize <= randAppleX + blockSize:
            if lead_y >= randAppleY and lead_y <=randAppleY + blockSize or lead_y + blockSize >= randAppleY and lead_y + blockSize <= randAppleY + blockSize:

                randAppleX = round(random.randrange(0,displayWidth - blockSize))  # / 10.0) * 10.0  # so apple not offscreen and only appears in multiples of 10
                randAppleY = round(random.randrange(0,displayHeight - blockSize))# / 10.0) * 10.0  # so apple not offscreen and only appears in multiples of 10
                snakeLength += 1

        clock.tick(fps)  # frames per second

    pygame.quit()
    quit()

gameLoop()