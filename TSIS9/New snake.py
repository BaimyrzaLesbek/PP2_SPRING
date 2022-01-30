import pygame
import random
import math
import time
import json

pygame.init()

WIDTH,HEIGHT = 800,600
FramePerSec = pygame.time.Clock()
tile_size = 20
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("NEW SNAKE GAME")

def menu():

    running1 = True
    choose = 0
    while running1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    running1 = False
                    choose = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    running1 = False
                    choose = 2
        font1 = pygame.font.SysFont("Impact", 72)
        font2 = pygame.font.SysFont("Impact", 36)
        SNAKe = font1.render("SNAKE GAME", True, (255, 139, 0))
        PLAY1 = font2.render("Press 1 to start", True, (13, 171, 255))
        PLAY2 = font2.render("Press 2 to start custom level", True, (13, 171, 255))
        screen.blit(SNAKe, (230, 100))
        screen.blit(PLAY1, (255, 265))
        screen.blit(PLAY2, (180, 300))
        pygame.display.flip()
        screen.fill((0,255,102))
    return choose
def game_over():
    font1 = pygame.font.SysFont("Impact", 72)
    screen.fill((60, 170, 60))
    GAME_OVER = font1.render('GAME OVER!', True, (212, 75, 75))
    screen.blit(GAME_OVER, (240,200))
    pygame.display.flip()
    time.sleep(3)
    global run
    run = False

class world:
    def __init__(self, data):
        self.list_of_tiles = []
        img = pygame.image.load("./images/brick-wall.png")
        row_cnt = 0
        for row in data:
            column = 0
            for tile in row:
                if tile == 1:
                    image = pygame.transform.scale(img, (20,20))
                    rect = image.get_rect()
                    rect.x = column * tile_size
                    rect.y = row_cnt * tile_size
                    self.list_of_tiles.append((image, rect))
                column += 1
            row_cnt += 1
    def draw(self,position):
        for i in self.list_of_tiles:
            screen.blit(i[0],i[1])
            if i[1].collidepoint(position):
                game_over()


class snake:
    def __init__(self,speed,element):
        self.dx = speed
        self.dy = 0
        self.colour = (0,0,255)
        self.element = element
    def draw(self):
        for i in self.element:
            pygame.draw.rect(screen, self.colour, i)
    def move(self):
        for i in range(len(self.element) - 1, 0, -1):
            self.element[i][0] = self.element[i - 1][0]
            self.element[i][1] = self.element[i - 1][1]
        self.element[0][0] += self.dx
        self.element[0][1] += self.dy
    

class food:
    def __init__(self):
        self.colour = (255,0,0)
        self.x = random.randrange(20,760,20)
        self.y = random.randrange(20,540,20)
    def draw(self):
        pygame.draw.rect(screen, self.colour, [self.x, self.y, 20, 20])
        self.rect = pygame.Rect(self.x, self.y, 20,20)
    def coolision(self,position):
        if self.rect.collidepoint(SNAKE.element[0][0], SNAKE.element[0][1]):
            SNAKE.element.append([-20,-20,20,20])
            self.x = random.randrange(20,760,20)
            self.y = random.randrange(20,540,20)
choose = menu()
if choose==1:
    world_data = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
elif choose==2:
    f = open("newlevel", 'r')
    world_data = eval(f.read())

# def draw_line():
#     for i in range(0, 40):
#         pygame.draw.line(screen, (255,255,255), (i*tile_size, 0), (i*tile_size, HEIGHT))
#     for i in range(0, 30):
#         pygame.draw.line(screen, (255,255,255), (0, i*tile_size), (WIDTH, i*tile_size))

run = True
WORLD = world(world_data)
SNAKE = snake(20,[[9*tile_size , 9*tile_size, 20,20 ], [8*tile_size , 9*tile_size,20,20  ], [7*tile_size , 9*tile_size,20,20  ]])
FOOD = food()
while run:
    for i in range(len(SNAKE.element)-1):
        if SNAKE.element[0] == SNAKE.element[i+1]:
            game_over()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and SNAKE.dx != -20:
                SNAKE.dx = 20
                SNAKE.dy = 0
            if event.key == pygame.K_LEFT and SNAKE.dx != 20:
                SNAKE.dx = -20
                SNAKE.dy = 0
            if event.key == pygame.K_UP and SNAKE.dy != 20:
                SNAKE.dx = 0
                SNAKE.dy = -20
            if event.key == pygame.K_DOWN and SNAKE.dy != -20:
                SNAKE.dx = 0
                SNAKE.dy = 20
    screen.fill((0,204,255))
    # draw_line()
    WORLD.draw((SNAKE.element[0][0], SNAKE.element[0][1]))
    SNAKE.draw()
    SNAKE.move()
    FOOD.draw()
    FOOD.coolision((SNAKE.element[0][0], SNAKE.element[0][1]))
    FramePerSec.tick(9)
    pygame.display.flip()
pygame.quit()