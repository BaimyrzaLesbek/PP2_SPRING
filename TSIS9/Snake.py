# Не сделано коллизии между двумя змейками
# Не смог сделать стенки

import pygame
import random
import time
import json
pygame.init()
WIDTH, HEIGHT = 800,600
FPS = 30
font = pygame.font.SysFont("Impact", 20)
font1 = pygame.font.SysFont("Impact", 72)
font2 = pygame.font.SysFont("Impact", 36)

FramePerSec = pygame.time.Clock()
Screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Zmeika")

brick = pygame.image.load("./images/brick-wall.png")
Score = 0
running = True
class eda():
    def __init__(self):
        self.radius = 5
        self.x = random.randint(100,600)
        self.y = random.randint(100,500)
    def draw(self):
        pygame.draw.circle(Screen, (255,0,0), [self.x, self.y], self.radius)

class Snake():
    def __init__(self, colour, element):
        self.radius = 5
        self.dx = 1
        self.dy = 0
        self.colour = colour
        self.element = element

    def move(self):
        for i in range(len(self.element) - 1, 0, -1):
            self.element[i][0] = self.element[i - 1][0]
            self.element[i][1] = self.element[i - 1][1]
        self.element[0][0] += self.dx
        self.element[0][1] += self.dy
    def draw(self):
        for i in self.element:
            pygame.draw.circle(Screen,self.colour,i,self.radius)

class Wall():
    def __init__(self):
        self.image = pygame.image.load("./images/wall.png")
        self.length = 32
        self.width = 32
    
    def draw(self):
        pass

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    running1 = False
                    choose = 3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    running1 = False
                    choose = 4
        font1 = pygame.font.SysFont("Impact", 72)
        font2 = pygame.font.SysFont("Impact", 36)
        SNAKE = font1.render("SNAKE GAME", True, (255, 139, 0))
        PLAY1 = font2.render("Press 1 to start easy level", True, (13, 171, 255))
        PLAY2 = font2.render("Press 2 to start medium level", True, (13, 171, 255))
        PLAY3 = font2.render("Press 3 to start hard level", True, (13, 171, 255))
        PLAY4 = font2.render("Press 4 to play coop", True, (13, 171, 255))
        Screen.blit(SNAKE, (240, 100))
        Screen.blit(PLAY1, (230, 265))
        Screen.blit(PLAY2, (205, 310))
        Screen.blit(PLAY3, (230, 355))
        Screen.blit(PLAY4, (280, 400))
        pygame.display.flip()
        Screen.fill((0,255,102))
    return choose

def game_over():
    Screen.fill((60, 170, 60))
    GAME_OVER = font1.render('GAME OVER!', True, (212, 75, 75))
    Screen.blit(GAME_OVER, (240,200))
    if choose != 4:
        my_score = font2.render('Total score: ' + str(Score), True, (255, 255, 255))
        Screen.blit(my_score, (300, 280))
    else:
        my_score1 = font2.render('Total score of 1st player: ' + str(Score) ,True, (255,255,255))
        my_score2 = font2.render('Total score of 2nd player: ' + str(Score2) ,True, (255,255,255))
        Screen.blit(my_score1, (220, 280))
        Screen.blit(my_score2, (210, 340))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    
def save_game():
    f = open("save", "w")
    if choose != 4:
        snake_save_game = {
            "Elements": snake1.element,
            "dx": snake1.dx,
            "dy": snake1.dy,
            "level": choose
        }
    else:
        snake_save_game = {
            "Elements": snake1.element,
            "Elements2": snake2.element,
            "dx": snake1.dx,
            "dx2": snake2.dx,
            "dy": snake1.dy,
            "dy2": snake2.dy,
            "level": choose
        }
    y = json.dumps(snake_save_game)
    f.write(y)
    f.close()

choose = menu()

pygame.display.flip()

