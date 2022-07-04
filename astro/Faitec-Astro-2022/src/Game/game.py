import pygame
import random
from globalFunctions import click

'''
#Initialize menu window
def menu_init(screen:any, screen_i):
        background_image = pygame.image.load("src/Menu/Images/Background.png").convert() 
        background_image = pygame.transform.scale(background_image, (screen_i[0][0], screen_i[0][1]))
        screen.blit(background_image,[0,0])
        pygame.display.flip()
'''

window_width = 1440  # 1240
window_height = 1024
pos_nave_x = 570
pos_missil_x = 620
pos_sol_x = 50
pos_saturno_x = 396
pos_lua_x = 742
pos_p_terra_x = 1090
pos_nave_y = 700
pos_alvo_y = 50
vel_x = 0.4

'''gameplay_bg = pygame.image.load(
    "src\Game\gameplay\gameplay_bg.png").convert()
gameplay_bg = pygame.transform.scale(gameplay_bg, (1440, 1024))'''

sol = pygame.image.load("src\Game\gameplay\sol.png")
sol = pygame.transform.scale(sol, (100, 100))

saturno = pygame.image.load("src\Game\gameplay\saturno.png")
saturno = pygame.transform.scale(saturno, (100, 100))

lua = pygame.image.load("src\Game\gameplay\lua.png")
lua = pygame.transform.scale(lua, (100, 100))

p_terra = pygame.image.load("src\Game\gameplay\p_terra.png")
p_terra = pygame.transform.scale(p_terra, (100, 100))

nave = pygame.image.load("src\Game\gameplay\espaconave.png")
nave = pygame.transform.scale(nave, (150, 150))

missil = pygame.image.load("src\Game\gameplay\missil.png")
missil = pygame.transform.scale(missil, (60, 60))

# def initialize button button menu


def init_game(screen, mouse, screen_i):
    x_init = 430
    x_final = 985
    y_init = 514
    y_final = 617
    if (click(mouse, screen_i, x_init, x_final, y_init, y_final)):
        loading_game(screen, screen_i)
        game_loop(screen, screen_i)


def loading_game(screen: any, screen_i):
    i = 0
    while i < 4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if i == 0:
            image_path = "src\Game\Images\Loading\Loading_3.png"
        elif i == 1:
            image_path = "src\Game\Images\Loading\Loading_2.png"
        elif i == 2:
            image_path = "src\Game\Images\Loading\Loading_1.png"
        else:
            image_path = "src\Game\Images\Loading\Loading_GO.png"

        background_image = pygame.image.load(image_path).convert()
        background_image = pygame.transform.scale(
            background_image, (screen_i[0][0], screen_i[0][1]))
        screen.blit(background_image, [0, 0])
        pygame.display.flip()
        pygame.time.delay(1000)
        i = i+1


def game_loop(screen: any, screen_i):
    vel_x = 5
    pos_nave_x = 570
    pos_missil_x = 620
    gameplay_bg = pygame.image.load(
        "src\Game\gameplay\gameplay_bg.png").convert()
    gameplay_bg = pygame.transform.scale(
        gameplay_bg, (screen_i[0][0], screen_i[0][1]))
    # pygame.init()
    #pygame.display.set_mode([1440, 1024])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    pygame.quit()
        screen.blit(gameplay_bg, [0, 0])
        screen.blit(nave, (pos_nave_x, pos_nave_y))
        screen.blit(missil, (pos_missil_x, pos_nave_y))
        screen.blit(sol, (pos_sol_x, pos_alvo_y))
        screen.blit(saturno, (pos_saturno_x, pos_alvo_y))
        screen.blit(lua, (pos_lua_x, pos_alvo_y))
        screen.blit(p_terra, (pos_p_terra_x, pos_alvo_y))

        # Movimentação da nave
        pos_nave_x = pos_nave_x + vel_x
        pos_missil_x = pos_missil_x + vel_x
        if (pos_nave_x + 150) > 1240:
            vel_x -= 5

        if (pos_nave_x) < 0:
            vel_x += 5

        pygame.display.update()
    pygame.quit()
