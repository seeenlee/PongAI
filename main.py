import time

import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Pong!")

# values associated with all paddles
PADDLE_WIDTH = 25
PADDLE_LENGTH = 125

# radius of ball
RADIUS = 10

global font
font = pygame.font.SysFont("arial", 30)


def write(text, location, color=(255, 255, 255)):
    screen.blit(font.render(text, True, color), location)

def bot_mode():
    # coordinates of ball
    ball_x = 500
    ball_y = 300

    # speed of ball
    x_vel = -8
    y_vel = 8

    # coordinates of right paddle
    right_paddle_x = 925
    right_paddle_y = 250

    # coordinates of left paddle
    left_paddle_x = 50
    left_paddle_y = 250

    loop = True
    clock = pygame.time.Clock()

    player1_score = 0
    player2_score = 0

    while loop:

        # score calculation
        # score_count = "Player 1: " + str(player1_score) + "          " + "Player 2: " + str(player2_score)
        # write(score_count, (300, 10))

        ball_x -= x_vel
        ball_y -= y_vel

        # setup of objects
        left_paddle = pygame.draw.rect(screen, (255, 255, 255),
                                       pygame.Rect(left_paddle_x, left_paddle_y, PADDLE_WIDTH, PADDLE_LENGTH))
        right_paddle = pygame.draw.rect(screen, (255, 255, 255),
                                        pygame.Rect(right_paddle_x, right_paddle_y, PADDLE_WIDTH, PADDLE_LENGTH))
        ball = pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), RADIUS)

        # Dividing the paddle
        ball1 = pygame.draw.circle(screen, (255, 0, 0), (925, right_paddle_y + 25), 3)
        ball2 = pygame.draw.circle(screen, (255, 0, 0), (925, right_paddle_y + 50), 3)
        ball3 = pygame.draw.circle(screen, (255, 0, 0), (925, right_paddle_y + 75), 3)
        ball4 = pygame.draw.circle(screen, (255, 0, 0), (925, right_paddle_y + 100), 3)

        # border boundaries
        if ball_x < RADIUS or ball_x > 1000 - RADIUS:
            ball_x = 500
            ball_y = 300
            x_vel = -7
            y_vel = 7
            if ball_x < RADIUS:
                player2_score += 1
            else:
                player1_score += 1
            # TODO: move the ball to the middle before it freezes
            time.sleep(1)

        if ball_y < RADIUS or ball_y > 600 - RADIUS:
            y_vel = -y_vel

        # bouncing off paddle
        if ball.colliderect(left_paddle):
            x_vel = -x_vel
            if (left_paddle_y + (PADDLE_LENGTH / 2)) < ball_y:
                if y_vel < 0:
                    y_vel *= 1
                    print('same slope')
                else:
                    y_vel = -y_vel
                    print('changed slope')
            elif (left_paddle_y + (PADDLE_LENGTH / 2)) > ball_y:
                if y_vel > 0:
                    y_vel *= 1
                    print('same slope')
                else:
                    y_vel = -y_vel
                    print('change slope')

            else:
                print('why are you here')

        if ball.colliderect(right_paddle):
            x_vel = -x_vel
            if (925 < right_paddle_x <= 950 and right_paddle_y + (PADDLE_LENGTH / 5)):
                y_vel = 8
            elif (925 < right_paddle_x <= 950 and right_paddle_y + 5 * (PADDLE_LENGTH / 5)):
                y_vel = -8
            elif (right_paddle_y + (PADDLE_LENGTH / 5)) >= ball_y:
                if y_vel > 0:
                    y_vel = y_vel
                elif y_vel < 0:
                    y_vel = -y_vel
                elif y_vel == 0:
                    y_vel = 8
            elif right_paddle_y + 2 * (PADDLE_LENGTH / 5) >= ball_y:
                if y_vel > 0:
                    y_vel = y_vel
                elif y_vel < 0:
                    y_vel = -y_vel
                elif y_vel == 0:
                    y_vel = 8
            elif right_paddle_y + 3 * (PADDLE_LENGTH / 5) >= ball_y:
                y_vel = 0.1
            elif right_paddle_y + 4 * (PADDLE_LENGTH / 5) >= ball_y:
                if y_vel > 0:
                    y_vel = -y_vel
                elif y_vel < 0:
                    y_vel = y_vel
                elif y_vel == 0:
                    y_vel = -8
            elif right_paddle_y + 5 * (PADDLE_LENGTH / 5) >= ball_y:
                if y_vel > 0:
                    y_vel = -y_vel
                elif y_vel < 0:
                    y_vel = y_vel
                elif y_vel == 0:
                    y_vel = -8

        # paddle control
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and 0 <= right_paddle_y:
            right_paddle_y -= 8
        if pressed[pygame.K_DOWN] and right_paddle_y <= 475:
            right_paddle_y += 8

        # AI

        if (x_vel < 0) and (ball_x > 500):
            if (left_paddle_y + (PADDLE_LENGTH / 2)) < ball_y:
                left_paddle_y += 3
            if (left_paddle_y + (PADDLE_LENGTH / 2)) > ball_y:
                left_paddle_y -= 3
        elif ball_y < 100 or ball_y > 500:
            if (left_paddle_y + (PADDLE_LENGTH / 2)) < ball_y:
                left_paddle_y += 3
            if (left_paddle_y + (PADDLE_LENGTH / 2)) > ball_y:
                left_paddle_y -= 3
        elif x_vel < 0:
            if (left_paddle_y + (PADDLE_LENGTH / 2)) < ball_y:
                left_paddle_y += 5
            if (left_paddle_y + (PADDLE_LENGTH / 2)) > ball_y:
                left_paddle_y -= 5
        else:
            if (left_paddle_y + (PADDLE_LENGTH / 2)) < ball_y:
                left_paddle_y += 8
            if (left_paddle_y + (PADDLE_LENGTH / 2)) > ball_y:
                left_paddle_y -= 8

        # bot tester
        #TODO:paddle gets stuck
        if (right_paddle_y + (PADDLE_LENGTH / 2)) < ball_y:
            right_paddle_y += 10
        if (right_paddle_y + (PADDLE_LENGTH / 2)) > ball_y:
            right_paddle_y -= 10
        # game quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        # update of screen
        pygame.display.update()
        screen.fill((0, 0, 0))
        clock.tick(60)
