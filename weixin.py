#!/usr/bin/python
# -*- coding: UTF-8 -*- 
# @Time = '2018/11/29'
# author = ‘wulu’


from wxpy import *

class weinxin:

    bot = None

    #微信登录
    def login(self):
        self.bot = Bot(console_qr=True, cache_path=True)
        self.bot.enable_puid('wxpy_puid.pkl')


