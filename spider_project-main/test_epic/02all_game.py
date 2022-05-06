# _*_coding:utf-8 _*_
# @Time　　:2022/5/5   14:30
# @Author　 : Ben
# @ File　　  :02all_game.py
# @Software  :PyCharm
# @Description Epic公开的游戏数据
import requests

game_base_url="https://store.epicgames.com/graphql"

"""
https://store.epicgames.com/graphql
payload
?operationName=searchStoreQuery&variables=
{"allowCountries":"CN"
,"category":"addons"
,"comingSoon":false
,"count":40
,"country":"CN"
,"keywords":""
,"locale":"zh-CN"
,"sortBy":"releaseDate"
,"sortDir":"DESC"
,"start":0
,"tag":""
,"withPrice":true
}&extensions={
"persistedQuery":{"version":1,"sha256Hash":"13a2b6787f1a20d05c75c54c78b1b8ac7c8bf4efc394edf7a5998fdf35d1adb0"}
}

"""
# 1.游戏
game_params={
    "operationName":"searchStoreQuery",
    "variables":"""{"allowCountries":"CN","category":"games/edition/base|software/edition/base|editors|bundles/games","comingSoon":false,"count":40,"country":"CN","keywords":"","locale":"zh-CN","sortBy":"releaseDate","sortDir":"DESC","start":40,"tag":"","withPrice":true}""",
    "extensions":"""{"persistedQuery":{"version":1,"sha256Hash":"13a2b6787f1a20d05c75c54c78b1b8ac7c8bf4efc394edf7a5998fdf35d1adb0"}}"""

}

# 2.游戏捆绑包
game_bundles_params={
    "operationName": "searchStoreQuery",
    "variables": """{"allowCountries":"CN","category":"bundles/games","comingSoon":false,"count":40,"country":"CN","keywords":"","locale":"zh-CN","sortBy":"releaseDate","sortDir":"DESC","start":0,"tag":"","withPrice":true}""",
    "extensions": """{"persistedQuery":{"version":1,"sha256Hash":"13a2b6787f1a20d05c75c54c78b1b8ac7c8bf4efc394edf7a5998fdf35d1adb0"}}"""
}

#3.游戏附加内容
game_addons_params={
    "operationName": "searchStoreQuery",
    "variables": """{"allowCountries":"CN","category":"addons","comingSoon":false,"count":40,"country":"CN","keywords":"","locale":"zh-CN","sortBy":"releaseDate","sortDir":"DESC","start":0,"tag":"","withPrice":true}""",
    "extensions": """{"persistedQuery":{"version":1,"sha256Hash":"13a2b6787f1a20d05c75c54c78b1b8ac7c8bf4efc394edf7a5998fdf35d1adb0"}}"""
}

#4.游戏演示版
game_addons_params={
    "operationName": "searchStoreQuery",
    "variables": """{"allowCountries":"CN","category":"games/edition/base|software/edition/base|editors|bundles/games","comingSoon":false,"count":40,"country":"CN","keywords":"","locale":"zh-CN","sortBy":"releaseDate","sortDir":"DESC","start":0,"tag":"","withPrice":true}""",
    "extensions": """{"persistedQuery":{"version":1,"sha256Hash":"13a2b6787f1a20d05c75c54c78b1b8ac7c8bf4efc394edf7a5998fdf35d1adb0"}}"""
}

# result=requests.get(url=game_base_url,params=game_params)
result=requests.get(url=game_base_url,params=game_bundles_params)
print(result.text)