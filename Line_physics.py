import pygame
import sys
import random
import math
from pygame.locals import *
import time
import pymunk
import config
import pymunk.pygame_util
import os

pygame.init()

screen_widht=1000
screen_height=500
screen=pygame.display.set_mode((screen_widht,screen_height))
pygame.display.set_caption(" Line physics")
title_coin=pygame.image.load(os.path.join("goku_tittle.png"))


pygame.display.set_icon(title_coin)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)
gray=(128,128,128)
orange=(255,165,0)
yellow=(255,255,0)
game_exit3=False
clock=pygame.time.Clock()

# creat a space 
def draw(space,screen,options):
    screen.fill(white)
    space.debug_draw(options)
    
space=pymunk.Space()
space.gravity=0,1
options=pymunk.pygame_util.DrawOptions(screen)

# ball draw
def ball(space,pos):
    ball_body=pymunk.Body(body_type=pymunk.Body.DYNAMIC)
    ball_body.position=pos
    ball_body.mass=10
    ball_body.moment=1
    ball_shape=pymunk.Circle(ball_body,40)
    ball_shape.color=(0,255,0,255)
    ball_shape.elasticity=0.2
    ball_shape.friction=0.5
    space.add(ball_body,ball_shape)
    return ball_shape
balls=[]
# line draw
def line(space,pos):
    line_body=pymunk.Body(10,4,body_type=pymunk.Body.STATIC)
    line_shape=pymunk.Segment(line_body,(pos),(pos),10)
    line_shape.color=(255,0,0,0)
    
    line_shape.elasticity=0.5
    line_shape.friction=0.4
    space.add(line_body,line_shape)
    return line_shape
lines=[]


while not game_exit3:
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_exit3=True
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==3:
                balls.append(ball(space,event.pos))
            elif event.button==1:
                lines.append(line(space,event.pos))
                
    
                    
    
    draw(space,screen,options)
    
    space.step(1/50)
    pygame.display.update()
pygame.quit()
quit() 