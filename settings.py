class Settings():
    '''储存《外星人入侵》的所有设置的类'''
    
    def __init__(self):
        '''初始化游戏设置'''
        #屏幕设置
        self.screen_width=1200
        self.screen_height=600
        self.bg_color=(230,230,230)
        #飞船的设置
        self.ship_speed_factor=3
        #球的设置
        self.ball_speed_factor=2
        self.ball_limit=3#等于1就正常运行3就不行
        
    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)
