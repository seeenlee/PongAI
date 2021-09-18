import pygame
pygame.init()

screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("First Game")

# values associated with all paddes
paddleLength = 25
paddleWidth = 125

# coordinates of left paddle
leftPaddleX = 50
leftPaddleY = 250

# coordinates of right paddle
rightPaddleX = 925
rightPaddleY = 250

def game_loop():
    ballX = 500
    ballY = 300
    xVel = 1
    yVel = 1
    radius = 10
    loop = True

    clock = pygame.time.Clock()
    while loop:
        leftPaddle = pygame.draw.rect(screen, (255,255,255), pygame.Rect(leftPaddleX, leftPaddleY, paddleLength, paddleWidth))
        rightPaddle = pygame.draw.rect(screen, (255,255,255), pygame.Rect(rightPaddleX, rightPaddleY, paddleLength, paddleWidth))
        cir = pygame.draw.circle(screen, (255, 255, 255), (ballX, ballY), radius)
        if ballX < radius or ballX > 1000 - radius:
            xVel = -xVel
        if ballY < radius or ballY > 600 - radius:
            yVel = -yVel
        ballX -= xVel
        ballY -= yVel
        pygame.display.update()
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False


game_loop()