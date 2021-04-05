import pygame,math
pygame.font.init()

size = weight, height = (800, 600)
screen = pygame.display.set_mode(size)

screen.fill((255,255,255))

x1=400
coord_x = 40
Dx = 1

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen,(0,0,0),[40,40,720,500],3)
    #center(400,290)
    pygame.draw.line(screen,(0,0,0),[40,290],[760,290],2)#origin line of x 
    pygame.draw.line(screen,(0,0,0),[400,40],[400,540],2)#origin line of y
    
    pygame.draw.line(screen, (0,0,0), (500,40), (500,540))
    pygame.draw.line(screen, (0,0,0), (600,40), (600,540))
    pygame.draw.line(screen, (0,0,0), (700,40), (700,540))

    pygame.draw.line(screen, (0,0,0), (300,40), (300,540))
    pygame.draw.line(screen, (0,0,0), (200,40), (200,540))
    pygame.draw.line(screen, (0,0,0), (100,40), (100,540))

    pygame.draw.line(screen, (0,0,0), (40,290+50), (760,290+50))
    pygame.draw.line(screen, (0,0,0), (40,290+100), (760,290+100))
    pygame.draw.line(screen, (0,0,0), (40,290+150), (760,290+150))
    pygame.draw.line(screen, (0,0,0), (40,290+200), (760,290+200))

    pygame.draw.line(screen, (0,0,0), (40,290-50), (760,290-50))
    pygame.draw.line(screen, (0,0,0), (40,290-100), (760,290-100))
    pygame.draw.line(screen, (0,0,0), (40,290-150), (760,290-150))
    pygame.draw.line(screen, (0,0,0), (40,290-200), (760,290-200))

    
    while coord_x>=40 and coord_x<=760:
        if coord_x%4==0:
            pygame.draw.line(screen,(255,255,255),(coord_x, -1 * (math.cos((coord_x-400) / 32))*200 + 290),(coord_x+Dx , -1 * (math.cos ((coord_x+Dx-400) / 32))*200 + 290))
        else:
            pygame.draw.line(screen,(0,0,255),(coord_x, -1 * (math.cos((coord_x-400) / 32))*200 + 290),(coord_x+Dx , -1 * (math.cos ((coord_x+Dx-400) / 32))*200 + 290))
        pygame.draw.line(screen,(255,0,0),(coord_x, -1 * (math.sin((coord_x-400) / 32))*200 + 290),(coord_x+Dx , -1 * (math.sin ((coord_x+Dx-400) / 32))*200 + 290))
        coord_x+=Dx


    font1 = pygame.font.Font(None, 23)
    num1 = font1.render("0", False, (0,0,0))
    num2 = font1.render("0.25", False, (0,0,0))
    num3 = font1.render("0.50", False, (0,0,0))
    num4 = font1.render("0.75", False, (0,0,0))
    num5 = font1.render("1", False, (0,0,0))
    num6 = font1.render("-0.25", False, (0,0,0))
    num7 = font1.render("-0.5", False, (0,0,0))
    num8 = font1.render("-0.75", False, (0,0,0))
    num9 = font1.render("-1", False, (0,0,0))
    screen.blit(num1,(30,290))
    screen.blit(num2,(10,290-50))
    screen.blit(num3,(10,290-100))
    screen.blit(num4,(10,290-150))
    screen.blit(num5,(30,290-200))
    screen.blit(num6,(10,290+50))
    screen.blit(num7,(10,290+100))
    screen.blit(num8,(10,290+150))
    screen.blit(num9,(20,290+200))

    num10 = font1.render("0", False,(0,0,0))
    num11 = font1.render("pi/2", False, (0,0,0))
    num12 = font1.render("pi", False, (0,0,0))
    num13 = font1.render("3*pi/2", False, (0,0,0))
    num14 = font1.render("2*pi", False, (0,0,0))
    num15 = font1.render("5*pi/2", False, (0,0,0))
    num16 = font1.render("3*pi", False, (0,0,0))
    num17 = font1.render("-pi/2", False, (0,0,0))
    num18 = font1.render("-pi", False, (0,0,0))
    num19 = font1.render("-3*pi/2", False, (0,0,0))
    num20 = font1.render("-2*pi", False, (0,0,0))
    num21 = font1.render("-5*pi/2", False, (0,0,0))
    num22 = font1.render("-3*pi", False, (0,0,0))
    screen.blit(num10,(397,543))
    screen.blit(num11,(440,543))
    screen.blit(num12,(497,543))
    screen.blit(num13,(540,543))
    screen.blit(num14,(597,543))
    screen.blit(num15,(640,543))
    screen.blit(num16,(697,543))
    screen.blit(num17,(347,543))
    screen.blit(num18,(297,543))
    screen.blit(num19,(235,543))
    screen.blit(num20,(190,543))
    screen.blit(num21,(136,543))
    screen.blit(num22,(89,543))

    for i in range(100, 750, 50):
        pygame.draw.line(screen, (0,0,0), (i,530),(i,540))
        pygame.draw.line(screen, (0,0,0), (i,40),(i,50))

    for i in range(67,550,50):
        pygame.draw.line(screen, (0,0,0), (40,i),(50,i))
        pygame.draw.line(screen, (0,0,0), (750,i),(760,i))
    
    for i in range(40,760,10):
        pygame.draw.line(screen,(0,0,0), (i,532),(i,540))
        pygame.draw.line(screen,(0,0,0), (i,40),(i,48))
    

    cos = font1.render("cos",False,(0,0,255))
    sin = font1.render("sin",False,(255,0,0))
    screen.blit(cos,(620,50))
    screen.blit(sin,(620,65))
    pygame.draw.line(screen,(0,0,255),(640,57),(643,57),1)
    pygame.draw.line(screen,(0,0,255),(646,57),(649,57),1)
    pygame.draw.line(screen,(0,0,255),(652,57),(655,57),1)
    pygame.draw.line(screen,(0,0,255),(658,57),(661,57),1)
    pygame.draw.line(screen,(255,0,0),(640,72),(660,72),1)

    pygame.display.flip()
pygame.quit()