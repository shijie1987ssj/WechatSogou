import wechatsogou

# 可配置参数

# 直连
ws_api = wechatsogou.WechatSogouAPI()

#ws_api.get_gzh_info('楼市参考')

info = ws_api.search_article('楼市参考')

#print(info)
