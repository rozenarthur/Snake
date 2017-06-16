import pygame
import time
import random
from Colors import *

pygame.init()

displayWidth = 800
displayHeight = 600

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

pygame.display.set_caption("Slytherin'")



clock = pygame.time.Clock()
fps = 30

font = pygame.font.SysFont(None, 25)

def msg_to_scrn(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [displayWidth/2, displayHeight/2])


blockSize = 10  # size of each square of the snake

# **Logical Game loop that runs the controls and changes of your game**
def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = displayWidth / 2
    lead_y = displayHeight / 2

    lead_x_change = 0
    lead_y_change = 0

    randAppleX = round(random.randrange(0, displayWidth-blockSize)/10.0) * 10.0 # so apple not offscreen and only appears in multiples of 10
    randAppleY = round(random.randrange(0, displayHeight-blockSize)/10.0) * 10.0 # so apple not offscreen and only appears in multiples of 10

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            msg_to_scrn("Game Over, Press c to play Again! or q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
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

                elif event.key == pygame.K_RIGHT:  # if the right arrow was clicked
                    lead_x_change = blockSize
                    lead_y_change = 0 # avoids diagonal movement

                elif event.key == pygame.K_UP:  # if the up arrow was clicked
                    lead_y_change = -blockSize
                    lead_x_change = 0 # avoids diagonal movement

                elif event.key == pygame.K_DOWN:  # if the down arrow was clicked
                    lead_y_change = blockSize
                    lead_x_change = 0 # avoids diagonal movement

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
        pygame.draw.rect(gameDisplay, blue, [lead_x, lead_y, blockSize, blockSize])
        pygame.display.update()


        #Snake is in the same position as the apple (eats apple)
        if lead_x == randAppleX and lead_y == randAppleY:
            print ("eat")

        clock.tick(fps)  # frames per second

    pygame.quit()
    quit()

gameLoop()