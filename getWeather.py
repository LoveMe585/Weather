#!/usr/bin/python
# -*- coding: UTF-8 -*- 
# @Time = '2018/11/27'
# author = ‘wulu’


import requests
import json

# AppKey：25053729     AppSecret：47d17730cd8f7fa96677dd939266b597 复制
#
# AppCode：673a803d67954b5fb03c2aab72cdd707



#天气的工具类
class Weather:

    #加密code，用于签名验证
    appcode = '673a803d67954b5fb03c2aab72cdd707'

    #请求的头信息
    header = {"Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
          "Authorization":"APPCODE 673a803d67954b5fb03c2aab72cdd707"}

    #实例统一请求体
    request = requests.session()
    request.headers = header

    def getNowWeaher(self, cityid):

        if cityid is None:
            print('cityid is None')
            return {}

        #获取实况天气
        url_now = 'http://aliv18.data.moji.com/whapi/json/alicityweather/condition'

        bodys = {'cityId': cityid}
        #设置参数
        self.request.params = bodys

        #请求数据
        response = self.request.post(url_now)

        print(response.text)
        #判断是否请求成功
        if response == None or response.status_code != 200:
            #请求结果出错
            print('request is error')
            return {}

        #进行json转化
        result_json = json.loads(response.text)

        #获取城市信息
        city = result_json['data']['city']

        #获取实时天气信息
        now_weaher = result_json['data']['condition']

        #封装返回信息
        result = {}
        result['city'] = city['name']  #天气的城市
        result['condition'] = now_weaher['condition'] #当前天气状况
        result['humidity'] = now_weaher['humidity'] #当前湿度
        result['temp'] = now_weaher['temp'] #当前温度
        result['realFeel'] = now_weaher['realFeel'] #体感温度
        result['tips'] = now_weaher['tips'] #一句提醒

        #获取对应城市的生活指数
        live_life = self.getlife(cityid)

        #合并生活指数信息
        result.update(live_life)

        return result


    def getlife(self, cityid):

        #判断cityid
        if cityid is None:
            print('cityid is None')
            return {}

        #获取生活只是
        url_life = 'http://aliv18.data.moji.com/whapi/json/alicityweather/index'

        #封装请求参数
        bodys = {'cityId': cityid}
        self.request.params = bodys

        #请求获取生活指数
        response = self.request.post(url_life)

        print(response.text)
        #判断返回请求
        if response is None or response.status_code != 200:
            print('response is None')
            return {}

        #获取生活指数
        result_json = json.loads(response.text)
        live_index = result_json['data']['liveIndex']

        lives = list(live_index.values())[0]
        #获取生活指数建议
        live_life = {}
        for live in lives:
            code = live['code']
            # print(type(code))
            if code == 17:  #洗车指数
                live_life['17'] = live

            if code == 20: #穿衣指数
                live_life['20'] = live

            if code == 7:  #化妆指数
                live_life['7'] = live

        return live_life




# request = requests.session()
# request.headers = header
# request.params = bodys
# result = request.post(url)
# if result != None and result.status_code == 200:
#     tianqi = json.loads(result.text)
#     print(tianqi)
#     for hourly in tianqi['data']['hourly']:
#         print(hourly)hourly

result = Weather().getNowWeaher(547)
print(result)