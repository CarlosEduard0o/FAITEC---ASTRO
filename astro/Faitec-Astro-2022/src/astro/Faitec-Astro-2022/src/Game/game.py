import pygame
import random
from globalFunctions import click
from Pause.pause import pauseGame
from Menu.menu import menu_init, exit_game

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
        background_image = pygame.transform.scale(background_image, (screen_i[0][0], screen_i[0][1]))
        screen.blit(background_image, [0, 0])
        pygame.display.flip()
        pygame.time.delay(1000)
        i = i+1


def game_loop(screen: any, screen_i):
    # Posicionamento dos elementos
    pos_nave_x = 570
    pos_missil_x = 626
    pos_sol_x = 50
    pos_saturno_x = 396
    pos_lua_x = 742
    pos_p_terra_x = 1090
    pos_nave_y = 700
    pos_missil_y = pos_nave_y
    pos_alvo_y = 50
    triggered = False

    # Fonte

    font_op = pygame.font.SysFont("src\Game\letras\PixelGameFont.ttf", 40)
    font_pause = pygame.font.SysFont("src\Game\letras\PixelGameFont.ttf", 200)
    font_score = pygame.font.SysFont("src\Game\letras\PixelGameFont.ttf", 40)
    calvo_sort = pygame.font.SysFont("src\Game\letras\PixelGameFont.ttf", 40)

    # Velocidade da locomoção da nave e míssil pelo eixo x
    vel_x = 1  # Nave
    aumento_vel_x = vel_x
    vel_missil_x = 1  # Missil
    aumento_vel_missil_x = vel_missil_x

    # Velocidade do tiro
    vel_missil_y = 5

    # Imagens
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

    # Background da gameplay
    gameplay_bg = pygame.image.load("src\Game\gameplay\gameplay_bg.png").convert()
    gameplay_bg = pygame.transform.scale(gameplay_bg, (screen_i[0][0], screen_i[0][1]))

    sol_rect = sol.get_rect()
    saturno_rect = saturno.get_rect()
    lua_rect = lua.get_rect()
    p_terra_rect = p_terra.get_rect()
    missil_rect = missil.get_rect()

    # Função para o missil dar respawn
    def respawn_missil():
        triggered = False
        respawn_missil_x = pos_nave_x + 57
        respawn_missil_y = pos_nave_y
        vel_missil_y = 5
        return [respawn_missil_x, respawn_missil_y, triggered, vel_missil_y]

    # Alvo

    def arm_alvo():
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 2)
        sorteio = random.randint(1, 4)

        if c == 1:
            op = "+"
            res = a + b

        elif c == 2:
            op = "-"
            res = a - b

        if sorteio == 1:
            alvo_sort = [sol_rect, "sol", res, saturno_rect, "saturno", (res - b), lua_rect, "lua", (res + a), p_terra_rect, "p_terra", (res - c)]
        elif sorteio == 2:
            alvo_sort = [saturno_rect, "saturno", res, sol_rect, "sol", (res + c), p_terra_rect, "p_terra", (res - a), lua_rect, "lua", (res + b)]
        elif sorteio == 3:
            alvo_sort = [lua_rect, "lua", res, p_terra_rect, "p_terra", (res - c), saturno_rect, "saturno", (res + a), sol_rect, "sol", (res - b)]
        elif sorteio == 4:
            alvo_sort = [p_terra_rect, "p_terra", res, saturno_rect, "saturno", (res + b), lua_rect, "lua", (res - a), sol_rect, "sol", (res + b)]

        return(a, b, sorteio, op, alvo_sort)

    a, b, sorteio, op, alvo_sort = arm_alvo()

    rodando = 0
    pausado = 1
    jogo = rodando
    pontos = 5

    # Loop da gameplay
    while True:
        # Captura dos eventos do PYGAME
        for event in pygame.event.get():
            # KEYDOWN
            if event.type == pygame.KEYDOWN:
                # Se pressionar BACKSPACE o game fecha
                if event.key == pygame.K_BACKSPACE:
                    pygame.quit()
                # Se pressionar ESPAÇO dispara o míssil
                elif event.key == pygame.K_SPACE:
                    triggered = True
                elif event.key == pygame.K_p:
                    if jogo != pausado:
                        jogo = pausado
                    else:
                        jogo = rodando
        if jogo == pausado:
            pause = font_pause.render(f' PAUSADO ', True, (255, 255, 0))
            screen.blit(pause, (390, 250))
            pygame.mouse.set_visible(True)
            pygame.display.flip()
            continue

        # Imagens
        screen.blit(gameplay_bg, [0, 0])
        screen.blit(missil, (pos_missil_x, pos_missil_y))
        screen.blit(nave, (pos_nave_x, pos_nave_y))
        screen.blit(sol, (pos_sol_x, pos_alvo_y))
        screen.blit(saturno, (pos_saturno_x, pos_alvo_y))
        screen.blit(lua, (pos_lua_x, pos_alvo_y))
        screen.blit(p_terra, (pos_p_terra_x, pos_alvo_y))

        # Colisão
        pygame.draw.rect(screen, (255, 0, 0), sol_rect, 4)
        pygame.draw.rect(screen, (255, 0, 0), saturno_rect, 4)
        pygame.draw.rect(screen, (255, 0, 0), lua_rect, 4)
        pygame.draw.rect(screen, (255, 0, 0), p_terra_rect, 4)
        pygame.draw.rect(screen, (255, 0, 0), missil_rect, 4)

        # Disparo e respawn do míssil
        if triggered == False:
            pos_missil_x = pos_missil_x + vel_missil_x
        if triggered == True:
            pos_missil_y = pos_missil_y - vel_missil_y
            if pos_missil_y < 0:
                pos_missil_x, pos_missil_y, triggered, vel_missil_y = respawn_missil()
            if missil_rect.colliderect(alvo_sort[0]):
                a, b, sorteio, op, alvo_sort = arm_alvo()
                pos_missil_x, pos_missil_y, triggered, vel_missil_y = respawn_missil()
                pontos += 1
                aumento_vel_x += 0.2
                aumento_vel_missil_x += 0.2
                # Progredir com a velocidade conforme vai acertando
            elif (missil_rect.colliderect(alvo_sort[3])) or (missil_rect.colliderect(alvo_sort[6])) or (missil_rect.colliderect(alvo_sort[9])):
                a, b, sorteio, op, alvo_sort = arm_alvo()
                pos_missil_x, pos_missil_y, triggered, vel_missil_y = respawn_missil()
                pontos -= 1
                # Colocar aqui a derrota      

        # Movimentação da nave e do míssil pelo eixo x
        pos_nave_x = pos_nave_x + vel_x
        if (pos_nave_x + 150) > 1240:
            vel_x -= aumento_vel_x
            vel_missil_x -= aumento_vel_missil_x

        if (pos_nave_x) < 0:
            vel_x += aumento_vel_x
            vel_missil_x += aumento_vel_missil_x

        # Posição do rect
        sol_rect.x = pos_sol_x
        sol_rect.y = pos_alvo_y
        saturno_rect.x = pos_saturno_x
        saturno_rect.y = pos_alvo_y
        lua_rect.x = pos_lua_x
        lua_rect.y = pos_alvo_y
        p_terra_rect.x = pos_p_terra_x
        p_terra_rect.y = pos_alvo_y
        missil_rect.x = pos_missil_x
        missil_rect.y = pos_missil_y

        # Score

        opera = font_op.render(f' Operação: {int(a)} {op} {int(b)} = ?', True, (255, 255, 0))
        screen.blit(opera, (1210, 50))

        if sorteio == 1:
            calvo_sort = font_op.render(f'{alvo_sort[7]} : {alvo_sort[8]}', True, (255, 255, 0))
            screen.blit(calvo_sort, (1210, 250))
            calvo_sort = font_op.render(f'{alvo_sort[4]} : {alvo_sort[5]}', True, (255, 255, 0))
            screen.blit(calvo_sort, (1210, 200))
            calvo_sort = font_op.render(f'{alvo_sort[1]} : {alvo_sort [2]}', True, (255, 255, 0))
            screen.blit(calvo_sort, (1210, 150))
            calvo_sort = font_op.render(f'{alvo_sort[10]} : {alvo_sort[11]}', True, (255, 255, 0))
            screen.blit(calvo_sort, (1210, 300))
        elif sorteio == 2:
            calvo_sort = font_op.render(f'{alvo_sort[4]} : {alvo_sort[5]}', True, (255, 255, 0))
            screen.blit(calvo_sort, (1210, 200))
            calvo_sort = font_op.render(f'{alvo_sort[7]} : {alvo_sort[8]}', True, (255, 255, 0))
            screen.blit(calvo_sort, (1210, 250))
            calvo_sort = font_op.render(f'{alvo_sort[1]} : {alvo_sort [2]}', True, (255, 255, 0))
            screen.blit(calvo_sort, (1210, 150))
            calvo_sort = font_op.render(f'{alvo_sort[10]} : {alvo_sort[11]}', True, (255, 255, 0))
            screen.blit(calvo_sort, (1210, 300))
        elif sorteio == 3:
            calvo_sort = font_op.render(f'{alvo_sort[10]} : {alvo_sort[11]}', True, (255, 255, 0))
            screen.blit(calvo_sort, (1210, 300))
            calvo_sort = font_op.render(f'{alvo_sort[7]} : {alvo_sort[8]}', True, (255, 255, 0))
            screen.blit(calvo_sort, (1210, 250))
            calvo_sort = font_op.render(f'{alvo_sort[1]} : {alvo_sort [2]}', True, (255, 255, 0))
            screen.blit(calvo_sort, (1210, 150))
            calvo_sort = font_op.render(f'{alvo_sort[4]} : {alvo_sort[5]}', True, (255, 255, 0))
            screen.blit(calvo_sort, (1210, 200))
        elif sorteio == 4:
            calvo_sort = font_op.render(f'{alvo_sort[1]} : {alvo_sort [2]}', True, (255, 255, 0))
            screen.blit(calvo_sort, (1210, 150))
            calvo_sort = font_op.render(f'{alvo_sort[10]} : {alvo_sort[11]}', True, (255, 255, 0))
            screen.blit(calvo_sort, (1210, 300))
            calvo_sort = font_op.render(f'{alvo_sort[4]} : {alvo_sort[5]}', True, (255, 255, 0))
            screen.blit(calvo_sort, (1210, 200))
            calvo_sort = font_op.render(f'{alvo_sort[7]} : {alvo_sort[8]}', True, (255, 255, 0))
            screen.blit(calvo_sort, (1210, 250))


        score = font_score.render(f' Pontuação: {int(pontos)}', True, (255, 255, 0))
        screen.blit(score, (1210, 500))

        pygame.display.update()
    pygame.quit()