tamak = eda()
#____________________EASY_LEVEL_____________
if choose == 1:
    F = [[100,100],[95,100],[90,100]]
    snake1 = Snake((0,0,255),F)
    while running:
        for i in range(len(snake1.element)-1):
            if snake1.element[0] == snake1.element[i+1]:
                game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_game()
                    running = False
                if event.key == pygame.K_RIGHT and snake1.dx != -5:
                    snake1.dx = 5
                    snake1.dy = 0
                if event.key == pygame.K_LEFT and snake1.dx != 5:
                    snake1.dx = -5
                    snake1.dy = 0
                if event.key == pygame.K_UP and snake1.dy != 5:
                    snake1.dx = 0
                    snake1.dy = -5
                if event.key == pygame.K_DOWN and snake1.dy != -5:
                    snake1.dx = 0
                    snake1.dy = 5
        Screen.fill((0,204,255))
        snake1.draw()
        snake1.move()
        tamak.draw()
        FramePerSec.tick(FPS)
        for i in range(0,HEIGHT, 64):
            Screen.blit(brick,(0,i))
            Screen.blit(brick,(740,i))
        for i in range(64,WIDTH,64):
            Screen.blit(brick,(i,0))
            Screen.blit(brick,(i,540))
        if snake1.element[0][1] > tamak.y-5 and snake1.element[0][1] <tamak.y+5:
            if snake1.element[0][0] > tamak.x-5 and snake1.element[0][0] < tamak.x+5:
                Score += 1
                tamak.x = random.randint(100,600)
                tamak.y = random.randint(100,500)
                snake1.element.append([0,0])
    
        if snake1.element[0][0] < 64 or snake1.element[0][0] > 740 or snake1.element[0][1] < 64 or snake1.element[0][1] > 540:
            game_over()
    
        SCORE = font.render("Score " + str(Score), True, (255, 180, 0))
        Screen.blit(SCORE, (70,70))
        pygame.display.flip()

#____________________MEDIUM_LEVEL_____________
elif choose == 2:
    F = [[190, 170], [185,170], [180,170]]
    snake1 = Snake((0,0,255), F)
    while running:
        for i in range(len(snake1.element)-1):
            if snake1.element[0] == snake1.element[i+1]:
                game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_game()
                    running = False
                if event.key == pygame.K_RIGHT and snake1.dx != -7:
                    snake1.dx = 7
                    snake1.dy = 0
                if event.key == pygame.K_LEFT and snake1.dx != 7:
                    snake1.dx = -7
                    snake1.dy = 0
                if event.key == pygame.K_UP and snake1.dy != 7:
                    snake1.dx = 0
                    snake1.dy = -7
                if event.key == pygame.K_DOWN and snake1.dy != -7:
                    snake1.dx = 0
                    snake1.dy = 7
        Screen.fill((0,204,255))
        snake1.draw()
        snake1.move()
        tamak.draw()
        FramePerSec.tick(FPS)
        for i in range(0,HEIGHT, 64):
            Screen.blit(brick,(0,i))
            Screen.blit(brick,(740,i))
        for i in range(64,WIDTH,64):
            Screen.blit(brick,(i,0))
            Screen.blit(brick,(i,540))
        if snake1.element[0][1] > tamak.y-5 and snake1.element[0][1] <tamak.y+5:
            if snake1.element[0][0] > tamak.x-5 and snake1.element[0][0] < tamak.x+5:
                Score += 1
                tamak.x = random.randint(200,500)
                tamak.y = random.randint(200,400)
                snake1.element.append([0,0])
    
        if snake1.element[0][0] < 64 or snake1.element[0][0] > 740 or snake1.element[0][1] < 64 or snake1.element[0][1] > 540:
            game_over()
    
        SCORE = font.render("Score " + str(Score), True, (255, 180, 0))
        Screen.blit(SCORE, (150,70))
        pygame.display.flip()


#____________________HARD_LEVEL_____________
elif choose == 3:# ne zakoncheno
    F = [[190, 170], [185,170], [180,170]]
    snake1 = Snake((0,0,255), F)
    while running:
        for i in range(len(snake1.element)-1):
            if snake1.element[0] == snake1.element[i+1]:
                game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_game()
                    running = False
                if event.key == pygame.K_RIGHT and snake1.dx != -9:
                    snake1.dx = 9
                    snake1.dy = 0
                if event.key == pygame.K_LEFT and snake1.dx != 9:
                    snake1.dx = -9
                    snake1.dy = 0
                if event.key == pygame.K_UP and snake1.dy != 9:
                    snake1.dx = 0
                    snake1.dy = -9
                if event.key == pygame.K_DOWN and snake1.dy != -9:
                    snake1.dx = 0
                    snake1.dy = 9
        Screen.fill((0,204,255))
        snake1.draw()
        snake1.move()
        tamak.draw()
        FramePerSec.tick(FPS)
        for i in range(0,HEIGHT, 64):
            Screen.blit(brick,(0,i))
            Screen.blit(brick,(740,i))
        for i in range(64,WIDTH,64):
            Screen.blit(brick,(i,0))
            Screen.blit(brick,(i,540))
        if snake1.element[0][1] > tamak.y-5 and snake1.element[0][1] <tamak.y+5:
            if snake1.element[0][0] > tamak.x-5 and snake1.element[0][0] < tamak.x+5:
                Score += 1
                tamak.x = random.randint(200,500)
                tamak.y = random.randint(200,400)
                snake1.element.append([0,0])
    
        if snake1.element[0][0] < 64 or snake1.element[0][0] > 740 or snake1.element[0][1] < 64 or snake1.element[0][1] > 540:
            game_over()
    
        SCORE = font.render("Score " + str(Score), True, (255, 180, 0))
        Screen.blit(SCORE, (150,70))
        pygame.display.flip()


