import time

import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("First Game")

# values associated with all paddles
PADDLE_WIDTH = 25
PADDLE_LENGTH = 125

# radius of ball
RADIUS = 10


def game_loop():

    # coordinates of ball
    ball_x = 500
    ball_y = 300

    # speed of ball
    x_vel = -7
    y_vel = 7

    # coordinates of right paddle
    right_paddle_x = 925
    right_paddle_y = 250

    # coordinates of left paddle
    left_paddle_x = 50
    left_paddle_y = 250

    loop = True
    clock = pygame.time.Clock()

    while loop:
        ball_x -= x_vel
        ball_y -= y_vel
        # setup of objects
        left_paddle = pygame.draw.rect(screen, (255, 255, 255),
                                       pygame.Rect(left_paddle_x, left_paddle_y, PADDLE_WIDTH, PADDLE_LENGTH))
        right_paddle = pygame.draw.rect(screen, (255, 255, 255),
                                        pygame.Rect(right_paddle_x, right_paddle_y, PADDLE_WIDTH, PADDLE_LENGTH))
        ball = pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), RADIUS)

        # border boundaries
        if ball_x < RADIUS or ball_x > 1000 - RADIUS:
            ball_x = 500
            ball_y = 300
            x_vel = -7
            y_vel = 7
            # TODO: move the ball to the middle before it freezes
            time.sleep(1)

        if ball_y < RADIUS or ball_y > 600 - RADIUS:
            y_vel = -y_vel

        # bouncing off paddle
        if ball.colliderect(left_paddle):
            if (left_paddle_y + (PADDLE_LENGTH / 2)) <= ball_y:
                x_vel = -x_vel
                y_vel = y_vel
            elif (left_paddle_y + (PADDLE_LENGTH / 2)) > ball_y:
                x_vel = -x_vel
                y_vel = y_vel
        if ball.colliderect(right_paddle):
            x_vel = -x_vel
            if (right_paddle_y + (PADDLE_LENGTH / 2)) <= ball_y:
                if y_vel < 0:
                    y_vel *= 1
                else:
                    y_vel = -y_vel
            elif (right_paddle_y + (PADDLE_LENGTH / 2)) > ball_y:
                if y_vel > 0:
                    y_vel *= 1
                else:
                    y_vel = -y_vel

            else:
                print('why are you here')

        # paddle control
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            right_paddle_y -= 8
        if pressed[pygame.K_DOWN]:
            right_paddle_y += 8

        # AI

        if (left_paddle_y + (PADDLE_LENGTH / 2)) < ball_y:
            left_paddle_y += 10
        if (left_paddle_y + (PADDLE_LENGTH / 2)) > ball_y:
            left_paddle_y -= 10


        # game quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        # update of screen
        pygame.display.update()
        screen.fill((0, 0, 0))
        clock.tick(60)


game_loop()
