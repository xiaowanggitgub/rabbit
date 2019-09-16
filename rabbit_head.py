import pygame

import sys

import rabbit_function as rf

from ship import Ship

from ball import Ball

from settings import Settings

from random import randint

from pygame.sprite import Group

from game_stats import Stats

from button import Button


screen=pygame.display.set_mode((1200,600))#创建一个窗口
pygame.display.set_caption('rabbit_head')#窗口名
ai_settings=Settings()    
balls=Group()
ships=Group()
ship=Ship(screen,ai_settings)
ships.add(ship)
ball=Ball(screen,ai_settings)
stats=Stats(ai_settings)
msg='play'
button=Button(ai_settings,screen,msg)
while True:
        
        #监视鼠标和电脑事件
    rf.check_events(ai_settings,stats,button,ship,balls)
    #背景色填充屏幕
    screen.fill(ai_settings.bg_color)
        
        #更新屏幕上的图像并切换到新屏幕        
    if stats.game_active:
        
        rf.check_active(screen,ai_settings,balls,stats,ship,ships,ball)
        
        
    rf.update_screen(button,stats,ship)    

    
    #让最近绘制的屏幕可见
    pygame.display.flip()
    



