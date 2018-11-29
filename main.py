#!/usr/bin/python
# -*- coding: UTF-8 -*- 
# @Time = '2018/11/29'
# author = ‘wulu’


from wxpy import *


#进行登录
bot = Bot(console_qr=True, cache_path=True)
#启用puid
bot.enable_puid('wxpy_puid.pkl')

groups = bot.groups().search('老铁2群')[0]

for group in groups:
    print(group.name)

# luozong = group.search('罗正顺').
# print(luozong)


#123456