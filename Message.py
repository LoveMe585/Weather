# -*- coding:utf-8 -*-
# author = wulu 
# date = 2018/11/30

from Weather import *


class Message:

    #发给罗总的消息
    def sendLuo(self):

        #获取  鄂州 ： 562
        result = Weather().getNowWeaher('562')
        print(result)

        #姓名
        xingming = 'hi  罗总' + '\n'

        #基本信息
        ll = ('城市： ' + str(result['city']) + '\n' +
                    '天气情况： ' + str(result['condition']) + '\n' +
                    '当前温度： ' + str(result['temp']) + '\n' +
                    '体感温度： ' + str(result['realFeel']) + '\n' +
                    '温馨提示： ' + str(result['tips']) + '\n' )

        #针对提示
        ss = ('洗车等级：' + str(result['17']['level']) + '\n' +
              '洗车建议：' + str(result['17']['status']) + '\n' +
              '温馨提醒：' + str(result['17']['desc']))

        return xingming + ll + ss


    # 发给罗总的消息
    def sendXman(self):
        # 获取  鄂州 ： 562
        result = Weather().getNowWeaher('892')
        # print(result)

        # 姓名
        xingming = 'hi  小曼' + '\n'

        # 基本信息
        ll = ('城市： ' + str(result['city']) + '\n' +
              '天气情况： ' + str(result['condition']) + '\n' +
              '当前温度： ' + str(result['temp']) + '\n' +
              '体感温度： ' + str(result['realFeel']) + '\n' +
              '温馨提示： ' + str(result['tips']) + '\n')

        # 针对提示
        ss = ('化妆等级：' + str(result['7']['level']) + '\n' +
              '化妆建议：' + str(result['7']['status']) + '\n' +
              '化妆提醒：' + str(result['7']['desc']))

        return xingming + ll + ss



# print(Message().sendXman())