#____________________COOP_LEVEL_____________
elif choose == 4:
    F = [[190, 170], [185,170], [180,170]]
    D = [[190, 200], [185,200], [180,200]]
    snake1 = Snake((0,0,255), F)
    snake2 = Snake((0,255,0), D)
    global Score2
    Score2 = 0
    death_of_1st_player = False
    death_of_2nd_player = False 
    while running:
        for i in range(len(snake1.element)-1):
            if snake1.element[0] == snake1.element[i+1]:
                death_of_1st_player = True
        for i in range(len(snake2.element)-1):
            if snake2.element[0] == snake2.element[i+1]:
                death_of_2nd_player = True
        for i in snake1.element:
            if i == snake2.element[0]:
                game_over()
        for i in snake2.element:
            if i == snake1.element[0]:
                game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_game()
                    running = False
                if event.key == pygame.K_RIGHT and snake1.dx != -5:
                    snake1.dx = 5
                    snake1.dy = 0
                if event.key == pygame.K_LEFT and snake1.dx != 5:
                    snake1.dx = -5
                    snake1.dy = 0
                if event.key == pygame.K_UP and snake1.dy != 5:
                    snake1.dx = 0
                    snake1.dy = -5
                if event.key == pygame.K_DOWN and snake1.dy != -5:
                    snake1.dx = 0
                    snake1.dy = 5
                if event.key == pygame.K_d and snake2.dx != -5:
                    snake2.dx = 5
                    snake2.dy = 0
                if event.key == pygame.K_a and snake2.dx != 5:
                    snake2.dx = -5
                    snake2.dy = 0
                if event.key == pygame.K_w and snake2.dy != 5:
                    snake2.dx = 0
                    snake2.dy = -5
                if event.key == pygame.K_s and snake2.dy != -5:
                    snake2.dx = 0
                    snake2.dy = 5
        Screen.fill((0,204,255))
        if not death_of_1st_player:
            snake1.draw()
            snake1.move()
        if not death_of_2nd_player:
            snake2.draw()
            snake2.move()
        tamak.draw()
        FramePerSec.tick(FPS)
        for i in range(0,HEIGHT, 64):
            Screen.blit(brick,(0,i))
            Screen.blit(brick,(740,i))
        for i in range(64,WIDTH,64):
            Screen.blit(brick,(i,0))
            Screen.blit(brick,(i,540))
        if snake1.element[0][1] > tamak.y-5 and snake1.element[0][1] <tamak.y+5:
            if snake1.element[0][0] > tamak.x-5 and snake1.element[0][0] < tamak.x+5:
                Score += 1
                tamak.x = random.randint(200,500)
                tamak.y = random.randint(200,400)
                snake1.element.append([0,0])
        if snake2.element[0][1] > tamak.y-5 and snake2.element[0][1] <tamak.y+5:
            if snake2.element[0][0] > tamak.x-5 and snake2.element[0][0] < tamak.x+5:
                Score2 += 1
                tamak.x = random.randint(200,500)
                tamak.y = random.randint(200,400)
                snake2.element.append([0,0])
        if snake1.element[0][0] < 64 or snake1.element[0][0] > 740 or snake1.element[0][1] < 64 or snake1.element[0][1] > 540:
            death_of_1st_player = True
        if snake2.element[0][0] < 64 or snake2.element[0][0] > 740 or snake2.element[0][1] < 64 or snake2.element[0][1] > 540:
            death_of_2nd_player = True
        SCORE = font.render("Score of 1st player " + str(Score), True, (255, 180, 0))
        SCORE2 = font.render("Score of 2st player " + str(Score2), True, (0, 204, 0))
        Screen.blit(SCORE, (150,70))
        Screen.blit(SCORE2, (500,70))
        if death_of_1st_player and death_of_2nd_player:
            game_over()
        pygame.display.flip()