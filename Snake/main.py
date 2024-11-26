import pygame
import time
import random

# Inicializa Pygame
pygame.init()

# Tamaño de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game - Personalizado")

# Colores personalizados
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 50, 50)
green = (50, 255, 50)
blue = (50, 50, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)

# Tamaño y velocidad
snake_block = 20
initial_speed = 10

# Fuentes
font_style = pygame.font.SysFont("comicsansms", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Función para mostrar la puntuación
def show_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    screen.blit(value, [10, 10])

# Dibuja la serpiente
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

# Mensajes en pantalla
def message(msg, color, position):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, position)

# Pantalla de inicio
def game_intro():
    intro = True
    while intro:
        screen.fill(purple)
        message("¡Bienvenido a Snake Game!", yellow, [width / 6, height / 4])
        message("Usa las flechas para moverte", white, [width / 6, height / 3])
        message("Presiona C para jugar o Q para salir", white, [width / 6, height / 2])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

# Bucle principal del juego
def game_loop():
    game_over = False
    game_close = False

    # Posición inicial
    x, y = width / 2, height / 2
    x_change, y_change = 0, 0

    snake_list = []
    snake_length = 1

    # Comida inicial
    food_x = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    score = 0
    speed = initial_speed

    while not game_over:
        while game_close:
            screen.fill(black)
            message("¡Game Over!", red, [width / 3, height / 3])
            message("Presiona C para jugar de nuevo o Q para salir", white, [width / 6, height / 2])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = snake_block
                    x_change = 0

        # Verifica colisiones con las paredes
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(blue)

        # Dibuja la comida
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

        # Actualiza la serpiente
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Verifica colisiones con sí misma
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        show_score(score)

        pygame.display.update()

        # Si la serpiente come
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            snake_length += 1
            score += 10
            speed += 0.5  # Aumenta la velocidad con cada comida

        pygame.time.Clock().tick(speed)

    pygame.quit()
    quit()

# Ejecución del juego
game_intro()
game_loop()