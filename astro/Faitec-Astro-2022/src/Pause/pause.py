import pygame
from globalFunctions import click


def pauseGame(screen: any, mouse: any, font, screen_i):
    x_init = 430
    x_final = 985
    y_init = 664
    y_final = 768
    if (click(mouse, screen_i, x_init, x_final, y_init, y_final)):
        pauseScreen(screen, mouse, font, screen_i)

#################################################################


def pauseScreen(screen: any, mouse: any, font: any, screen_i):
    stopWhile = True
    while(stopWhile):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = event.pos
                tutorialButton(mouse, screen_i)
                musicButton(mouse, screen_i)
                Creditos(mouse, screen_i)
                stopWhile = returnButton(mouse, screen_i)
        image_path = "src\Pause\Images\Background.png"
        background_image = pygame.image.load(image_path).convert()
        background_image = pygame.transform.scale(
            background_image, (screen_i[0][0], screen_i[0][1]))
        screen.blit(background_image, [0, 0])

        text(screen, font, "on", [500, 500])

        pygame.display.flip()

#################################################################


def tutorialButton(mouse, screen_i):
    x_init = 439
    x_final = 1010
    y_init = 217
    y_final = 335
    if (click(mouse, screen_i, x_init, x_final, y_init, y_final)):
        print("tutorial")


def musicButton(mouse, screen_i):
    x_init = 439
    x_final = 1010
    y_init = 360
    y_final = 475
    if (click(mouse, screen_i, x_init, x_final, y_init, y_final)):
        print("music")


def returnButton(mouse, screen_i):
    x_init = 1062
    x_final = 1397
    y_init = 36
    y_final = 100
    if (click(mouse, screen_i, x_init, x_final, y_init, y_final)):
        return False
    else:
        return True


def Creditos(mouse, screen_i):
    x_init = 439
    x_final = 1010
    y_init = 680
    y_final = 804
    if (click(mouse, screen_i, x_init, x_final, y_init, y_final)):
        print("creditos")


def text(screen, font, text, position):
    text = font.render(text, True, (250, 250, 250))
    screen.blit(text, (position[0], position[1]))
