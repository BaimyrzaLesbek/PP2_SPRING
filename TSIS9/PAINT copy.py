import pygame
import os
import math


WIDTH, HEIGHT = 800,600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

FramePerSec = pygame.time.Clock()

pygame.display.set_caption("PAINT")
SCREEN.fill((255,255,255))
previous_pos = None
current_pos = None
running = True

rectangle_image = pygame.image.load("./images/rectangle.png")
line_image = pygame.image.load("./images/diagonal-line.png")
circle_image = pygame.image.load("./images/circle.png")
eraser_image = pygame.image.load("./images/eraser.png")

#_______________COLORS_______________
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)  

def colour(choose_color):
    if choose_color == 1:
        #RED
        return (255,0,0)
    elif choose_color == 2:
        #GREEN
        return (0,255,0)
    elif choose_color == 3:
        #BLUE
        return (0,0,255)
    elif choose_color == 4:
        #BLACK
        return (0,0,0)
    elif choose_color == 5:
        #WHITE or ERASER
        return (255,255,255)
    elif choose_color == 6:
        #YELLOW
        return (255,255,0)
    elif choose_color == 7:
        #CYAN
        return (0,255,255)
    elif choose_color == 8:
        #MAGENTA
        return (255,0,255)    

def show_images():
    pygame.draw.rect(SCREEN, RED, [0,0,50,10])
    pygame.draw.rect(SCREEN, GREEN, [50,0,50,10])
    pygame.draw.rect(SCREEN, BLUE, [100,0,50,10])
    pygame.draw.rect(SCREEN, WHITE, [150,0,50,10])
    pygame.draw.rect(SCREEN, BLACK, [200,0,50,10])
    pygame.draw.rect(SCREEN, YELLOW, [250,0,50,10])
    pygame.draw.rect(SCREEN, CYAN, [300,0,50,10])
    pygame.draw.rect(SCREEN, MAGENTA, [350,0,50,10])
    SCREEN.blit(rectangle_image, (700, 0))
    SCREEN.blit(line_image, (730, 0))
    SCREEN.blit(circle_image, (760, 0))
    SCREEN.blit(eraser_image, (670, 0))

#constants
drawing = "line"
right_moment_color = BLACK
zhirnost = 1

red_rect = pygame.Rect(0,0,50,10)
green_rect = pygame.Rect(50,0,50,10)
blue_rect = pygame.Rect(100,0,50,10)
white_rect = pygame.Rect(150,0,50,10)
black_rect = pygame.Rect(200,0,50,10)
yellow_rect = pygame.Rect(250,0,50,10)
cyan_rect = pygame.Rect(300,0,50,10)
magenta_rect = pygame.Rect(350,0,50,10)
rectangular_rect = pygame.Rect(700, 0,24,24)
line_rect = pygame.Rect(730, 0,24,24)
circle_rect = pygame.Rect(760, 0,24,24)
eraser_rect = pygame.Rect(670, 0,24,24)


show_images_bool = True
while running:
    if show_images_bool:
        show_images()
    position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if red_rect.collidepoint(position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                right_moment_color = RED
        if green_rect.collidepoint(position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                right_moment_color = GREEN
        if blue_rect.collidepoint(position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                right_moment_color = BLUE
        if white_rect.collidepoint(position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                right_moment_color = WHITE
        if black_rect.collidepoint(position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                right_moment_color = BLACK
        if yellow_rect.collidepoint(position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                right_moment_color = YELLOW
        if cyan_rect.collidepoint(position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                right_moment_color = CYAN
        if magenta_rect.collidepoint(position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                right_moment_color = MAGENTA
        if rectangular_rect.collidepoint(position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = "rectangle"
        if line_rect.collidepoint(position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = "line"
        if circle_rect.collidepoint(position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = "circle"
        if eraser_rect.collidepoint(position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = "eraser"
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                right_moment_color = colour(1)
            if event.key == pygame.K_2:
                right_moment_color = colour(2)
            if event.key == pygame.K_3:
                right_moment_color = colour(3)
            if event.key == pygame.K_4:
                right_moment_color = colour(4)
            if event.key == pygame.K_5:
                right_moment_color = colour(5)
            if event.key == pygame.K_6:
                right_moment_color = colour(6)
            if event.key == pygame.K_7:
                right_moment_color = colour(7)
            if event.key == pygame.K_8:
                right_moment_color = colour(8)
            if event.key == pygame.K_r:
                drawing = "rectangle"
            if event.key == pygame.K_l:
                drawing = "line"
            if event.key == pygame.K_c:
                drawing = "circle"
            if event.key == pygame.K_e:
                drawing = "eraser"
            if event.key == pygame.K_s:
                show_images_bool = not show_images_bool
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                zhirnost += 1
                if zhirnost >21:
                    zhirnost = 20
            if event.button == 5:
                zhirnost -= 1
                if zhirnost<=0:
                    zhirnost = 1
            previous_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            current_pos = pygame.mouse.get_pos()
            if previous_pos and drawing == "line":
                pygame.draw.line(SCREEN, right_moment_color, previous_pos, current_pos, zhirnost)
                previous_pos = current_pos
            if previous_pos and drawing == "eraser":
                pygame.draw.line(SCREEN, (255,255,255), previous_pos, current_pos, zhirnost)
                previous_pos = current_pos
        if event.type == pygame.MOUSEBUTTONUP:
            current_pos = pygame.mouse.get_pos()
            if drawing == "circle" and event.button == 1:
                pygame.draw.circle(SCREEN, right_moment_color, previous_pos, math.sqrt((abs(current_pos[0]-previous_pos[0]))**2+(abs(current_pos[1]-previous_pos[1]))**2), zhirnost)
            elif drawing == "circle" and event.button == 3:
                pygame.draw.circle(SCREEN, right_moment_color, previous_pos, math.sqrt((abs(current_pos[0]-previous_pos[0]))**2+(abs(current_pos[1]-previous_pos[1]))**2))
                previous_pos = None
            elif previous_pos and drawing == "rectangle" and event.button == 1:
                pygame.draw.rect(SCREEN, right_moment_color,[previous_pos[0],previous_pos[1], abs(current_pos[0]-previous_pos[0]),abs(current_pos[1]-previous_pos[1])], zhirnost)
                previous_pos = None
            elif previous_pos and drawing == "rectangle" and event.button == 3:
                pygame.draw.rect(SCREEN, right_moment_color,[previous_pos[0],previous_pos[1], abs(current_pos[0]-previous_pos[0]),abs(current_pos[1]-previous_pos[1])])
                previous_pos = None
            previous_pos = None
    
    pygame.display.flip()
    FramePerSec.tick(30)
pygame.display.flip()
pygame.draw.rect(SCREEN, WHITE, [0,0,800,30])
pygame.image.save(SCREEN,"NewPaint.png")