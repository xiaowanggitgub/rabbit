import pygame
from pygame.sprite import Sprite
from random import randint
class Ball(Sprite):
    
    def __init__(self,screen,ai_settings):
        super(Ball, self).__init__()
        '''初始化小球,并设置其位置'''
        self.screen=screen
        self.ai_settings=ai_settings
        
        #加载球图像并获取其外接矩形
        self.image=pygame.image.load('images/ball.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #设置球的位置，随机出现在顶部
        self.rect.x=randint(0,1200)#球的X坐标随机
        self.rect.y= 0
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def update(self,ai_settings):#无
        '''更新球的位置'''
        self.rect.y+=ai_settings.ball_speed_factor
    
    def blitme(self):
        '''在指定位置绘制球'''
        self.screen.blit(self.image,self.rect)
