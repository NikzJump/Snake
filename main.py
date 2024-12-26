import pygame
import random

import hamilton_cycle
import a_star

alive = True
direction = 0

clock = pygame.time.Clock()

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

Wsize = (720, 480)

screen = pygame.display.set_mode(Wsize)

Tside = 10
Msize = Wsize[0] // Tside, Wsize[1] // Tside

start_pos = 0, 0

snake = [start_pos]

apple = random.randint(0, Msize[0] - 3), random.randint(0, Msize[1] - 3)
run = True

dirs = a_star.convert_to_dirs(a_star.a_star(Msize, snake[0], apple, snake, snake[0]))

calculate_status = True
color = "green"


def error_calculate_dirs(local_calculate_status, Msize):
    new_apple = None
    stop_num = 0
    while not local_calculate_status:
        stop_num += 1
        new_apple = (
            random.randint(0, Msize[0] - 3),
            random.randint(0, Msize[1] - 3),
        )

        local_calculate_status = a_star.convert_to_dirs(
            a_star.a_star(Msize, snake[0], new_apple, snake, snake[0])
        )

    return local_calculate_status, new_apple


while run:
    for dir in dirs:
        clock.tick(100)
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    alive = True
                    run = True
                    apple = (
                        random.randint(0, Msize[0] - 1),
                        random.randint(0, Msize[1] - 1),
                    )
                    snake = [start_pos]

        [
            pygame.draw.rect(
                screen, color, (x * Tside, y * Tside, Tside - 1, Tside - 1)
            )
            for x, y in snake
        ]
        pygame.draw.rect(
            screen, "red", (apple[0] * Tside, apple[1] * Tside, Tside - 1, Tside - 1)
        )

        if not alive:
            continue

        direction = dir

        new_pos = (
            snake[0][0] + directions[direction][0],
            snake[0][1] + directions[direction][1],
        )

        if not (0 <= new_pos[0] < Msize[0] and 0 <= new_pos[1] < Msize[1]):
            alive = False
        else:
            snake.insert(0, new_pos)
            if snake[0] == apple:
                apple = random.randint(0, Msize[0] - 3), random.randint(0, Msize[1] - 3)
                print("Длина: ", len(snake))
                if apple in snake:
                    apple = (
                        random.randint(0, Msize[0] - 1),
                        random.randint(0, Msize[1] - 1),
                    )

                    while apple in snake:
                        apple = (
                            random.randint(0, Msize[0] - 1),
                            random.randint(0, Msize[1] - 1),
                        )

                snake.append(new_pos)

                calculate_status = a_star.convert_to_dirs(
                    a_star.a_star(Msize, snake[0], apple, snake, snake[0])
                )

                if not calculate_status:
                    error_result = error_calculate_dirs(calculate_status, Msize)
                    calculate_status = error_result[0]
                    apple = error_result[1]

                dirs = calculate_status

            snake.pop(-1)
            pygame.display.flip()

            new_pos = snake[0]


#     if event.key == pygame.K_d and direction != 2:
#         direction = 0
#     if event.key == pygame.K_s and direction != 3:
#         direction = 1
#     if event.key == pygame.K_a and direction != 0:
#         direction = 2
#     if event.key == pygame.K_w and direction != 1:
#         direction = 3
