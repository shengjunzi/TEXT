import pygame
import sys
from pygame.locals import *
#初始化
pygame.init()



size=width,height=1200,600
speed=[-2,3]

bg=(255,255,255)
clock=pygame.time.Clock()

#创建窗口大小
screen=pygame.display.set_mode(size,RESIZABLE)
#设置窗口标题
pygame.display.set_caption("hekko")

fullscreen=False

#加载图片
plane=pygame.image.load("plane.jpg")
    
#获得图片矩形
position=plane.get_rect()
l_head=plane
r_head=pygame.transform.flip(plane,True,False)

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                plane=l_head
                speed=[-1,0]
            if event.key==K_RIGHT:
                plane=r_head
                speed=[1,0]
            if event.key==K_UP:
                speed=[0,-1]
            if event.key==K_DOWN:
                speed=[0,1]
            if event.key==K_F11:
                fullscreen=not fullscreen
                if fullscreen:
                    screen=pygame.display.set_mode(pygame.display.list_modes()[0],FULLSCREEN|HWSURFACE)
                    width=pygame.display.list_modes()[0][0]
                    height=pygame.display.list_modes()[0][1]
                else:
                    screen=pygame.display.set_mode(size)
                if event.type==VIDEORESIZE:
                    size=event.size
                    width,height=size
                    screen=pygame.display.set_mode(size,RESIZABLE)
                    
                    
                    
    position=position.move(speed)

    if position.left<0 or position.right>width:
        plane=pygame.transform.flip(plane,True,False)
        speed[0]=-speed[0]
    if position.top<0 or position.bottom>height:
        speed[1]=-speed[1]
    screen.fill(bg)
    screen.blit(plane,position)
    pygame.display.flip()
    #pygame.time.delay(20)
    clock.tick(10)
    
