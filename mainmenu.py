import pygame, sys

pygame.init()

screen = pygame.display.set_mode((1000, 600))  # setting display size
pygame.display.set_caption("PONG")  # title

done = False

def single_player():
    font = pygame.font.SysFont("arial", 30)  # setting font style and size
    back = font.render("BACK", True, (255, 255, 255))  # creating a back button
    easy = font.render("EASY", True, (255, 255, 255))   # creating an easy mode button
    hard = font.render("HARD", True, (255, 255, 255))   # creating a hard mode button

    screen.blit(back, (60 - back.get_width() // 2, 560 - back.get_height() // 2))
    screen.blit(easy, (500 - easy.get_width() // 2, 175 - easy.get_height() // 2))
    screen.blit(hard, (500 - back.get_width() // 2, 425 - back.get_height() // 2))

    back_box = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(20, 520, 100, 50))  # creating rectangle over text
    easy_box = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(375, 150, 250, 50))
    hard_box = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(375, 400, 250, 50))

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
                if easy_box.collidepoint(mx, my):
                    easy = font.render("EASY", True, (128, 128, 128))
                    screen.blit(easy, (500 - easy.get_width() // 2, 175 - easy.get_height() // 2))
                if not easy_box.collidepoint(mx, my):
                    easy = font.render("EASY", True, (255, 255, 255))
                    screen.blit(easy, (500 - easy.get_width() // 2, 175 - easy.get_height() // 2))
                if hard_box.collidepoint(mx, my):
                    hard = font.render("HARD", True, (128, 128, 128))
                    screen.blit(hard, (500 - back.get_width() // 2, 425 - back.get_height() // 2))
                if not hard_box.collidepoint(mx, my):
                    hard = font.render("HARD", True, (255, 255, 255))
                    screen.blit(hard, (500 - back.get_width() // 2, 425 - back.get_height() // 2))

                click = pygame.mouse.get_pressed()
                if click[0] == 1 and 10 < mx < 80 and 520 < my < 590:  # if instructions is clicked, instructions pops up
                    modes()
                if click[0] == 1 and 450 < mx < 550 and 145 < my < 205:  # easy mode
                    main_menu()  # CHANGE TO ACTUAL CODE
                if click[0] == 1 and 450 < mx < 550 and 395 < my < 4550:
                    main_menu()  # CHANGE TO ACTUAL FUNCTION

            pygame.display.flip()
            pygame.display.update()


def modes():
    font = pygame.font.SysFont("arial", 30)  # setting font style and size
    back = font.render("BACK", True, (255, 255, 255))  # creating a back button
    sp = font.render("SINGLE PLAYER", True, (255, 255, 255))  # creating a single player button
    mp = font.render("MULTIPLAYER", True, (255, 255, 255))  # creating a multiplayer button
    co = font.render("COMPUTER ONLY", True, (255, 255, 255))  # creating a computer only button
    tm = font.render("TRAINING", True, (255, 255, 255))  # creating a training mode button
    sm = font.render("SURVIVAL", True, (255, 255, 255))  # creating a survival mode button

    screen.blit(back, (60 - back.get_width() // 2, 560 - back.get_height() // 2))  # location of buttons
    screen.blit(sp, (500 - sp.get_width() // 2, 100 - sp.get_height() // 2))
    screen.blit(mp, (500 - mp.get_width() // 2, 200 - mp.get_height() // 2))
    screen.blit(co, (500 - co.get_width() // 2, 300 - co.get_height() // 2))
    screen.blit(tm, (500 - tm.get_width() // 2, 400 - tm.get_height() // 2))
    screen.blit(sm, (475 - back.get_width() // 2, 500 - back.get_height() // 2))

    back_box = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(20, 520, 100, 50))  # creating rectangle over text
    sp_box = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(375, 70, 250, 50))
    mp_box = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(375, 170, 250, 50))
    co_box = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(375, 270, 250, 50))
    tm_box = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(375, 370, 250, 50))
    sm_box = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(375, 470, 250, 50))

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
                if sp_box.collidepoint(mx, my):
                    sp = font.render("SINGLE PLAYER", True, (128, 128, 128))
                    screen.blit(sp, (500 - sp.get_width() // 2, 100 - sp.get_height() // 2))
                if not sp_box.collidepoint(mx, my):
                    sp = font.render("SINGLE PLAYER", True, (255, 255, 255))
                    screen.blit(sp, (500 - sp.get_width() // 2, 100 - sp.get_height() // 2))
                if mp_box.collidepoint(mx, my):
                    mp = font.render("MULTIPLAYER", True, (128, 128, 128))
                    screen.blit(mp, (500 - mp.get_width() // 2, 200 - mp.get_height() // 2))
                if not mp_box.collidepoint(mx, my):
                    mp = font.render("MULTIPLAYER", True, (255, 255, 255))
                    screen.blit(mp, (500 - mp.get_width() // 2, 200 - mp.get_height() // 2))
                if co_box.collidepoint(mx, my):
                    co = font.render("COMPUTER ONLY", True, (128, 128, 128))
                    screen.blit(co, (500 - co.get_width() // 2, 300 - co.get_height() // 2))
                if not co_box.collidepoint(mx, my):
                    co = font.render("COMPUTER ONLY", True, (255, 255, 255))
                    screen.blit(co, (500 - co.get_width() // 2, 300 - co.get_height() // 2))
                if tm_box.collidepoint(mx, my):
                    tm = font.render("TRAINING", True, (128, 128, 128))
                    screen.blit(tm, (500 - tm.get_width() // 2, 400 - tm.get_height() // 2))
                if not tm_box.collidepoint(mx, my):
                    tm = font.render("TRAINING", True, (255, 255, 255))
                    screen.blit(tm, (500 - tm.get_width() // 2, 400 - tm.get_height() // 2))
                if sm_box.collidepoint(mx, my):
                    sm = font.render("SURVIVAL", True, (128, 128, 128))
                    screen.blit(sm, (475 - back.get_width() // 2, 500 - back.get_height() // 2))
                if not sm_box.collidepoint(mx, my):
                    sm = font.render("SURVIVAL", True, (255, 255, 255))
                    screen.blit(sm, (475 - back.get_width() // 2, 500 - back.get_height() // 2))

                click = pygame.mouse.get_pressed()
                if click[0] == 1 and 10 < mx < 80 and 520 < my < 590:  # if instructions is clicked, instructions pops up
                    main_menu()
                elif click[0] == 1 and 450 < mx < 550 and 70 < my < 130:  # single player
                    single_player()
                elif click[0] == 1 and 450 < mx < 550 and 170 < my < 230:  # multiplayer
                    main_menu()  # placeholder CHANGE TO MULTIPLAYER
                elif click[0] == 1 and 450 < mx < 550 and 270 < my < 330:  # computer only
                    main_menu()  # placeholder CHANGE TO MULTIPLAYER
                elif click[0] == 1 and 450 < mx < 550 and 370 < my < 430:  # training
                    main_menu()  # placeholder CHANGE TO MULTIPLAYER
                elif click[0] == 1 and 450 < mx < 550 and 470 < my < 530:  # survival
                    main_menu()  # placeholder CHANGE TO MULTIPLAYER

            pygame.display.flip()
            pygame.display.update()


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

    instruction = font.render("INSTRUCTIONS", True, (255, 255, 255))  # setting buttons onto screen
    enter = font.render("PLAY", True, (255, 255, 255))
    gamename = font1.render("PONG", True, (255, 255, 255))
    instructions_box = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(375, 470, 250, 60))  # setting location of
    # rectangles 
    enter_box = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(445, 400, 100, 50))

    screen.blit(instruction,  # setting location of buttons
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
                    modes()

            clock.tick(60)
            pygame.display.update()


main_menu()

pygame.quit()
