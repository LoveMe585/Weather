#!/usr/bin/python
# -*- coding: UTF-8 -*- 
# @Time = '2018/11/29'
# author = ‘wulu’


from wxpy import *
from Message import *


#进行登录
bot = Bot(console_qr=1, cache_path=True)
#启用puid
bot.enable_puid('wxpy_puid.pkl')

groups = bot.groups().search('今年贼吃鸡')[0]

message = Message()
ms = message.sendLuo()
groups.send(ms)
ms = message.sendXman()
groups.send(ms)

# luozong = group.search('罗正顺').
# print(luozong)


#123456