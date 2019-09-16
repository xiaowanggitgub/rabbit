import sys

import pygame

from ball import Ball
        
def check_events(ai_settings,stats,button,ship,balls):
    '''响应按键和鼠标事件'''
    #监视鼠标和电脑事件
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:#鼠标点击关闭窗口
            sys.exit()#退出程序
            
            #监测按键
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,stats,ship,balls,ai_settings)
                
               #监测松键
        elif event.type==pygame.KEYUP: 
            check_keyup_events(event,ship)
            
        elif event.type==pygame.MOUSEBUTTONDOWN:#点击屏幕行为
            mouse_x,mouse_y=pygame.mouse.get_pos()#它返回一个元组，其中包含玩家单击时鼠标的x 和y 坐标
            check_play_button(ai_settings,stats,button,ship,balls,mouse_x,mouse_y)

def check_keydown_events(event,stats,ship,balls,ai_settings):
    '''响应按键'''
                
                #按下右键时，飞船连续移动开关打开
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
                
                #按下左键时，飞船连续移动开关打开
    if event.key==pygame.K_LEFT:
        ship.moving_left=True
        
    if event.key==pygame.K_UP:
        ship.moving_top=True
        
    if event.key==pygame.K_DOWN:
        ship.moving_bottom=True
        
    if event.key==pygame.K_q:
        sys.exit() 
        
    if event.key==pygame.K_p:
        start_game(stats,ship,balls,ai_settings)
           
        
def check_keyup_events(event,ship):
    '''响应松开'''
     #松开右键时，飞船连续移动开关关闭
    if  event.key==pygame.K_RIGHT:
        ship.moving_right=False
    #松开左键时，飞船连续移动开关关闭
    if  event.key==pygame.K_LEFT:
        ship.moving_left=False
        
    if event.key==pygame.K_UP:
        ship.moving_top=False
        
    if event.key==pygame.K_DOWN:
        ship.moving_bottom=False
    
                    
def update_screen(button,stats,ship):
    '''更新屏幕上的图像并切换到新屏幕'''
    #每次循环时都重绘屏幕
    

    
    ship.blitme()   
    
    if not stats.game_active:
        
        button.draw_button()#为了让按钮处于屏幕顶层，绘制完其他元素再绘制按钮
    

def create_ball(screen,ai_settings,balls):
    if len(balls)==0:
        ball=Ball(screen,ai_settings)
        balls.add(ball)
        
    else:
        pass

def count_ball_limit(stats,ball,balls):
    '''统计是否超过限定未接到球次数，如果超过停止游戏'''
    for ball in balls.sprites():#遍历精灵的rect和image要加.sprites()
        if ball.rect.y ==ball.screen_rect.bottom:#ball.rect.bottom==ball.screen_rect.bottom
            stats.rest_number-=1 #未接到一个球后就结束游戏，改为现在这样或者ball.rect.bottom==600可按预期运行
            ball.remove(balls)
    if stats.rest_number==0:
        stats.game_active=False

def check_active(screen,ai_settings,balls,stats,ship,ships,ball):
    '''检查游戏运行状态'''
    ship.update()
    
    #创建一个球
    create_ball(screen,ai_settings,balls)
    #更新精灵组中每个球的位置
    update_balls(ai_settings,balls)
    #画球
    balls.draw(screen)
    #检测碰撞，删除接到的球
    check_collisions(balls,ships)
    #统计是否超过限定未接到球次数，如果超过停止游戏
    count_ball_limit(stats,ball,balls)
    
    
            
def check_collisions(balls,ships):
    '''检查碰撞，删除碰撞的球'''
    collisions = pygame.sprite.groupcollide(balls,ships,True,False)

def update_balls(ai_settings,balls):
    '''更新精灵组内的每个精灵位置'''
    for ball in balls:
        ball.update(ai_settings)
        
def start_game(stats,ship,balls,ai_settings):
    '''开始游戏'''
        #隐藏光标
    if stats.game_active:
        pygame.mouse.set_visible(False)
        #重置游戏统计信息                                  
    stats.reset_stats(ai_settings)
    stats.game_active=True

    #清空球列表
    balls.empty()
    #让飞船居中
    ship.center_ship()
    
def check_play_button(ai_settings,stats,button,ship,balls,mouse_x,mouse_y):
    '''在玩家单击play按钮时开始新游戏'''
    #测试点是否在矩形内，前面需要一个rect对象，检测点是否在其内
    button_clicked=button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active: #如果游戏在运行点击play区域也不会重置信息                   
        start_game(stats,ship,balls,ai_settings)
