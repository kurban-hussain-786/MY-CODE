import pygame
from pygame.locals import *
import random
import time
import os
import psreadline
pygame.init()

white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)
clock=pygame.time.Clock()
# screen info
screen_widht=1000
screen_hieght=500
screen=pygame.display.set_mode((screen_widht,screen_hieght))
pygame.display.set_caption("kurban 3 game")
fps=60
x=30
y=40
w1=100
h1=100
x_vol=0
y_vol=0
x1=400
y1=40
w2=90
h2=90
player1=pygame.image.load("C:\\Users\\Lenovo\\Desktop\\python program\\pics\\NR1.png")



player1_spite_stand=player1

player1_walkright=[pygame.image.load("NR2.png"),pygame.image.load("NR2.png"),pygame.image.load("NR3.png"),pygame.image.load("NR3.png"),pygame.image.load("NR2.png"),pygame.image.load("NR2.png"),pygame.image.load("NR3.png")]
player1_walkleft=[pygame.image.load("NL2.png"),pygame.image.load("NL2.png"),pygame.image.load("NL3.png"),pygame.image.load("NL3.png"),pygame.image.load("NL3.png"),pygame.image.load("NL2.png"),pygame.image.load("NL2.png"),]
player1_walkright_point=0
player1_walkleft_point=0
player1_right=False
player1_left=False
NL1=pygame.image.load("NL1.png")
player1_left_stand=False
player1_right_stand=False
hit=pygame.image.load("C:\\Users\\Lenovo\\Desktop\\python program\\pics\\hit image.png")

hit=pygame.transform.scale(hit,(300,300))
player2=pygame.image.load("C:\\Users\\Lenovo\\Desktop\\python program\\pics\\NR1.png")
font=pygame.font.SysFont(None, 20)
boom=pygame.image.load("C:\\Users\\Lenovo\\Desktop\\python program\\pics\\isprite boom.png")
boom=pygame.transform.scale(boom,(100,100))
boom_x=0

boom_y=y
boom_x_vol=4
boom_attack="load"
def boom1(boom_x,boom_y):
    global boom_attack
    boom_attack="fired"
    
def button(bx,by,text):
    pygame.draw.rect(screen, black, (bx,by,100,40))
    text1=font.render(text, True, red)
    screen.blit(text1,(bx,by) )
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if bx<mouse[0]<bx+94 and by<mouse[1]<by+37:
        pygame.draw.rect(screen, (128,128,128), (bx,by,100,40))
        text1=font.render(text, True, white)
        screen.blit(text1, (bx,by))
        
        if click==(0,0,1):
            print("right ok") 
    
    
    

        
while True:
    

    

     
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
        if event.type==pygame.KEYDOWN:
            
            if event.key==pygame.K_RIGHT:
                x_vol=4
                y_vol=0
                game=True
                player1_right=True
                player1_left=False
                
            elif event.key==pygame.K_LEFT:
                x_vol=-4
                y_vol=0
                player1_right=False
                player1_left=True
            elif event.key==pygame.K_UP:
                y_vol=-1
                x_vol=0
            elif event.key==pygame.K_DOWN:
                y_vol=1
                x_vol=0

            if event.key==pygame.K_s:

                if boom_attack=="load":
                    boom_x=x
                    boom1(boom_x,boom_y)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                x_vol=0
                y_vol=0
                game=True
                player1_right=False
                player1_left=False
                player1_spite_stand=player1
                player1_right_stand=True
                
            elif event.key==pygame.K_LEFT:
                x_vol=0
                y_vol=0
                player1_right=False
                player1_left=False
                player1_left_stand=True
                player1_spite_stand=NL1
            elif event.key==pygame.K_UP:
                x_vol=0
                y_vol=0
            elif event.key==pygame.K_DOWN:
                x_vol=0
                y_vol=0
    x+=x_vol
    y+=y_vol
    if boom_attack=="fired":
        print("it work")
        screen.blit(boom,(boom_x,boom_y))

    screen.fill(white)
    button(100,40,'play')
    screen.blit(player2, (x1,y1))
    
    if abs(boom_x-x1)<90 and abs(boom_y-y1)<90:  
        screen.blit(hit,(random.randint(x1,x1)-100,random.randint(y1,y1)-100))           
        print("ha ha ha ha ")
        
    
        boom=pygame.transform.scale(boom,(100,100)) 
    
    if player1_walkright_point>=6:
        player1_walkright_point=0
        
    if player1_right:
        player1_walkright_point+=1
        screen.blit(player1_walkright[player1_walkright_point],(x,y))
        print("ok")
    elif player1_left:
        player1_walkright_point+=1
        screen.blit(player1_walkleft[player1_walkright_point],(x,y))
    else:
        screen.blit(player1_spite_stand,(x,y))
        print("it work")
        if player1_left_stand:
            screen.blit(player1_spite_stand,(x,y))
            print("ha ha ha ha ha ")
        elif player1_right_stand:
            screen.blit(player1_spite_stand,(x,y))
    r1=pygame.draw.rect(screen, black,(x,y,w1,h1),1)
    pygame.draw.rect(screen,red , (x1,y1,w2,h2),1)
    
    if abs(x-x1)<90 and abs(y-y1)<90:
        x-=10
        y-=10
        print("yes it work ")
        
    elif not abs(x-x1)<90:
        pass
    clock.tick(fps)
    pygame.display.update()



pygame.quit()
quit()