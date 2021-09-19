import pygame, sys

pygame.init()

screen = pygame.display.set_mode((1000, 600))  # setting display size
pygame.display.set_caption("PONG")  # title

done = False

def instr():
    font = pygame.font.SysFont("arial", 30)
    back = font.render("BACK", True, (255, 255, 255))  # creating a back button
    screen.blit(back, (60 - back.get_width() // 2, 560 - back.get_height() // 2))
    back_box = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(20, 520, 100, 50))  # creating rectangle over text

    go = True  # printing instructions
    while go:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                go = False
                sys.exit(0)
            elif event.type == pygame.MOUSEMOTION:  # detecting mouse movement
                mx, my = event.pos  # tracking mouse movement once detected
                if back_box.collidepoint(mx, my):
                    back = font.render("BACK", True, (128, 128, 128))
                    screen.blit(back, (60 - back.get_width() // 2, 560 - back.get_height() // 2))
                    #  if mouse interacts with box, highlights text
                if not back_box.collidepoint(mx, my):
                    back = font.render("BACK", True, (255, 255, 255))
                    screen.blit(back, (60 - back.get_width() // 2, 560 - back.get_height() // 2))

            font = pygame.font.SysFont("arial", 25)
            instructions_A = "Move your paddle with the up and down arrow keys on your device. "
            instructions_B = "Hit the ball past your opponent to score a point! "
            instructions_C =  "First to 10 wins! Good Luck!"
            a = font.render(instructions_A, True, (255, 255, 255))  # assigning colors
            b = font.render(instructions_B, True, (255, 255, 255))
            c = font.render(instructions_C, True, (255, 255, 255))
            screen.blit(a, (500 - a.get_width() // 2, 200 - a.get_height() // 2))  # printing text
            screen.blit(b, (500 - b.get_width() // 2, 300 - b.get_height() // 2))
            screen.blit(c, (500 - c.get_width() // 2, 400 - c.get_height() // 2))

            click = pygame.mouse.get_pressed()
            if click[0] == 1 and 10 < mx < 80 and 520 < my < 590:  # if instructions is clicked, instructions pops up
                main_menu()

            pygame.display.flip()
            pygame.display.update()


def main_menu():
    screen.fill((0, 0, 0))  # setting screen black
    font = pygame.font.SysFont("arial", 30)
    font1 = pygame.font.SysFont("arial", 80)

    instruction = font.render("INSTRUCTIONS", True, (255, 255, 255))  # setting text onto screen
    enter = font.render("PLAY", True, (255, 255, 255))
    gamename = font1.render("PONG", True, (255, 255, 255))
    instructions_box = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(375, 470, 250, 60))  # setting location of
    # rectangles 
    enter_box = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(445, 400, 100, 50))

    screen.blit(instruction,  # setting location of text
                (500 - instruction.get_width() // 2, 500 - instruction.get_height() // 2))
    screen.blit(gamename,
                (500 - gamename.get_width() // 2, 200 - gamename.get_height() // 2))
    screen.blit(enter,
                (475 - enter.get_height() // 2, 425 - enter.get_height() // 2))

    pygame.display.flip()
    clock = pygame.time.Clock()
    intro = True
    mouse_position = False
    while intro:
        for event in pygame.event.get():  # letting game quit when inputted
            if event.type == pygame.QUIT:
                intro = False
                sys.exit(0)
            elif event.type == pygame.MOUSEMOTION:  # detecting mouse motion
                mx, my = event.pos  # getting position when mouse motion detected
                if instructions_box.collidepoint(mx, my):  # highlighting text when mouse touches rectangle
                    instruction = font.render("INSTRUCTIONS", True, (128, 128, 128))
                    screen.blit(instruction,
                                (500 - instruction.get_width() // 2, 500 - instruction.get_height() // 2))
                if not instructions_box.collidepoint(mx, my):  # un-highlighting when mouse removed from rectangle
                    instruction = font.render("INSTRUCTIONS", True, (255, 255, 255))
                    screen.blit(instruction,
                                (500 - instruction.get_width() // 2, 500 - instruction.get_height() // 2))
                if enter_box.collidepoint(mx, my):
                    enter = font.render("PLAY", True, (128, 128, 128))
                    screen.blit(enter,
                                (475 - enter.get_height() // 2, 425 - enter.get_height() // 2))
                if not enter_box.collidepoint(mx, my):
                    enter = font.render("PLAY", True, (255, 255, 255))
                    screen.blit(enter,
                                (475 - enter.get_height() // 2, 425 - enter.get_height() // 2))
            click = pygame.mouse.get_pressed()  # detecting mouse input
            if click[0] == 1 and 450 < mx < 550 and 450 < my < 530:  # if instructions is clicked, instructions pops up
                instr()
            elif click[0] == 1 and 450 < mx < 500 and 400 < my < 450:  # if play is clicked, difficulty function called
                instr()

            clock.tick(60)
            pygame.display.update()


main_menu()

pygame.quit()
