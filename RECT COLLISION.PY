import pygame,sys,pygame.color,random
pygame.init()
black=(0,0,0)
screen=pygame.display.set_mode((500,500))
# rect collision
black=(182,130,0)
hero=pygame.image.load("C:\\Users\\Lenovo\\Desktop\\python program\\pics\\goku_stand.png")
hero=pygame.transform.scale(hero,(100,100))
x=50
y=100
x1=0
y1=0
run=False
# boom data
boom=pygame.image.load('isprite boom.png')

boom=pygame.transform.scale(boom,(100,100))

boom_x=50
boom_y=y
boom_x_vol=0.6
boom_attack="load"
left=False
right=False

def boom1(boom_x,boom_y):
    global boom_attack
    boom_attack="fired"
    screen.blit(boom,(boom_x,boom_y))
    
    pygame.display.update()
while not run:
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    screen.fill((255,255,120))
    enemy=pygame.draw.rect(screen,(255,255,255),(200,100,100,100))
    hero1=pygame.draw.rect(screen,black,(x,y,100,100))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=True
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                x1=0.1
                
            if event.key==pygame.K_LEFT:
                x1=-0.1
                
            if event.key==pygame.K_UP:
                y1=-0.1
            if event.key==pygame.K_DOWN:
                y1=0.1 

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                x1=0
                
            if event.key==pygame.K_LEFT:
                x1=-0
                
            if event.key==pygame.K_UP:
                y1=-0
            if event.key==pygame.K_DOWN:
                y1=0
            if event.key==pygame.K_s:
                if boom_attack=="load":
                    boom_x=x
                    boom_y=y
                    boom1(boom_x,boom_y)
    x+=x1
    y+=y1
    
    
    
    if hero1.colliderect(enemy):
        if hero1.right>=enemy.x and hero1.right<=enemy.x+5:
            x-=1
        elif hero1.left<=enemy.x+100 and hero1.left>=enemy.x+95:
            x+=1
        elif hero1.top<=enemy.y and hero1.top<=enemy.y+5:
            y-=1
        elif hero1.bottom>=enemy.y+100 and hero1.bottom>=enemy.y+105:
            y+=1
    if boom_x>=500:
        boom_attack="load"
    elif boom_x<=-500:
        boom_attack="load"
    if boom_attack=="fired":
        boom1(boom_x,boom_y)
        if right==True:
            boom_x+=boom_x_vol
        elif left==True:
            boom_x-=boom_x_vol  
            
    pygame.display.update()  
pygame.quit()
