
import pygame
import random

pygame.init()

# Screen setup
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Snake Game")

# Colors
white = (255, 255, 255)
green = (0, 200, 0)
red = (255, 0, 0)
black = (0, 0, 0)

# Snake settings
snake_block = 20
snake_speed = 10

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)


def show_score(score):
    text = font.render("Score: " + str(score), True, black)
    screen.blit(text, [10, 10])


def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])


def game_loop():
    game_over = False

    # Snake starting position
    x = width // 2
    y = height // 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, width - snake_block) / 20.0) * 20
    food_y = round(random.randrange(0, height - snake_block) / 20.0) * 20

    while not game_over:
        screen.fill(white)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Move snake
        x += x_change
        y += y_change

        # Game over if snake hits wall
        if x >= width or x < 0 or y >= height or y < 0:
            game_over = True

        # Draw food
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

        # Snake body logic
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Game over if snake hits itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True

        draw_snake(snake_list)
        show_score(snake_length - 1)

        pygame.display.update()

        # If snake eats food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 20.0) * 20
            food_y = round(random.randrange(0, height - snake_block) / 20.0) * 20
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()


game_loop()