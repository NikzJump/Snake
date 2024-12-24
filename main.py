import pygame
import random
import hamilton_cycle

alive = True
direction = 0

clock = pygame.time.Clock()

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

Wsize = (720, 480)

screen = pygame.display.set_mode(Wsize)

Tside = 30
Msize = Wsize[0] // Tside, Wsize[1] // Tside

start_pos = 0, 0

snake = [start_pos]

apple = random.randint(0, Msize[0] - 1), random.randint(0, Msize[1] - 1)
run = True


while run:
    dirs = hamilton_cycle.cycle(Msize, len(snake))
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
                screen, "green", (x * Tside, y * Tside, Tside - 1, Tside - 1)
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
            if len(snake) != len(set(snake)):
                alive = False
            snake.insert(0, new_pos)
            if new_pos == apple:
                apple = random.randint(0, Msize[0] - 1), random.randint(0, Msize[1] - 1)
                if apple in snake:
                    apple = (
                        random.randint(0, Msize[0] - 1),
                        random.randint(0, Msize[1] - 1),
                    )
                    continue
                snake.append(new_pos)
            snake.pop(-1)
            pygame.display.flip()
        continue

#     if event.key == pygame.K_d and direction != 2:
#         direction = 0
#     if event.key == pygame.K_s and direction != 3:
#         direction = 1
#     if event.key == pygame.K_a and direction != 0:
#         direction = 2
#     if event.key == pygame.K_w and direction != 1:
#         direction = 3


# if snake[0][0] < apple[0]:
#     if direction != 2:
#         direction = 0
#     elif snake[0][1] + 5 <= Msize[1]:
#         direction = 3
#     elif snake[0][1] + 5 > Msize[1]:
#         direction = 1
#
# elif snake[0][0] > apple[0]:
#     if direction != 0:
#         direction = 2
#     elif snake[0][1] + 5 <= Msize[1]:
#         direction = 3
#     elif snake[0][1] + 5 > Msize[1]:
#         direction = 1
#
# elif snake[0][1] < apple[1]:
#     if direction != 3:
#         direction = 1
#     elif snake[0][0] - 5 < Msize[0]:
#         direction = 0
#     elif snake[0][0] - 5 >= Msize[0]:
#         direction = 2
#
# elif snake[0][1] > apple[1]:
#     if direction != 1:
#         direction = 3
#     else:
#         direction = 2