def singleplayer_easy():
    # coordinates of ball
    ball_x = 500
    ball_y = 300

    # speed of ball
    x_vel = -8
    y_vel = 8

    # coordinates of right paddle
    right_paddle_x = 925
    right_paddle_y = 250

    # coordinates of left paddle
    left_paddle_x = 50
    left_paddle_y = 250

    loop = True
    clock = pygame.time.Clock()

    player1_score = 0
    player2_score = 0

    while loop:

        # score calculation
        score_count = "Player 1: " + str(player1_score) + "          " + "Player 2: " + str(player2_score)
        write(score_count, (300, 10))

        ball_x -= x_vel
        ball_y -= y_vel

        # setup of objects
        left_paddle = pygame.draw.rect(screen, (255, 255, 255),
                                       pygame.Rect(left_paddle_x, left_paddle_y, PADDLE_WIDTH, PADDLE_LENGTH))
        right_paddle = pygame.draw.rect(screen, (255, 255, 255),
                                        pygame.Rect(right_paddle_x, right_paddle_y, PADDLE_WIDTH, PADDLE_LENGTH))
        ball = pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), RADIUS)

        # Dividing the paddle
        ball1 = pygame.draw.circle(screen, (255, 0, 0), (925, right_paddle_y + 25), 3)
        ball2 = pygame.draw.circle(screen, (255, 0, 0), (925, right_paddle_y + 50), 3)
        ball3 = pygame.draw.circle(screen, (255, 0, 0), (925, right_paddle_y + 75), 3)
        ball4 = pygame.draw.circle(screen, (255, 0, 0), (925, right_paddle_y + 100), 3)

        # border boundaries
        if ball_x < RADIUS or ball_x > 1000 - RADIUS:
            ball_x = 500
            ball_y = 300
            x_vel = -7
            y_vel = 7
            if ball_x < RADIUS:
                player2_score += 1
            else:
                player1_score += 1
            # TODO: move the ball to the middle before it freezes
            time.sleep(1)

        if ball_y < RADIUS or ball_y > 600 - RADIUS:
            y_vel = -y_vel

        # bouncing off paddle
        if ball.colliderect(left_paddle):
            x_vel = -x_vel
            if (left_paddle_y + (PADDLE_LENGTH / 2)) < ball_y:
                if y_vel < 0:
                    y_vel *= 1
                    print('same slope')
                else:
                    y_vel = -y_vel
                    print('changed slope')
            elif (left_paddle_y + (PADDLE_LENGTH / 2)) > ball_y:
                if y_vel > 0:
                    y_vel *= 1
                    print('same slope')
                else:
                    y_vel = -y_vel
                    print('change slope')

            else:
                print('why are you here')

        if ball.colliderect(right_paddle):
            x_vel = -x_vel
            if (925 < right_paddle_x <= 950 and right_paddle_y + (PADDLE_LENGTH / 5)):
                y_vel = 8
            elif (925 < right_paddle_x <= 950 and right_paddle_y + 5 * (PADDLE_LENGTH / 5)):
                y_vel = -8
            elif (right_paddle_y + (PADDLE_LENGTH / 5)) >= ball_y:
                if y_vel > 0:
                    y_vel = y_vel
                elif y_vel < 0:
                    y_vel = -y_vel
                elif y_vel == 0:
                    y_vel = 8
            elif right_paddle_y + 2 * (PADDLE_LENGTH / 5) >= ball_y:
                if y_vel > 0:
                    y_vel = y_vel
                elif y_vel < 0:
                    y_vel = -y_vel
                elif y_vel == 0:
                    y_vel = 8
            elif right_paddle_y + 3 * (PADDLE_LENGTH / 5) >= ball_y:
                y_vel = 0.1
            elif right_paddle_y + 4 * (PADDLE_LENGTH / 5) >= ball_y:
                if y_vel > 0:
                    y_vel = -y_vel
                elif y_vel < 0:
                    y_vel = y_vel
                elif y_vel == 0:
                    y_vel = -8
            elif right_paddle_y + 5 * (PADDLE_LENGTH / 5) >= ball_y:
                if y_vel > 0:
                    y_vel = -y_vel
                elif y_vel < 0:
                    y_vel = y_vel
                elif y_vel == 0:
                    y_vel = -8

        # paddle control
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            right_paddle_y -= 8
        if pressed[pygame.K_DOWN]:
            right_paddle_y += 8

        # AI

        if (x_vel < 0) and (ball_x > 500):
            if (left_paddle_y + (PADDLE_LENGTH / 2)) < ball_y:
                left_paddle_y += 3
            if (left_paddle_y + (PADDLE_LENGTH / 2)) > ball_y:
                left_paddle_y -= 3
        elif ball_y < 100 or ball_y > 500:
            if (left_paddle_y + (PADDLE_LENGTH / 2)) < ball_y:
                left_paddle_y += 3
            if (left_paddle_y + (PADDLE_LENGTH / 2)) > ball_y:
                left_paddle_y -= 3
        elif x_vel < 0:
            if (left_paddle_y + (PADDLE_LENGTH / 2)) < ball_y:
                left_paddle_y += 5
            if (left_paddle_y + (PADDLE_LENGTH / 2)) > ball_y:
                left_paddle_y -= 5
        else:
            if (left_paddle_y + (PADDLE_LENGTH / 2)) < ball_y:
                left_paddle_y += 8
            if (left_paddle_y + (PADDLE_LENGTH / 2)) > ball_y:
                left_paddle_y -= 8

        # bot tester
        # if (right_paddle_y + (PADDLE_LENGTH / 2)) < ball_y:
        #     right_paddle_y += 10
        # if (right_paddle_y + (PADDLE_LENGTH / 2)) > ball_y:
        #     right_paddle_y -= 10
        # game quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        # update of screen
        pygame.display.update()
        screen.fill((0, 0, 0))
        clock.tick(60)

bot_mode()
# singleplayer_easy()
