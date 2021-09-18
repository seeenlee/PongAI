import pygame
pygame.init()

class Game:
    def __init__(self):
        pass

screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("First Game")

# values associated with all paddles
paddle_length = 25
paddle_width = 125

# coordinates of left paddle
left_paddle_x = 50
left_paddle_y = 250

# coordinates of right paddle
right_paddle_x = 925
right_paddle_y = 250

ball_x = 500
ball_y = 300
x_vel = 1
y_vel = 1
radius = 10

def get_paddle_length():
    return paddle_length
def get_paddle_width():
    return paddle_width
def getleft_paddle_x():
    return left_paddle_x
def get_left_paddle_y():
    return left_paddle_y
def get_right_paddle_x():
    return right_paddle_x
def get_right_paddle_y():
    return right_paddle_y
def get_ball_x():
    return ball_x
def get_ball_y():
    return ball_y
def get_x_vel(self):
    return self.x_vel
def get_y_vel():
    return y_vel
def get_radius():
    return radius


def game_loop():

    loop = True
    clock = pygame.time.Clock()

    while loop:

        #setup of objects
        leftPaddle = pygame.draw.rect(screen, (255,255,255), pygame.Rect(left_paddle_x, left_paddle_y, paddle_length, paddle_width))
        rightPaddle = pygame.draw.rect(screen, (255,255,255), pygame.Rect(right_paddle_x, right_paddle_y, paddle_length, paddle_width))
        cir = pygame.draw.circle(screen, (255, 255, 255), (get_x_vel(), ballY), radius)


        # border boundaries
        if get_x_vel() < radius or get_x_vel() > 1000 - radius:
            xVel = -xVel
        if ballY < radius or ballY > 600 - radius:
            yVel = -yVel
        ballX -= xVel
        ballY -= yVel









        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False


        # update of screen
        pygame.display.update()
        screen.fill((0, 0, 0))


game_loop()