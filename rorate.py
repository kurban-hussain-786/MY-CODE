import pygame
import random
import os 



pygame.init()
screen=pygame.display.set_mode((1000,500))
angle=0

hit=pygame.image.load(os.path.join("pics","shenron-dragon.png"))
hit=pygame.transform.scale(hit,(100,100))


game_exit3=False

while not game_exit3:
    angle+=1
    screen.fill((255,255,255))
    x,y=mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    screen.blit(pygame.transform.rotate(hit,angle),(x,y))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_exit3=True
    pygame.display.update()
pygame.quit()
quit()