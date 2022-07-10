import pygame
import random

pygame.init()

black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

fruit_color = "red"

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("Helvetica", 35)


def Yourscore(score):
    value = score_font.render("Your Score was " + str(score), True, red)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 2])


def gameLoop():
    game_over = False
    game_close = False
    game_menu = True

    fruit_color = "red"

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 2

    foodx = 400
    foody = 200

    foodx1 = 450
    foody1 = 250

    foodx2 = 450
    foody2 = 150

    while not game_over:

        while game_close == True:

            dis.fill(black)
            message("You Lost! Press Space to Play Again or Enter to Quit", red)
            Yourscore((Length_of_snake - 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()
                    if event.key == pygame.K_SLASH:
                        game_menu = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, fruit_color, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, fruit_color, [foodx1, foody1, snake_block, snake_block])
        pygame.draw.rect(dis, fruit_color, [foodx2, foody2, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-2]:
            if x == snake_Head:
                game_close = False

        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1

        if x1 == foodx1 and y1 == foody1:
            foodx1 = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody1 = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1

        if x1 == foodx2 and y1 == foody2:
            foodx2 = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody2 = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
