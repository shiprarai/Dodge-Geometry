import pygame
import time
import random

pygame.init()
black=(0,0,0)
white=(255,255,255)

bright_red=(255,0,0)
blue=(0,0,255)
bright_green=(0,255,0)
red=(200,0,0)
green=(0,200,0)

rec=(203,64,223)
#circ=(189,88,21)
sq=(146,192,160)
elli=(180,206,89)
#tri=(228,67,99)

disp_width=800
disp_height=600
img_width=47
pause= False

G_display=pygame.display.set_mode((disp_width,disp_height))
pygame.display.set_caption("Geometry Game")
clock=pygame.time.Clock()
img= pygame.image.load("a.png")

def things_dodged(count):
    font=pygame.font.SysFont("comicsansms", 25)
    text=font.render("Dodged:  " +str(count), True, black)
    G_display.blit(text,(0,0))
    #if crash():
        #DodgedC(count)

def DodgedC(count):
    font=pygame.font.SysFont("comicsansms",20)
    text=font.render("Your score: " +str(count), True, blue)
    textSurf=(disp_width*0.45,disp_height*0.8)
    G_display.blit(text,textSurf)

    
def quitgame():
    pygame.quit()
    quit()
    
def paused():
    
    largeText = pygame.font.SysFont('comicsansms',110)
    textSurf,textRect= text_obj("Paused",largeText)
    textRect.center=((disp_width/2,disp_height/2))
    G_display.blit(textSurf,textRect)
               
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
       
        #DodgedC(dodged)
        button("Contd.." ,150,450,100,50,green,bright_green,unpause)
        button("quit!" , 550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)
    


def button(msg, x,y,w,h,ic,ac, action=None):
    mouse= pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w >mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(G_display,ac,(x,y,w,h))
        if click[0]==1 and action!= None:
            action()
    else:
        pygame.draw.rect(G_display,ic,(x,y,w,h))
    smallText= pygame.font.SysFont("comicsansms", 20)
    textSurf,textRect=text_obj(msg,smallText)
    textRect.center=((x+(w/2)),(y+(h/2)))
    G_display.blit(textSurf,textRect)

def Rect(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(G_display,color,[thingx,thingy,thingw,thingh])

'''def Circle(thingx,thingy,radius,color):
    pygame.draw.circle(G_display,color,[thingx,thingy],radius)'''

def Ellipse(thingx,thingy,thingh,thingw,color):
    pygame.draw.ellipse(G_display,color,[thingx,thingy,thingh,thingw])

'''def Triangle(x0,y0,x1,y1,x2,y2):
    pygame.draw.polygon(G_display,color,[x0,y0,x1,y1,x2,y2])'''


def unpause():
    global pause
    pause= False                               
                                    

def text_obj(text,font):
    textSurface= font.render(text,True,black)
    return textSurface, textSurface.get_rect()



def crash(count):
    
    G_display.fill(white)
    largeText = pygame.font.SysFont('comicsansms',80)
    textSurf,textRect= text_obj("Gotcha!!",largeText)
    textRect.center=((disp_width/2,disp_height/2))
    G_display.blit(textSurf,textRect)
    
      
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #G_display.fill(white)
        
        button("Play again" ,150,450,150,50,green,bright_green,game_loop)
        button("quit!" , 550,450,100,50,red,bright_red,quitgame)

        font=pygame.font.SysFont("comicsansms",30)
        text=font.render("Your Score: " +str(count), True, blue)
        textSurf=(disp_width*0.35,disp_height*0.6)
        G_display.blit(text,textSurf)
        pygame.display.update()
        clock.tick(15)

def A(x,y):
    G_display.blit(img,(x,y))


    
def game_intro():
    
    intro = False
    while not intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        G_display.fill(white)
        largeText = pygame.font.SysFont('comicsansms',80)
        textSurf,textRect= text_obj("Dodge Geometry",largeText)
        textRect.center=((disp_width/2,disp_height/2))
        G_display.blit(textSurf,textRect)
        button("Go!" ,150,450,100,50,green,bright_green,game_loop)
        button("quit!" , 550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
   
    thing_starty= -600
    thing_starty1=-200
    th_y= -800
    thing_w=150
    thing_h=100
    thing_w1=100
    thing_h1=100

    thing_startx= random.randrange(0,disp_width-thing_w)
    thing_startx1= random.randrange(0,disp_width-thing_w1)
    the_x=random.randrange(0,disp_width-thing_w)
    thing_speed=7
    x_change=0
    x=(disp_width*0.45)
    y= (disp_height*0.78)
    dodged=0
    dodgedS=0
    dodgedR=0
    dodgedE=0


    gamExit= False
    while not gamExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change= -5
                if event.key==pygame.K_RIGHT:
                    x_change= 5
                if event.key==pygame.K_p:
                    pause=True
                    paused()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
        x+= x_change
        G_display.fill(white)
        #things(thingx,thingy,rhingw,thingh,color)

        Rect(thing_startx,thing_starty,thing_w,thing_h,rec)

        Rect(thing_startx1,thing_starty1,thing_w1,thing_h1,sq)

        Ellipse(the_x,th_y,thing_w,thing_h,elli)

        thing_starty+=thing_speed
        thing_starty1+=thing_speed
        th_y+= thing_speed

        A(x,y)

        things_dodged(dodged)

        if x>disp_width-img_width or x<0:
            crash()
        
        if thing_starty>disp_height:
            thing_starty=0-thing_h
            thing_startx =random.randrange(0,disp_width)
            dodgedR+=1
            thing_speed+= 1

        if thing_starty1>disp_height:
            thing_starty1=0-thing_h1
            thing_startx1 =random.randrange(0,disp_width)
            dodgedS+=1
            thing_speed+= 1

        if th_y>disp_height:
            th_y=0-thing_h
            the_x =random.randrange(0,disp_width)
            dodgedE+=1
            thing_speed+= 1
            
        dodged= dodgedS+dodgedR+dodgedE    

        if y<thing_starty+thing_h:
            if x>thing_startx and x<thing_startx+thing_w or x+img_width> thing_startx and x+img_width<thing_startx + thing_w:
                crash(dodged)
                #DodgedC(dodged)

        if y<thing_starty1+thing_h1:
            if x>thing_startx1 and x<thing_startx1+thing_w1 or x+img_width> thing_startx1 and x+img_width<thing_startx1 + thing_w1:
                crash(dodged)
                #DodgedC(dodged)
        if y<th_y+thing_h:
            if x>the_x and x<the_x+thing_w or x+img_width> the_x and x+img_width<the_x + thing_w:
                crash(dodged)
                #DodgedC(dodged)
           
        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()
