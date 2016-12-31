
import pygame
import time
import random
pygame.init()
breadth=800
length=600
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
bright_red=(200,0,0)
bright_green=(0,200,0)
blue=(0,0,255)
direction="right"

pygame.display.set_caption("snake game")
gameDisplay=pygame.display.set_mode((breadth,length))
appleimg=pygame.image.load("apple.png")
snakeimg=pygame.image.load("snake.png")
clock=pygame.time.Clock()
def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()



def game_intro():

        intro = True

        while intro:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            gameDisplay.fill(black)
            largeText = pygame.font.SysFont('calibri',80)
            TextSurf, TextRect = text_objects("Snake XENZIA", largeText)
            TextRect.center = ((breadth/2),(length/2))
            gameDisplay.blit(TextSurf, TextRect)
            button("start",200,500,50,50,green,bright_green,"play")
            button("quit",600,500,50,50,red,bright_red,"quit")
            pygame.display.update()
            clock.tick(15)
def eaten(cal):
    font=pygame.font.SysFont("calibri",40)
    text=font.render("score: "+str(cal),True,blue)
    gameDisplay.blit(text,(0,0))
    pygame.display.update()
            
def button(msg,x,y,b,l,ic,ac,action=None):
            mouse = pygame.mouse.get_pos()
            click=pygame.mouse.get_pressed()

            #print(mouse)

            if x+b > mouse[0] > x and y+l > mouse[1] > y:
                pygame.draw.rect(gameDisplay, ac,(x,y,b,l))
                if click[0]==1 and action!=None:
                    if action=="play":
                        game_loop()

                    
                    if action=="quit":
                        pygame.quit()
                        quit()
            else:
                pygame.draw.rect(gameDisplay, ic,(x,y,b,l))

            smalltext=pygame.font.SysFont("calibri",20)
            TextSurf,TextRect=text_objects(msg,smalltext)
            TextRect.center=((x+b/2),(y+l/2))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            
    

    
    

def crash():
        
        

       
        intro = True

        while intro:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            
            largeText = pygame.font.SysFont('calibri',115)
            TextSurf, TextRect = text_objects("you lost", largeText)
            TextRect.center = ((breadth/2),(length/2))
            gameDisplay.blit(TextSurf, TextRect)
            button("continue",200,500,80,50,green,bright_green,"play")
            button("quit",600,500,80,50,red,bright_red,"quit")
            
            pygame.display.update()
            clock.tick(15)

def snake(snakelist):
    
    if direction=="right":
        head=pygame.transform.rotate(snakeimg,270)
    if direction=="left":
        head=pygame.transform.rotate(snakeimg,90)
    if direction=="up":
        head=snakeimg
    if direction=="down":
        head=pygame.transform.rotate(snakeimg,180)
    gameDisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    for xy in snakelist[:-1]:
        pygame.draw.rect(gameDisplay,red,[xy[0],xy[1],20,20])
        
            

def game_loop():
            gameex=False
            x=600
            y=400
            global direction
            count=5
            eat=0
            count2=0
            snakelist=[]
            snakelen=1
            applex=round(random.randrange(0,breadth-40)/10)*10
            appley=round(random.randrange(0,length-40)/10)*10
            
            while not gameex:
                        for event in pygame.event.get():
                            if event.type==pygame.QUIT:
                                
                                pygame.quit()
                                quit
                            if event.type==pygame.KEYDOWN:
                                
                                if event.key==pygame.K_LEFT:
                                    count-=10
                                    count2=0
                                    direction="left"
                                elif event.key==pygame.K_RIGHT:
                                    count+=10
                                    count2=0
                                    direction="right"
                                elif event.key==pygame.K_UP:
                                    count2-=10
                                    count=0
                                    direction="up"
                                elif event.key==pygame.K_DOWN:
                                    count2+=10
                                    count=0
                                    direction="down"
                                
                        gameDisplay.fill(black)
                        eaten(eat)
                        
                       # pygame.draw.rect(gameDisplay,green,[applex,appley,20,20])
                        gameDisplay.blit(appleimg,(applex,appley))
                     
                        
                        if x>750 or x<0 or y>580 or y<0:
                            crash()
                        x+=count
                        y+=count2
                        if applex+20>x>applex or applex+20>=x+20>=applex:
                           if appley+20>y>appley or appley+20>y+20>appley:

                                applex=round(random.randrange(0,breadth-40)/10)*10
                                appley=round(random.randrange(0,length-40)/10)*10
                                eat+=1
                                snakelen+=2
                           
                        snakehead=[]
                        snakehead.append(x)
                        snakehead.append(y)
                        snakelist.append(snakehead)

                        snake(snakelist)
                        if len(snakelist)>snakelen:
                            del snakelist[0]
                        for seg in snakelist[:-1]:
                            if seg==snakehead:
                                crash()
                       
                           
                         
                        pygame.display.update()
                        
                        clock.tick(20)
game_intro()
game_loop()


























































































































































                
            



   
