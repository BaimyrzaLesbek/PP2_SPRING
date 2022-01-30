import pygame
import random
import time
FPS = 60
pygame.init()
FramePerSec = pygame.time.Clock()
pygame.font.init()
font1 = pygame.font.SysFont("Impact", 72)
font2 = pygame.font.SysFont("Impact", 25)
font3 = pygame.font.SysFont("Impact", 20)
Game_Over = font1.render("Game Over", True, (0,0,0))
Coins_counter = font3.render("Coins", True, (0,0,0))
Score_show = font2.render("Your total score: ", True, (0,0,0))

size = weight, height = (400, 600)
screen = pygame.display.set_mode(size)

background = pygame.image.load("./Materials/AnimatedStreet.png")
Player = pygame.image.load("./Materials/Player.png")
Enemy = pygame.image.load("./Materials/Enemy.png")
Coin = pygame.image.load("./Materials/Coin.png")
Coins = pygame.image.load("./Materials/Coins.png")
pygame.mixer.music.load("./Materials/background.wav")
pygame.mixer.music.play(-1)



#Variables and values
Player_x = 200
Player_dx = 6
Player_y = 500
Enemy_x = random.randint(20,300)
Enemy_y = 20
Enemy_dy = 10
Coin_x = random.randint(20,300)
Coin_y = 20
Coin_dy =10
counter = 0

def show_player(x,y):
    screen.blit(Player,(x,y))
def show_enemy(x,y):
    screen.blit(Enemy,(x,y))
def show_coin(x,y):
    screen.blit(Coin,(x,y))

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        Player_x -= Player_dx
    elif pressed[pygame.K_RIGHT]:
        Player_x += Player_dx
    
    #showing players, background, coin, enemy
    screen.blit(background,(0,0))
    show_player(Player_x,Player_y)
    show_enemy(Enemy_x,Enemy_y)
    show_coin(Coin_x,Coin_y)
    Coins_counter1 = font3.render(str(counter), True, (0,0,0)) #shows how many coins you have
    screen.blit(Coins_counter,(300,20))
    screen.blit(Coins_counter1,(350,20))

    Coin_dy = Enemy_dy
    Enemy_y += Enemy_dy
    Coin_y += Coin_dy

    if Enemy_y > 600: # if enemy drive outside map
        Enemy_x = random.randint(20,300)
        Enemy_y = 20
        Enemy_dy = random.randint(5,10)
    if Coin_y > 600: # if coin occure outside map
        Coin_x = random.randint(20,300)
        Coin_y = 20
    
    if Player_y < (Coin_y+65):
        if ((Player_x>Coin_x) and (Player_x<Coin_x+65)) or ((Player_x+45>Coin_x) and (Player_x+45<Coin_x+65)):
            pygame.mixer.Sound("./Materials/Coin_updated.mp3").play()
            counter += 1
            Coin_y = 20
            Coin_x = random.randint(20,300)
    
    if Player_y < (Enemy_y+80): #death of player if collision between enemy and player
        if ((Player_x>Enemy_x) and (Player_x<Enemy_x+45)) or ((Player_x+45>Enemy_x) and (Player_x+45<Enemy_x+45)):
            pygame.mixer.music.pause()
            pygame.mixer.Sound("./Materials/crash.wav").play()
            time.sleep(1)
            screen.fill((255,255,0))
            screen.blit(Game_Over, (45,200))
            screen.blit(Score_show, (100, 300))
            screen.blit(Coins_counter1, (280, 304))
            pygame.display.flip()
            Player_dx = 0
            Enemy_dy = 0
            Coin_dy = 0
            time.sleep(3)
            pygame.quit()
    
    if Player_x<0 or Player_x>370: #death of player if player drive outside of map
        pygame.mixer.music.pause()
        pygame.mixer.Sound("./Materials/crash.wav").play()
        time.sleep(1)
        screen.fill((255,255,0))
        screen.blit(Game_Over, (45,200))
        screen.blit(Score_show, (100, 300))
        screen.blit(Coins_counter1, (280, 304))
        pygame.display.flip()
        Player_dx = 0
        Enemy_dy = 0
        Coin_dy = 0
        time.sleep(3)
        pygame.quit()
    if counter>=3:
        Enemy_dy=100
    pygame.display.flip()
    FramePerSec.tick(FPS)
