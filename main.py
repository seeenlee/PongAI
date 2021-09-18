import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("First Game")


def game_loop():
    # coordinates of ball
    ball_x = 500
    ball_y = 300

    # speed of ball
    x_vel = 1
    y_vel = 1

    # radius of ball
    RADIUS = 10

    # coordinates of right paddle
    right_paddle_x = 925
    right_paddle_y = 250

    # coordinates of left paddle
    left_paddle_x = 50
    left_paddle_y = 250

    # values associated with all paddles
    PADDLE_LENGTH = 25
    PADDLE_WIDTH = 125

    loop = True
    clock = pygame.time.Clock()

    while loop:

        # setup of objects
        left_paddle = pygame.draw.rect(screen, (255, 255, 255),
                                       pygame.Rect(left_paddle_x, left_paddle_y, PADDLE_LENGTH, PADDLE_WIDTH))
        right_paddle = pygame.draw.rect(screen, (255, 255, 255),
                                        pygame.Rect(right_paddle_x, right_paddle_y, PADDLE_LENGTH, PADDLE_WIDTH))
        cir = pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), RADIUS)

        # border boundaries
        if ball_x < RADIUS or ball_x > 1000 - RADIUS:
            x_vel = -x_vel
        if ball_y < RADIUS or ball_y > 600 - RADIUS:
            y_vel = -y_vel
        ball_x -= x_vel
        ball_y -= y_vel

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        # update of screen
        pygame.display.update()
        screen.fill((0, 0, 0))


game_loop()