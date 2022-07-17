from pyclbr import Function
import pygame
from globalFunctions import click

#Initialize menu window
def menu_init(screen:any, screen_i):
        background_image = pygame.image.load("src/Menu/Images/Background.png").convert() 
        background_image = pygame.transform.scale(background_image, (screen_i[0][0], screen_i[0][1]))
        screen.blit(background_image,[0,0])
        pygame.display.flip()

def exit_game(mouse, screen_i):
    x_init = 430
    x_final = 985
    y_init = 812
    y_final = 912
    if (click(mouse, screen_i, x_init, x_final, y_init, y_final)):
        pygame.quit()