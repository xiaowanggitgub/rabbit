

class Stats():
    '''统计未接到次数'''
    def __init__(self,ai_settings):
        '''初始化属性'''
        self.ai_settings=ai_settings
        self.reset_stats(ai_settings)#调用自己的方法
        self.game_active=False
        
    def reset_stats(self,ai_settings):
        '''重置游戏统计信息'''
        self.rest_number=3
                        
