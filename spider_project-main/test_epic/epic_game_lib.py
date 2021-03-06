# _*_coding:utf-8 _*_
# @Time　　:2022/5/5   14:28
# @Author　 : Ben
# @ File　　  :1.game_lib.py
# @Software  :PyCharm
# @Description Epic用户的数据
import requests
from fake_useragent import UserAgent


def get_epic_account_lib(cookie):
    """
    获取epic用户数据
    抓包页面：https://www.epicgames.com/site/zh-CN/home
    :param cookie:Epic用户cookie
    :return:
    """
    base_url = "https://graphql.epicgames.com/ue/graphql"
    header = {
        "User-Agent": UserAgent().random,
        "referer": "https://www.epicgames.com/"
    }
    data = {
        "query": "\n{\n    Account {\n        myAccount(mask: true) {\n            country\n            displayName\n            email\n            id\n            isLoggedIn\n            preferredLanguage\n        }\n    }\n}\n",
        "variables": {}}
    result = requests.post(url=base_url, cookies=cookie, headers=header, json=data)
    print(result.text)


def get_epic_wish_lib(cookie):
    """
    获取epic用户愿望清单的数据,可行
    :param cookie:Epic用户cookie
    :return:
    """
    base_url = "https://store.epicgames.com/graphql"
    wish_params = {
        "operationName": "getWishlist",
        "variables": """{"accountId":"7c5f6d0bc5414a2cb4d7e66ad022cd1c"}""",
        "extensions": """{"persistedQuery":{"version":1,"sha256Hash":"40e7770852757ee6aaa43b0f6fce65de984754e8d32572a1c978910cbf26f02e"}}"""
    }
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
        "referer": "https://store.epicgames.com/zh-CN/",
        # "authority": "store.epicgames.com"
    }

    result = requests.get(url=base_url, cookies=cookie, headers=header, params=wish_params)
    print(result.text)


def get_epic_payment_lib(cookie):
    """
    获取用户交易订单
    抓包接口：https://www.epicgames.com/account/transactions?lang=zh-CN&productName=epicgames
    :param cookie:
    :return:
    """
    # print(cookie)
    url = "https://www.epicgames.com/account/v2/payment/ajaxGetOrderHistory?locale=zh-CN"
    result = requests.get(url, cookies=cookie)
    print(result.text)


def get_epic_user_games_lib(cookie):
    """
    获取epic用户游戏库,从客户端获取
    :param cookie:Epic用户cookie，客户端获取复用 paymentcookie
    :return:
    """
    base_url = "https://store.epicgames.com/graphql"
    params = {
        "operationName": "getUserLibrary"
        ,
        "variables": '{"cursor":"","locale":"zh-CN","includeNs":[],"includeCategories":["games","software","engines","digitalextras","mods","addons"],"accountId":"7c5f6d0bc5414a2cb4d7e66ad022cd1c"}'
        ,
        "extensions": '{"persistedQuery":{"version":1,"sha256Hash":"c4ed3c80f30bf97ee884eadee81a512fea1ab2a19e1a17fdeb71e16ad7ff7fb9"}}'
    }
    header = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) EpicGamesLauncher/13.1.7-18788447+++Portal+Release-Live UnrealEngine/4.23.0-18788447+++Portal+Release-Live Chrome/84.0.4147.38 Safari/537.36",
        "Authorization": "Bearer eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJhcHAiOiJsYXVuY2hlciIsInN1YiI6IjdjNWY2ZDBiYzU0MTRhMmNiNGQ3ZTY2YWQwMjJjZDFjIiwiZHZpZCI6IjlhNmU1YzQ2NDI3NDhiNTI4ZGIxYzQ5NGZlYzJiYzE5IiwibXZlciI6ZmFsc2UsImNsaWQiOiIzNGEwMmNmOGY0NDE0ZTI5YjE1OTIxODc2ZGEzNmY5YSIsImRuIjoi6JCk54Gr55yg55ygIiwiYW0iOiJleGNoYW5nZV9jb2RlIiwicCI6ImVOcWxXRTF2SWprUVwvVCtJdzhDR1pHV0pReFJOZGcram1kV3dxejFHMVhaMVkrRzJlXC94Qnd2NzZyVExkMEFRSVRUZ040N2JMVmErcVhqM0g0MXJqcTJoU1liUVVIaHZubzRqZ0s0enp5Vmk2dWs1V1M0amEyU0MwamVndEdOb0hTZ1NNVWRzcXpLZnY5K0ZidXcra2RNbEd3ZGFtNDN4SldOS1o3cjdHTzVWa0ZIUVFLK2MzODhsa25BTDZienBFTVJJUGNsYmVxeStGbk4xTjdtQXFpenYxZ1BmM29MNU1wMUpONUljMmpaTmc5SFwvWnBmbGtOamFRckZ5aUY4cTlXdU1vQUtQWFNDWVVydEc0Qm4zajlScmtaaGZZNWZ2dngyaWpqZ1pyK3BkTWpVU05JVURGN2x3OFRENUpwOUNqd3JwaEw3c0lMcDBVZkl4aGQxNngxMDdTcGM2THNBUXlKdkxxWlNPTno2bW5MSU9QdWdTQ3JOQVdPQW16TVNZRDBZTmM5WUJWT2pRR05sQjV6UEhlbHA0eW1WSWJrNEY3R0ZNQmdISFZMb1N5Uk04Uk5yREpWdzFGcGlDVGRGbGJkMlNncThEV1FQZmZya0lmVTF3R3VwK3lINXlGN25zWWxMM1R0cWtvemtjZExEUmg2ZGd6NUtaQkx6RzNWZVhocWhLZ0dpYVhsN3A1V3FKY1wvZTFXYUhPXC9IdFJUaXlhdllEMmZYVldlWXNRaE9sK0JiWnRJZ0txMTNVRjQyY1hlMlV3U2h6a2U5Ykl6R0hZS0lJSWlRXC9tNFB5QXZvMWZJNExkUXQ2c0JyQ3JjR3lXNDFpRXdGMHpIQlhIREtuUE01VFRmbmV3Rmo2R2hxSENBZ1JQRTA3ckltSElZSVRvQ1JBZnAxdWczM1JYUk5Wb3licnZ6UmhlZStsUG9pSFg0c0xscU1nZE1wdVwvcW1ralJyVktUU1lcL1piMzliNTF2eUpneHA3RVNrYlZ4UzdEdFVLSmkxQjlaVUY4YlFVbWZTaWJwR0FjWncxSVE5V21xYmw4dCszcDNBS0tSaVh3azlGdXErY3c5UjFqNFZJSWZYUWI2YklrTWI1dlNRMnRmS2VUYmpJbnFIS2pSTjZBYmMrVHFCRUhqT2MwN0NjSktWTkRDNHVHNGFQNytTbHF1XC9rcGRMQ0l4MzZTR3B6a1pMKzNtTk8rZ3d0cTcrZzVPYVJFWkVxSU1nMlRHaTdpKzlScXNDWmRGYWxGczVNcUNjYnlDaWI0XC9cL2ZIXC82OCt2UGw4WGl4OHVQNStkY0F5YzVLTVwvc0F6YlpFZlNXVFphYXEyMXpQdEdnRk8wTitHSDNzd010TkFHQkFCNEN3RnZkTkxROTk4VVE1Y1d6SmlQY0lVMHJ0Vk83aVBmYXNMZEtQODhnUUNzWTRrNWE4QzRJUklFMDFxZ05RZGVpS1pWVzRvV3VPUTRjdlhlZVJrc1B1TzFSRjZtWEZ0dW93cjg2TGhkUTQ4SlIxZUd6ODRcL3R3UDU5VEwyOTFoSzFKUitJV25JN1hkRVFyK1FPSDJEa1I0ZTBFVGFCcXZVRGlTeEpTMGZzQURzdTl1SDBXQ1N6SXNhN1FqKzN4SEZGcE5GQllJVnpVK3VYbE9WZTU1UHNsb2lXVkFrZTZEK1JQeHhUMjJCRXlNOWpQaVZpekdHZnkwZlwvYWNOejdobzBzK0dHMkpHMFdWXC9VSmZab3lHdmlOcmtyRkphUVRPeHJob1BIenRhXC9Gdm05eU41dFB2NzA2UWRLWWtMTG1aN1wvTmk2U05rcmIwb244cXlaWldHTFl6cTJUXC9aS1wvOUlpall6YnkzaG16VzZYZlBjb2ZwajZHN3U0TGZBZjBUS0FTSVhCc2hWbHNQMldWTUx1dEViYTl6eSt3VDQrZkl4V2NnN3kyamw1Sld1VW4ranVOM2szYVwvZnpoRjhDV1d4a1Q1MXQ5djRXalwveG9lXC9rN29IZUs3RG9UQXhjUHRMWDk0cXJnOEZZXC9KSklBaHhiamVqcFV1d0JhWml1YkJpWmYwVU55eTZaXC81anliejZmODFDQVBUIiwiaWFpIjoiN2M1ZjZkMGJjNTQxNGEyY2I0ZDdlNjZhZDAyMmNkMWMiLCJzZWMiOjAsImNsc3ZjIjoibGF1bmNoZXIiLCJ0IjoicyIsImljIjp0cnVlLCJleHAiOjE2NTE4Mzc2NzAsImlhdCI6MTY1MTgwODg3MCwianRpIjoiNzQ4NGJkZjcxMTZhNGJkYmEwYjc0YzFjOTM3ZWIyZTQifQ.AZ0XKNoNfL0xcwb-ibQESDwjrL6ZrabDLQsYZz5zUOtSriLIUJE0K_P5I4TT1UvtsB5tUB9ipatV5cR1dprgJkFg"
    }

    result = requests.get(url=base_url, cookies=cookie, headers=header, params=params)
    print(result.text)


def get_epic_itemplaytime(cookie):
    """
    获取某个游戏的游玩时长，从客户端抓包获取，cookie也是从客户端获取
    :param cookie:
    :return:
    """
    base_url = "https://launcher.store.epicgames.com/graphql"
    params = {
        "operationName": "playtimeTracking",
        "variables": '{"accountId":"7c5f6d0bc5414a2cb4d7e66ad022cd1c","artifactId":"582c8940f499450d9033840efe5937a6"}',#artifactId==appName
        "extensions": '{"persistedQuery":{"version":1,"sha256Hash":"7d3296da9e0e1511711fb460bedbf8150e06da6abb64354ec39185c8e07de881"}}',
    }
    header = {
        "Accept": "application/json, text/plain, */*",
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
        ,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) EpicGamesLauncher/14.0.7-20032006+++Portal+Release-Live UnrealEngine/4.23.0-20032006+++Portal+Release-Live Chrome/90.0.4430.212 Safari/537.36'
        , 'X-Requested-With': 'XMLHttpRequest'
        , 'Host': 'launcher.store.epicgames.com'
        ,
        "Authorization": "Bearer eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJhcHAiOiJsYXVuY2hlciIsInN1YiI6IjdjNWY2ZDBiYzU0MTRhMmNiNGQ3ZTY2YWQwMjJjZDFjIiwiZHZpZCI6IjlhNmU1YzQ2NDI3NDhiNTI4ZGIxYzQ5NGZlYzJiYzE5IiwibXZlciI6ZmFsc2UsImNsaWQiOiIzNGEwMmNmOGY0NDE0ZTI5YjE1OTIxODc2ZGEzNmY5YSIsImRuIjoi6JCk54Gr55yg55ygIiwiYW0iOiJleGNoYW5nZV9jb2RlIiwicCI6ImVOcWxXRTF2SWprUVwvVCtJdzhDR1pHV0pReFJOZGcram1kV3dxejFHMVhaMVkrRzJlXC94Qnd2NzZyVExkMEFRSVRUZ040N2JMVmErcVhqM0g0MXJqcTJoU1liUVVIaHZubzRqZ0s0enp5Vmk2dWs1V1M0amEyU0MwamVndEdOb0hTZ1NNVWRzcXpLZnY5K0ZidXcra2RNbEd3ZGFtNDN4SldOS1o3cjdHTzVWa0ZIUVFLK2MzODhsa25BTDZienBFTVJJUGNsYmVxeStGbk4xTjdtQXFpenYxZ1BmM29MNU1wMUpONUljMmpaTmc5SFwvWnBmbGtOamFRckZ5aUY4cTlXdU1vQUtQWFNDWVVydEc0Qm4zajlScmtaaGZZNWZ2dngyaWpqZ1pyK3BkTWpVU05JVURGN2x3OFRENUpwOUNqd3JwaEw3c0lMcDBVZkl4aGQxNngxMDdTcGM2THNBUXlKdkxxWlNPTno2bW5MSU9QdWdTQ3JOQVdPQW16TVNZRDBZTmM5WUJWT2pRR05sQjV6UEhlbHA0eW1WSWJrNEY3R0ZNQmdISFZMb1N5Uk04Uk5yREpWdzFGcGlDVGRGbGJkMlNncThEV1FQZmZya0lmVTF3R3VwK3lINXlGN25zWWxMM1R0cWtvemtjZExEUmg2ZGd6NUtaQkx6RzNWZVhocWhLZ0dpYVhsN3A1V3FKY1wvZTFXYUhPXC9IdFJUaXlhdllEMmZYVldlWXNRaE9sK0JiWnRJZ0txMTNVRjQyY1hlMlV3U2h6a2U5Ykl6R0hZS0lJSWlRXC9tNFB5QXZvMWZJNExkUXQ2c0JyQ3JjR3lXNDFpRXdGMHpIQlhIREtuUE01VFRmbmV3Rmo2R2hxSENBZ1JQRTA3ckltSElZSVRvQ1JBZnAxdWczM1JYUk5Wb3licnZ6UmhlZStsUG9pSFg0c0xscU1nZE1wdVwvcW1ralJyVktUU1lcL1piMzliNTF2eUpneHA3RVNrYlZ4UzdEdFVLSmkxQjlaVUY4YlFVbWZTaWJwR0FjWncxSVE5V21xYmw4dCszcDNBS0tSaVh3azlGdXErY3c5UjFqNFZJSWZYUWI2YklrTWI1dlNRMnRmS2VUYmpJbnFIS2pSTjZBYmMrVHFCRUhqT2MwN0NjSktWTkRDNHVHNGFQNytTbHF1XC9rcGRMQ0l4MzZTR3B6a1pMKzNtTk8rZ3d0cTcrZzVPYVJFWkVxSU1nMlRHaTdpKzlScXNDWmRGYWxGczVNcUNjYnlDaWI0XC9cL2ZIXC82OCt2UGw4WGl4OHVQNStkY0F5YzVLTVwvc0F6YlpFZlNXVFphYXEyMXpQdEdnRk8wTitHSDNzd010TkFHQkFCNEN3RnZkTkxROTk4VVE1Y1d6SmlQY0lVMHJ0Vk83aVBmYXNMZEtQODhnUUNzWTRrNWE4QzRJUklFMDFxZ05RZGVpS1pWVzRvV3VPUTRjdlhlZVJrc1B1TzFSRjZtWEZ0dW93cjg2TGhkUTQ4SlIxZUd6ODRcL3R3UDU5VEwyOTFoSzFKUitJV25JN1hkRVFyK1FPSDJEa1I0ZTBFVGFCcXZVRGlTeEpTMGZzQURzdTl1SDBXQ1N6SXNhN1FqKzN4SEZGcE5GQllJVnpVK3VYbE9WZTU1UHNsb2lXVkFrZTZEK1JQeHhUMjJCRXlNOWpQaVZpekdHZnkwZlwvYWNOejdobzBzK0dHMkpHMFdWXC9VSmZab3lHdmlOcmtyRkphUVRPeHJob1BIenRhXC9Gdm05eU41dFB2NzA2UWRLWWtMTG1aN1wvTmk2U05rcmIwb244cXlaWldHTFl6cTJUXC9aS1wvOUlpall6YnkzaG16VzZYZlBjb2ZwajZHN3U0TGZBZjBUS0FTSVhCc2hWbHNQMldWTUx1dEViYTl6eSt3VDQrZkl4V2NnN3kyamw1Sld1VW4ranVOM2szYVwvZnpoRjhDV1d4a1Q1MXQ5djRXalwveG9lXC9rN29IZUs3RG9UQXhjUHRMWDk0cXJnOEZZXC9KSklBaHhiamVqcFV1d0JhWml1YkJpWmYwVU55eTZaXC81anliejZmODFDQVBUIiwiaWFpIjoiN2M1ZjZkMGJjNTQxNGEyY2I0ZDdlNjZhZDAyMmNkMWMiLCJzZWMiOjAsImNsc3ZjIjoibGF1bmNoZXIiLCJ0IjoicyIsImljIjp0cnVlLCJleHAiOjE2NTE4Mzc2NzAsImlhdCI6MTY1MTgwODg3MCwianRpIjoiNzQ4NGJkZjcxMTZhNGJkYmEwYjc0YzFjOTM3ZWIyZTQifQ.AZ0XKNoNfL0xcwb-ibQESDwjrL6ZrabDLQsYZz5zUOtSriLIUJE0K_P5I4TT1UvtsB5tUB9ipatV5cR1dprgJkFg"

    }
    # proxy={
    #     "http": None,
    #     "https": None
    # }
    result = requests.get(url=base_url, cookies=cookie, headers=header, params=params, proxies=None)
    # result=requests.get(url=base_url,cookies=None,headers=header,params=params,proxies=None)
    print(result.text)


def get_eipc_achievements(cookie):
    url = 'https://www.epicgames.com/store/zh-CN/my-achievements'
    headers={
        "User-Agent":UserAgent().random
    }
    result = requests.get(url=url, cookies=cookie,headers=headers)
    print(result.text)
    ...


def deal_cookie(cookie: str) -> dict:
    """
    处理cookie
    :param cookie:
    :return:
    """
    cookie_dict = {i.split("=")[0]: i.split("=")[-1] for i in cookie.split("; ")}
    # print(cookie_dict)
    return cookie_dict


if __name__ == '__main__':
    # cookie="""EPIC_DEVICE=c24c5e100d8043f4beb21d4d6e8088ad; _tald=01a88680-1e09-4fdf-8918-ca2c6e3e4770; EPIC_SSO=a13b792a51c6490aa887099aef1e3a4c; EPIC_BEARER_TOKEN=55f8e98674ba4b6997e19e6553754a9f; EPIC_SSO_RM=a13b792a51c6490aa887099aef1e3a4c; EPIC_EG1=eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJhcHAiOiJkaWVzZWx3ZWIiLCJzdWIiOiI3YzVmNmQwYmM1NDE0YTJjYjRkN2U2NmFkMDIyY2QxYyIsImR2aWQiOiJjMjRjNWUxMDBkODA0M2Y0YmViMjFkNGQ2ZTgwODhhZCIsIm12ZXIiOmZhbHNlLCJjbGlkIjoiODc1YTNiNTdkM2E2NDBhNmI3ZjliNGU4ODM0NjNhYjQiLCJkbiI6IuiQpOeBq-ecoOecoCIsImFtIjoidG9rZW5fdG9fdG9rZW4iLCJwIjoiZU5xbFZrRnU0ekFNXC9FK1JRNU5OVWtDQWY3Q0h4ZjZBbG1pSHFDd1psSlEyZmYxU2l1MjZUUU83M1ZOc2l5STVveGtxakdmQ0Y5V24ycEpXakwzbnFDSndpN0hhYnJUdnV1UklReVR2Z2lJWGtSMVlpUU9qQXNaSXJnM1Y3bk1jdmc1eG9MVlBMcXFjYmJjWjM0Wmk0K3VETEZrSzBcL2NuZldpTzVySFdoXC8xMkR6dGQ3ODBUSG85Z0huYzdiYlphYVdCcGJydEpBZmwzM3JpNGcxR2ppMzhzWEpCREtWY3o4R1dzU0JHN1wvTm5nR2EzdmtYdW1NK2pMQkhHeFFuWGNTQUdLRmp2NUxZd1laRFRZOVptUzlkQmtXKzZrWjIrU25pZ0o0RXp0WDhzU0pndVJRVDlMWXlxY1FLb0l2dEFMOFhnU05qeGZQa2NOV1F5RlhpaUFsckcwdVl4S2NFQUU2NmRDdm1tdURQWndLU21HMU9QcklrQkk4YVNoRjIxMTNrenczcFgwdFVhRTNsbTRQRXBrOEpxS3hDS2RLWTVuZVljZytZSWhUc2h2RDJnaTBraEVkZGg0YnNIUld4RzBBdE9SbVwvUzZpSEcrTjl4eStEQ0RPZnd1QzB4MUdNRklvckpkaEg4bWplUUVrOVA0WFFPOVVEamxEZFgyY05lNldqd2VjVHdhT1NcLytNQ2tzUGFPY3l0YzZGUWQxRklJa1wvRzVuMFVPSUphXC9BUTllU3d3XC9TVTJWQnN0Ylc2K2RWNXErMis4OStYMndqMnlSU2gzZU1OTnB0UmUyN1wvTTVIYVBFVFI0ZWNKMnpMVjlXbDNNV2F5Wk05ajJKdTdjXC80RGpMNm5uUVpkcENjUGdsM0l3dmp1T3NUNnhNSWpNblZVK2p0MG84SFdzcFVxVWFjVlwvM2ExSW1zSWRkNFZaNDY4VWtqeGl5aWJwalFtUlZXZU1pNlhSdWRZMzk2XC9BcXNcL1MrejNwcFwvNUw1SnRpRnI1ek0wTXl5Q21kMGo2MGZPYk5QMStyaXhUd0NMUWU2MzZcL0FibWhvcXQ5Q1ZxOFd6eVhlZjF4aUM1OVYwbGRSXC95MStIYXZjUDFXTHBOdz09IiwiaWFpIjoiN2M1ZjZkMGJjNTQxNGEyY2I0ZDdlNjZhZDAyMmNkMWMiLCJzZWMiOjAsImNsc3ZjIjoiZGllc2Vsd2ViIiwibHB2IjoxNjUxNzM1NDMyLCJ0IjoicyIsImljIjp0cnVlLCJleHAiOjE2NTE3NjQyMzEsImlhdCI6MTY1MTczNTQzNSwianRpIjoiMzJkNTA3YjQ2NmI1NDFlYjkzNDk0OTdmNDRhOTRmYzUifQ.Ajf0p4fpuyX8Y_4IXPDOlEG_V3MrWrkAN3NUD-tVyhTRzQWi5mmHOtJxTH-7DYPbJCbrm0wDhHDqWL99ShSihqRD; REFRESH_EPIC_EG1=eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJzdWIiOiI3YzVmNmQwYmM1NDE0YTJjYjRkN2U2NmFkMDIyY2QxYyIsImR2aWQiOiJjMjRjNWUxMDBkODA0M2Y0YmViMjFkNGQ2ZTgwODhhZCIsInQiOiJyIiwiY2xpZCI6Ijg3NWEzYjU3ZDNhNjQwYTZiN2Y5YjRlODgzNDYzYWI0IiwiZXhwIjoxNjUxODUwNjM1LCJhbSI6InRva2VuX3RvX3Rva2VuIiwianRpIjoiZmIyYzIzZWZjOTkzNGI0Yzk3NDRjOTk2YzYyYjE1N2MifQ.AU4Hku2xRmVb6kOK0KNV4jYctsv8b2BGO_meznPUlgruVDGNhLPKQFlx02PeHSUO19Has48Zygf9610PUTt0tY_W; refreshTokenExpires=2022-05-06T15:23:55.623Z; storeTokenExpires=2022-05-05T15:23:51.618Z; EPIC_LOCALE_COOKIE=zh-CN; EPIC_LOCALE=zh_CN; fptctx2=taBcrIH61PuCVH7eNCyH0LNKRXFdWqLJ6b8ywJyet7VH992QKkZo43FOwM7Y8rKB9SdBXOebxgFta8DqVKPPigmmedAKHD9eeto05rw9nverZ0k%2fsE2tIgK2Ys7Z%2fUJaiAxKALlQF481BnRVklNyRSyCMbinqPqTJ8Lag2AW31zURx9GI%2f0zlG7%2fRfd5Kzk2qe9DtFZkyqTY8JMJHOGK%2btsMEQKWM5J65w%2bEYrBKitr9CyAGjjDipPmd89JQPqH4FGugu1lnSz5%2bcHrfaDtJl5B4kX5nvEFeJN0eEI4CwjM%3d; MUID=21550c974b6f431bbf7ece7e56bc2dc1; EPIC_LOCALE_COOKIE=zh-Hans; _epicSID=870498b71c0a46d68e0cc525a8af7d2e"""
    cookie_wish = """EPIC_DEVICE=c24c5e100d8043f4beb21d4d6e8088ad; _tald=01a88680-1e09-4fdf-8918-ca2c6e3e4770; MUID=21550c974b6f431bbf7ece7e56bc2dc1; EPIC_SSO=7cd84af0bc7748a59b6c3e9518c0b45a; EPIC_BEARER_TOKEN=c73820d6ebf04b3fadd42dcbd445d184; EPIC_SSO_RM=7cd84af0bc7748a59b6c3e9518c0b45a; EPIC_EG1=eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJhcHAiOiJkaWVzZWx3ZWIiLCJzdWIiOiI3YzVmNmQwYmM1NDE0YTJjYjRkN2U2NmFkMDIyY2QxYyIsImR2aWQiOiJjMjRjNWUxMDBkODA0M2Y0YmViMjFkNGQ2ZTgwODhhZCIsIm12ZXIiOmZhbHNlLCJjbGlkIjoiODc1YTNiNTdkM2E2NDBhNmI3ZjliNGU4ODM0NjNhYjQiLCJkbiI6IuiQpOeBq-ecoOecoCIsImFtIjoidG9rZW5fdG9fdG9rZW4iLCJwIjoiZU5xbFZrRnU0ekFNXC9FK1JRNU5OVWtDQWY3Q0h4ZjZBbG1pSHFDd1psSlEyZmYxU2l1MjZUUU83M1ZOc2l5STVveGtxakdmQ0Y5V24ycEpXakwzbnFDSndpN0hhYnJUdnV1UklReVR2Z2lJWGtSMVlpUU9qQXNaSXJnM1Y3bk1jdmc1eG9MVlBMcXFjYmJjWjM0Wmk0K3VETEZrSzBcL2NuZldpTzVySFdoXC8xMkR6dGQ3ODBUSG85Z0huYzdiYlphYVdCcGJydEpBZmwzM3JpNGcxR2ppMzhzWEpCREtWY3o4R1dzU0JHN1wvTm5nR2EzdmtYdW1NK2pMQkhHeFFuWGNTQUdLRmp2NUxZd1laRFRZOVptUzlkQmtXKzZrWjIrU25pZ0o0RXp0WDhzU0pndVJRVDlMWXlxY1FLb0l2dEFMOFhnU05qeGZQa2NOV1F5RlhpaUFsckcwdVl4S2NFQUU2NmRDdm1tdURQWndLU21HMU9QcklrQkk4YVNoRjIxMTNrenczcFgwdFVhRTNsbTRQRXBrOEpxS3hDS2RLWTVuZVljZytZSWhUc2h2RDJnaTBraEVkZGg0YnNIUld4RzBBdE9SbVwvUzZpSEcrTjl4eStEQ0RPZnd1QzB4MUdNRklvckpkaEg4bWplUUVrOVA0WFFPOVVEamxEZFgyY05lNldqd2VjVHdhT1NcLytNQ2tzUGFPY3l0YzZGUWQxRklJa1wvRzVuMFVPSUphXC9BUTllU3d3XC9TVTJWQnN0Ylc2K2RWNXErMis4OStYMndqMnlSU2gzZU1OTnB0UmUyN1wvTTVIYVBFVFI0ZWNKMnpMVjlXbDNNV2F5Wk05ajJKdTdjXC80RGpMNm5uUVpkcENjUGdsM0l3dmp1T3NUNnhNSWpNblZVK2p0MG84SFdzcFVxVWFjVlwvM2ExSW1zSWRkNFZaNDY4VWtqeGl5aTdyMjEwenlSWjBIV01LRXpLOXp4a0tXOE5qckhcL2xRUkNxU3hcL1wvSHY3VHdZajZOSnRpRnI1Mk0xa3k0YW1sMHQ2NmZRYk5QMVJybHhWQUNMUWE2ODZ6d2NtaG9xdDlDVjI4YXp5ZGVoMXhpQzU5VjBsZFJcL3k3K0phdmNQZUc3d053PT0iLCJpYWkiOiI3YzVmNmQwYmM1NDE0YTJjYjRkN2U2NmFkMDIyY2QxYyIsInNlYyI6MCwiY2xzdmMiOiJkaWVzZWx3ZWIiLCJscHYiOjE2NTE4MDY5OTMsInQiOiJzIiwiaWMiOnRydWUsImV4cCI6MTY1MTgzNTc5MCwiaWF0IjoxNjUxODA2OTk0LCJqdGkiOiI4NjIwMTVlMWQ4NWE0MzkzYmNhNjU0NGQ3ZTJhY2E5ZiJ9.Ae8mfMQzCMQR20UZFSLHDaDWv2RILqZ9daGdN2FJR9KeP0yjM_9TuZ10VzyhWySLFNDHxZ1D2OopCAomE5Z5h4Wy; REFRESH_EPIC_EG1=eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJzdWIiOiI3YzVmNmQwYmM1NDE0YTJjYjRkN2U2NmFkMDIyY2QxYyIsImR2aWQiOiJjMjRjNWUxMDBkODA0M2Y0YmViMjFkNGQ2ZTgwODhhZCIsInQiOiJyIiwiY2xpZCI6Ijg3NWEzYjU3ZDNhNjQwYTZiN2Y5YjRlODgzNDYzYWI0IiwiZXhwIjoxNjUxOTIyMTk0LCJhbSI6InRva2VuX3RvX3Rva2VuIiwianRpIjoiMTI1ZTNkYmRlZmJiNDc1Y2E5ZGM0ZTIwYTJjMDQ3ZWEifQ.ASPkg_cxGR8CH3xT9G1mn2uxkp1Gq6lglM7IIunm__bNVwLSMKYVV9z4x6kvNIuFxwcgu961Uux1rYYtSrxcmdvq; refreshTokenExpires=2022-05-07T11%3A16%3A34.968Z; storeTokenExpires=2022-05-06T11%3A16%3A30.964Z; EPIC_LOCALE_COOKIE=zh-CN; _epicSID=5c7d0ab5b3114f0bbf211593df4f1118"""
    """
    此cookie可进行
    1. 用户信息获取
    2. 愿望清单获取
    3. 交易清单
    """

    cookie = """EPIC_SESSION_GRAPHQL=RxRMgsrWZXMwo9vB3O4-Vg.qgCjcWZbV0-jBdjC5XE3-EWhdu6NGQ1wBQduqeYG41cD5pnCTlY3P_vzui9O2O_JVJiJZkos7xwpDPDqAnuwK8kZl7gupa_87wPqHX32SOmg16b4mJnoHs_rcy2KDlF86oPHRAIxex3cwwQpBZjm9S8jRftrDjhhG1ZSeQVeM-fdDLKdWtMatz9r_oSMFF8OcbH_4Gkh-4mwDDNZM0WKLKlJTs_XIZL1lwj6cmqa36xquIjFRwIDqyGekZR4cEwq_AHkzEcxE4Izg2MRpLSqKwgyLIxe1pErL-LXlwgCJR8ViuocANrb11ZEgeOgwc8OSomBVfskThBl-_bil8O6531mQWnRhgD1kIvs8BY0quFnWexmX_NOkORB64kTu92kIMANveS13A7oPUr6haVmmQdycThtumguKeQtvL9qFsAxWM3RsKPHIq4I5StKAHgZSnUHAlQw09LL4RfuAOeTDmX6g-B5qwmiGdCqO1ntxSN4yKTI7qf8Fhp40v3sPV2VS8-iP61VPtDw4XtJblj7Qy6cqiA-Dj8YsAIaMeszwtOGVdfVQ0k2qboV0NdfiVlBJcpPd0KqvDCo23uxb9f-WQLcI02gd2zBEQtHy2fpCj2Rd-8xqQfKVuroSrHYrbQvx54RYnGsmwfFo9y86JQns4noYn8eaQ78j432UHoNisJOs4LeY0Srxd2SWWDjbt8MvQ6VOz16NhL9_w4yWwFapw.1651819441561.86400000.hApY-bCbyTgett7e3LJicpXkNP_dbr5tjl2DrYnwPGQ; EPIC_DEVICE=c24c5e100d8043f4beb21d4d6e8088ad; _tald=01a88680-1e09-4fdf-8918-ca2c6e3e4770; MUID=21550c974b6f431bbf7ece7e56bc2dc1; EPIC_SSO=7cd84af0bc7748a59b6c3e9518c0b45a; EPIC_BEARER_TOKEN=c73820d6ebf04b3fadd42dcbd445d184; EPIC_SSO_RM=7cd84af0bc7748a59b6c3e9518c0b45a; _epicSID=5c7d0ab5b3114f0bbf211593df4f1118; EPIC_EG1=eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJhcHAiOiJncmFwaHFsd2Vic2l0ZSIsInN1YiI6IjdjNWY2ZDBiYzU0MTRhMmNiNGQ3ZTY2YWQwMjJjZDFjIiwiZHZpZCI6ImMyNGM1ZTEwMGQ4MDQzZjRiZWIyMWQ0ZDZlODA4OGFkIiwibXZlciI6ZmFsc2UsImNsaWQiOiIzMTllMTUyN2QwYmU0NDU3YTEwNjc4MjlmYzBhZDg2ZSIsImRuIjoi6JCk54Gr55yg55ygIiwiYW0iOiJ0b2tlbl90b190b2tlbiIsInAiOiJlTnFkVmRGdTJ6QU1cL0o4Z0QwMldwSmdBXC84R0FEZHNYMEJMdEVKRWxRNVRTWmNQK2ZaUml1Mm5qSWU2ZUVsc2llYndqendIUGhDK3FUN1VsclFMMlBrUVZJYlFZcTgyYXZTYXdxZzArOWF3Y3F4TlE4Rnh0OW12UTJpY1h4OGp4Y1ZWdDE0a3hmQ0dPNmxudm00TjVxdlYrdDluQlZ0Yzc4NHlIQTVpbjdWYWJUYTZuMGNWdkZpNFlXQ0l0MVFIQ1pVeEtFYnY4V3U1UXROakpyenhwYnpDZ3dhNlA1TjE0OTJHdEhKYVQ5Y0dicENmZ0RNN1VcL21jNXdtUWhCdEFuY3EzaUkwZ1ZnY2k5ZDR4SGFjaUh5XC90YlF4WkQzRXNYMEFZc01CXC9Da1R3RHVUVXM3cUU2ekVMTW5NXC9MOFk4QWVZTWNKN0N2V0VCSE9sTWNCWkFESDFwdzlBc0sxV0E2Y3BQVUR4bVwvamMzME5qSmJUalJWSWtGREZwZG8xbldpVHhrNERSR3NuMjE2K09YSENUdU1ZQ1JSQ1g4M1NKUGdSbWlwUG8rYzlCRGlSWWlVb1Q2VFJuTENuTk5ZcHBYajR2RjdJVDdtZ056S25DYVRHdlhsTE1zZ2dLUkNlTE9kbGs0b1FPWUh1TWZRRVE5eGQzczdVcCtyZndoMjlNQ3hGSlhlMGJYa2NFVHNtd2FES2dkU3NyWmVueFp0ZmJYWnplN1F1R2tMRXF5ektBNER1WWh0dUE1bnlndTRaSVVzSktlUEFuMTBtOUZtcG9NK0JYMEVRVkphdkpvR01vcnFhdldZTWl1TWZYVldtTXFCY1BGcG92djZkSFZaXC9vQkh2QXI1MjBFblBJSEdQMlVwXC90Y0xVNlphTlRKejFhZDFuY2dhY28xWDVaK3NIRFZpRUdWSjdoQ3NKS0FKaE03OHdCaEZQMTVDK2pWaXdkVXlvRysrQWcrN3ljSkg2bENCdGRsbWtoVjNzY1dHaHhTWkpwbWFtK1wvSWNoZTdDZUk3UGtpTVNFeWxxMlZNRnZVMnMwY01Wb2JyUEh6Y0JwY2JnTGRaN1dMRG9yTXN2a1ptSHhZelUxSlwvTCtOV2JmOENuUjNBS0E9PSIsImlhaSI6IjdjNWY2ZDBiYzU0MTRhMmNiNGQ3ZTY2YWQwMjJjZDFjIiwic2VjIjowLCJjbHN2YyI6ImdyYXBocWx3ZWJzaXRlIiwibHB2IjoxNjUxODA2OTkzLCJ0IjoicyIsImljIjp0cnVlLCJleHAiOjE2NTE4NDgyNDEsImlhdCI6MTY1MTgxOTQ0MSwianRpIjoiMmEwZjQxYTViNTk0NDBjNzhmMWYwODA5YTNhZDdmYmIifQ.AQ8OyK7L8wENvGuVu2JxFuFf9r3ufW1N1eDOyItGib6yHm0XunLMKcdOGFhO6_Ddfr6HYHnDuGHvu-hXOINkTrpT"""
    """
     此cookie（用户信息接口）可进行
     1. 用户基本信息获取
     2. 用户交易订单
     """
    # print(cookie_dict)

    cookie_playtime = "EPIC_BEARER_TOKEN=eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJhcHAiOiJsYXVuY2hlciIsInN1YiI6IjdjNWY2ZDBiYzU0MTRhMmNiNGQ3ZTY2YWQwMjJjZDFjIiwiZHZpZCI6IjlhNmU1YzQ2NDI3NDhiNTI4ZGIxYzQ5NGZlYzJiYzE5IiwibXZlciI6ZmFsc2UsImNsaWQiOiIzNGEwMmNmOGY0NDE0ZTI5YjE1OTIxODc2ZGEzNmY5YSIsImRuIjoi6JCk54Gr55yg55ygIiwiYW0iOiJleGNoYW5nZV9jb2RlIiwicCI6ImVOcWxXRTF2SWprUVwvVCtJdzhDR1pHV0pReFJOZGcram1kV3dxejFHMVhaMVkrRzJlXC94Qnd2NzZyVExkMEFRSVRUZ040N2JMVmErcVhqM0g0MXJqcTJoU1liUVVIaHZubzRqZ0s0enp5Vmk2dWs1V1M0amEyU0MwamVndEdOb0hTZ1NNVWRzcXpLZnY5K0ZidXcra2RNbEd3ZGFtNDN4SldOS1o3cjdHTzVWa0ZIUVFLK2MzODhsa25BTDZienBFTVJJUGNsYmVxeStGbk4xTjdtQXFpenYxZ1BmM29MNU1wMUpONUljMmpaTmc5SFwvWnBmbGtOamFRckZ5aUY4cTlXdU1vQUtQWFNDWVVydEc0Qm4zajlScmtaaGZZNWZ2dngyaWpqZ1pyK3BkTWpVU05JVURGN2x3OFRENUpwOUNqd3JwaEw3c0lMcDBVZkl4aGQxNngxMDdTcGM2THNBUXlKdkxxWlNPTno2bW5MSU9QdWdTQ3JOQVdPQW16TVNZRDBZTmM5WUJWT2pRR05sQjV6UEhlbHA0eW1WSWJrNEY3R0ZNQmdISFZMb1N5Uk04Uk5yREpWdzFGcGlDVGRGbGJkMlNncThEV1FQZmZya0lmVTF3R3VwK3lINXlGN25zWWxMM1R0cWtvemtjZExEUmg2ZGd6NUtaQkx6RzNWZVhocWhLZ0dpYVhsN3A1V3FKY1wvZTFXYUhPXC9IdFJUaXlhdllEMmZYVldlWXNRaE9sK0JiWnRJZ0txMTNVRjQyY1hlMlV3U2h6a2U5Ykl6R0hZS0lJSWlRXC9tNFB5QXZvMWZJNExkUXQ2c0JyQ3JjR3lXNDFpRXdGMHpIQlhIREtuUE01VFRmbmV3Rmo2R2hxSENBZ1JQRTA3ckltSElZSVRvQ1JBZnAxdWczM1JYUk5Wb3licnZ6UmhlZStsUG9pSFg0c0xscU1nZE1wdVwvcW1ralJyVktUU1lcL1piMzliNTF2eUpneHA3RVNrYlZ4UzdEdFVLSmkxQjlaVUY4YlFVbWZTaWJwR0FjWncxSVE5V21xYmw4dCszcDNBS0tSaVh3azlGdXErY3c5UjFqNFZJSWZYUWI2YklrTWI1dlNRMnRmS2VUYmpJbnFIS2pSTjZBYmMrVHFCRUhqT2MwN0NjSktWTkRDNHVHNGFQNytTbHF1XC9rcGRMQ0l4MzZTR3B6a1pMKzNtTk8rZ3d0cTcrZzVPYVJFWkVxSU1nMlRHaTdpKzlScXNDWmRGYWxGczVNcUNjYnlDaWI0XC9cL2ZIXC82OCt2UGw4WGl4OHVQNStkY0F5YzVLTVwvc0F6YlpFZlNXVFphYXEyMXpQdEdnRk8wTitHSDNzd010TkFHQkFCNEN3RnZkTkxROTk4VVE1Y1d6SmlQY0lVMHJ0Vk83aVBmYXNMZEtQODhnUUNzWTRrNWE4QzRJUklFMDFxZ05RZGVpS1pWVzRvV3VPUTRjdlhlZVJrc1B1TzFSRjZtWEZ0dW93cjg2TGhkUTQ4SlIxZUd6ODRcL3R3UDU5VEwyOTFoSzFKUitJV25JN1hkRVFyK1FPSDJEa1I0ZTBFVGFCcXZVRGlTeEpTMGZzQURzdTl1SDBXQ1N6SXNhN1FqKzN4SEZGcE5GQllJVnpVK3VYbE9WZTU1UHNsb2lXVkFrZTZEK1JQeHhUMjJCRXlNOWpQaVZpekdHZnkwZlwvYWNOejdobzBzK0dHMkpHMFdWXC9VSmZab3lHdmlOcmtyRkphUVRPeHJob1BIenRhXC9Gdm05eU41dFB2NzA2UWRLWWtMTG1aN1wvTmk2U05rcmIwb244cXlaWldHTFl6cTJUXC9aS1wvOUlpall6YnkzaG16VzZYZlBjb2ZwajZHN3U0TGZBZjBUS0FTSVhCc2hWbHNQMldWTUx1dEViYTl6eSt3VDQrZkl4V2NnN3kyamw1Sld1VW4ranVOM2szYVwvZnpoRjhDV1d4a1Q1MXQ5djRXalwveG9lXC9rN29IZUs3RG9UQXhjUHRMWDk0cXJnOEZZXC9KSklBaHhiamVqcFV1d0JhWml1YkJpWmYwVU55eTZaXC81anliejZmODFDQVBUIiwiaWFpIjoiN2M1ZjZkMGJjNTQxNGEyY2I0ZDdlNjZhZDAyMmNkMWMiLCJzZWMiOjAsImNsc3ZjIjoibGF1bmNoZXIiLCJ0IjoicyIsImljIjp0cnVlLCJleHAiOjE2NTE4Mjk3NjksImlhdCI6MTY1MTgwMDk2OSwianRpIjoiOTMwZTE2ODhlYTFlNDljZDljMzE0NjRiZmEwNGI1YWYifQ.Ab5cF7KcGHzCtMMDu9kTPdgEFF1zWxWyX_FV9l6gWxeC5-uoXEsVIG3t4NOFz0SH0jwdX77l_dCp-a4CUJRgQwW1; EPIC_SSO=Marker; EPIC_LOCALE_COOKIE=zh-CN; _epicSID=8b9978fa277846899951822601b1dd4f; ecma=eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJhcHAiOiJsYXVuY2hlciIsInN1YiI6IjdjNWY2ZDBiYzU0MTRhMmNiNGQ3ZTY2YWQwMjJjZDFjIiwiZHZpZCI6IjlhNmU1YzQ2NDI3NDhiNTI4ZGIxYzQ5NGZlYzJiYzE5IiwibXZlciI6ZmFsc2UsImNsaWQiOiIzNGEwMmNmOGY0NDE0ZTI5YjE1OTIxODc2ZGEzNmY5YSIsImRuIjoi6JCk54Gr55yg55ygIiwiYW0iOiJleGNoYW5nZV9jb2RlIiwicCI6ImVOcWxXRTF2SWprUVwvVCtJdzhDR1pHV0pReFJOZGcram1kV3dxejFHMVhaMVkrRzJlXC94Qnd2NzZyVExkMEFRSVRUZ040N2JMVmErcVhqM0g0MXJqcTJoU1liUVVIaHZubzRqZ0s0enp5Vmk2dWs1V1M0amEyU0MwamVndEdOb0hTZ1NNVWRzcXpLZnY5K0ZidXcra2RNbEd3ZGFtNDN4SldOS1o3cjdHTzVWa0ZIUVFLK2MzODhsa25BTDZienBFTVJJUGNsYmVxeStGbk4xTjdtQXFpenYxZ1BmM29MNU1wMUpONUljMmpaTmc5SFwvWnBmbGtOamFRckZ5aUY4cTlXdU1vQUtQWFNDWVVydEc0Qm4zajlScmtaaGZZNWZ2dngyaWpqZ1pyK3BkTWpVU05JVURGN2x3OFRENUpwOUNqd3JwaEw3c0lMcDBVZkl4aGQxNngxMDdTcGM2THNBUXlKdkxxWlNPTno2bW5MSU9QdWdTQ3JOQVdPQW16TVNZRDBZTmM5WUJWT2pRR05sQjV6UEhlbHA0eW1WSWJrNEY3R0ZNQmdISFZMb1N5Uk04Uk5yREpWdzFGcGlDVGRGbGJkMlNncThEV1FQZmZya0lmVTF3R3VwK3lINXlGN25zWWxMM1R0cWtvemtjZExEUmg2ZGd6NUtaQkx6RzNWZVhocWhLZ0dpYVhsN3A1V3FKY1wvZTFXYUhPXC9IdFJUaXlhdllEMmZYVldlWXNRaE9sK0JiWnRJZ0txMTNVRjQyY1hlMlV3U2h6a2U5Ykl6R0hZS0lJSWlRXC9tNFB5QXZvMWZJNExkUXQ2c0JyQ3JjR3lXNDFpRXdGMHpIQlhIREtuUE01VFRmbmV3Rmo2R2hxSENBZ1JQRTA3ckltSElZSVRvQ1JBZnAxdWczM1JYUk5Wb3licnZ6UmhlZStsUG9pSFg0c0xscU1nZE1wdVwvcW1ralJyVktUU1lcL1piMzliNTF2eUpneHA3RVNrYlZ4UzdEdFVLSmkxQjlaVUY4YlFVbWZTaWJwR0FjWncxSVE5V21xYmw4dCszcDNBS0tSaVh3azlGdXErY3c5UjFqNFZJSWZYUWI2YklrTWI1dlNRMnRmS2VUYmpJbnFIS2pSTjZBYmMrVHFCRUhqT2MwN0NjSktWTkRDNHVHNGFQNytTbHF1XC9rcGRMQ0l4MzZTR3B6a1pMKzNtTk8rZ3d0cTcrZzVPYVJFWkVxSU1nMlRHaTdpKzlScXNDWmRGYWxGczVNcUNjYnlDaWI0XC9cL2ZIXC82OCt2UGw4WGl4OHVQNStkY0F5YzVLTVwvc0F6YlpFZlNXVFphYXEyMXpQdEdnRk8wTitHSDNzd010TkFHQkFCNEN3RnZkTkxROTk4VVE1Y1d6SmlQY0lVMHJ0Vk83aVBmYXNMZEtQODhnUUNzWTRrNWE4QzRJUklFMDFxZ05RZGVpS1pWVzRvV3VPUTRjdlhlZVJrc1B1TzFSRjZtWEZ0dW93cjg2TGhkUTQ4SlIxZUd6ODRcL3R3UDU5VEwyOTFoSzFKUitJV25JN1hkRVFyK1FPSDJEa1I0ZTBFVGFCcXZVRGlTeEpTMGZzQURzdTl1SDBXQ1N6SXNhN1FqKzN4SEZGcE5GQllJVnpVK3VYbE9WZTU1UHNsb2lXVkFrZTZEK1JQeHhUMjJCRXlNOWpQaVZpekdHZnkwZlwvYWNOejdobzBzK0dHMkpHMFdWXC9VSmZab3lHdmlOcmtyRkphUVRPeHJob1BIenRhXC9Gdm05eU41dFB2NzA2UWRLWWtMTG1aN1wvTmk2U05rcmIwb244cXlaWldHTFl6cTJUXC9aS1wvOUlpall6YnkzaG16VzZYZlBjb2ZwajZHN3U0TGZBZjBUS0FTSVhCc2hWbHNQMldWTUx1dEViYTl6eSt3VDQrZkl4V2NnN3kyamw1Sld1VW4ranVOM2szYVwvZnpoRjhDV1d4a1Q1MXQ5djRXalwveG9lXC9rN29IZUs3RG9UQXhjUHRMWDk0cXJnOEZZXC9KSklBaHhiamVqcFV1d0JhWml1YkJpWmYwVU55eTZaXC81anliejZmODFDQVBUIiwiaWFpIjoiN2M1ZjZkMGJjNTQxNGEyY2I0ZDdlNjZhZDAyMmNkMWMiLCJzZWMiOjAsImNsc3ZjIjoibGF1bmNoZXIiLCJ0IjoicyIsImljIjp0cnVlLCJleHAiOjE2NTE4Mjk3NjksImlhdCI6MTY1MTgwMDk2OSwianRpIjoiOTMwZTE2ODhlYTFlNDljZDljMzE0NjRiZmEwNGI1YWYifQ.Ab5cF7KcGHzCtMMDu9kTPdgEFF1zWxWyX_FV9l6gWxeC5-uoXEsVIG3t4NOFz0SH0jwdX77l_dCp-a4CUJRgQwW1"

    cookie_dict = deal_cookie(cookie)
    cookie_wish_dict = deal_cookie(cookie_wish)
    cookie_playtime_dict = deal_cookie(cookie_playtime)

    # 1. 使用 用户cookie 获取用户信息
    # get_epic_account_lib(cookie=cookie_dict)
    # 2. 使用 wish cookie 获取用户信息
    # get_epic_account_lib(cookie=cookie_wish_dict)

    # 3. 使用 用户cookie 获取用户 wish list
    # get_epic_wish_lib(cookie=cookie_dict)
    # 4. 使用 wish cookie 获取用户 wish list
    # get_epic_wish_lib(cookie=cookie_wish_dict)

    # 5. 使用 用户cookie 获取用户 交易信息
    # get_epic_payment_lib(cookie=cookie_dict)
    # 6. 使用 wish cookie 获取用户 交易信息
    # get_epic_payment_lib(cookie=cookie_wish_dict)

    """
    获取
    """

    cookie_playtime_dict = {
        "EPIC_BEARER_TOKEN": "eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJhcHAiOiJsYXVuY2hlciIsInN1YiI6IjdjNWY2ZDBiYzU0MTRhMmNiNGQ3ZTY2YWQwMjJjZDFjIiwiZHZpZCI6IjlhNmU1YzQ2NDI3NDhiNTI4ZGIxYzQ5NGZlYzJiYzE5IiwibXZlciI6ZmFsc2UsImNsaWQiOiIzNGEwMmNmOGY0NDE0ZTI5YjE1OTIxODc2ZGEzNmY5YSIsImRuIjoi6JCk54Gr55yg55ygIiwiYW0iOiJleGNoYW5nZV9jb2RlIiwicCI6ImVOcWxXRTF2SWprUVwvVCtJdzhDR1pHV0pReFJOZGcram1kV3dxejFHMVhaMVkrRzJlXC94Qnd2NzZyVExkMEFRSVRUZ040N2JMVmErcVhqM0g0MXJqcTJoU1liUVVIaHZubzRqZ0s0enp5Vmk2dWs1V1M0amEyU0MwamVndEdOb0hTZ1NNVWRzcXpLZnY5K0ZidXcra2RNbEd3ZGFtNDN4SldOS1o3cjdHTzVWa0ZIUVFLK2MzODhsa25BTDZienBFTVJJUGNsYmVxeStGbk4xTjdtQXFpenYxZ1BmM29MNU1wMUpONUljMmpaTmc5SFwvWnBmbGtOamFRckZ5aUY4cTlXdU1vQUtQWFNDWVVydEc0Qm4zajlScmtaaGZZNWZ2dngyaWpqZ1pyK3BkTWpVU05JVURGN2x3OFRENUpwOUNqd3JwaEw3c0lMcDBVZkl4aGQxNngxMDdTcGM2THNBUXlKdkxxWlNPTno2bW5MSU9QdWdTQ3JOQVdPQW16TVNZRDBZTmM5WUJWT2pRR05sQjV6UEhlbHA0eW1WSWJrNEY3R0ZNQmdISFZMb1N5Uk04Uk5yREpWdzFGcGlDVGRGbGJkMlNncThEV1FQZmZya0lmVTF3R3VwK3lINXlGN25zWWxMM1R0cWtvemtjZExEUmg2ZGd6NUtaQkx6RzNWZVhocWhLZ0dpYVhsN3A1V3FKY1wvZTFXYUhPXC9IdFJUaXlhdllEMmZYVldlWXNRaE9sK0JiWnRJZ0txMTNVRjQyY1hlMlV3U2h6a2U5Ykl6R0hZS0lJSWlRXC9tNFB5QXZvMWZJNExkUXQ2c0JyQ3JjR3lXNDFpRXdGMHpIQlhIREtuUE01VFRmbmV3Rmo2R2hxSENBZ1JQRTA3ckltSElZSVRvQ1JBZnAxdWczM1JYUk5Wb3licnZ6UmhlZStsUG9pSFg0c0xscU1nZE1wdVwvcW1ralJyVktUU1lcL1piMzliNTF2eUpneHA3RVNrYlZ4UzdEdFVLSmkxQjlaVUY4YlFVbWZTaWJwR0FjWncxSVE5V21xYmw4dCszcDNBS0tSaVh3azlGdXErY3c5UjFqNFZJSWZYUWI2YklrTWI1dlNRMnRmS2VUYmpJbnFIS2pSTjZBYmMrVHFCRUhqT2MwN0NjSktWTkRDNHVHNGFQNytTbHF1XC9rcGRMQ0l4MzZTR3B6a1pMKzNtTk8rZ3d0cTcrZzVPYVJFWkVxSU1nMlRHaTdpKzlScXNDWmRGYWxGczVNcUNjYnlDaWI0XC9cL2ZIXC82OCt2UGw4WGl4OHVQNStkY0F5YzVLTVwvc0F6YlpFZlNXVFphYXEyMXpQdEdnRk8wTitHSDNzd010TkFHQkFCNEN3RnZkTkxROTk4VVE1Y1d6SmlQY0lVMHJ0Vk83aVBmYXNMZEtQODhnUUNzWTRrNWE4QzRJUklFMDFxZ05RZGVpS1pWVzRvV3VPUTRjdlhlZVJrc1B1TzFSRjZtWEZ0dW93cjg2TGhkUTQ4SlIxZUd6ODRcL3R3UDU5VEwyOTFoSzFKUitJV25JN1hkRVFyK1FPSDJEa1I0ZTBFVGFCcXZVRGlTeEpTMGZzQURzdTl1SDBXQ1N6SXNhN1FqKzN4SEZGcE5GQllJVnpVK3VYbE9WZTU1UHNsb2lXVkFrZTZEK1JQeHhUMjJCRXlNOWpQaVZpekdHZnkwZlwvYWNOejdobzBzK0dHMkpHMFdWXC9VSmZab3lHdmlOcmtyRkphUVRPeHJob1BIenRhXC9Gdm05eU41dFB2NzA2UWRLWWtMTG1aN1wvTmk2U05rcmIwb244cXlaWldHTFl6cTJUXC9aS1wvOUlpall6YnkzaG16VzZYZlBjb2ZwajZHN3U0TGZBZjBUS0FTSVhCc2hWbHNQMldWTUx1dEViYTl6eSt3VDQrZkl4V2NnN3kyamw1Sld1VW4ranVOM2szYVwvZnpoRjhDV1d4a1Q1MXQ5djRXalwveG9lXC9rN29IZUs3RG9UQXhjUHRMWDk0cXJnOEZZXC9KSklBaHhiamVqcFV1d0JhWml1YkJpWmYwVU55eTZaXC81anliejZmODFDQVBUIiwiaWFpIjoiN2M1ZjZkMGJjNTQxNGEyY2I0ZDdlNjZhZDAyMmNkMWMiLCJzZWMiOjAsImNsc3ZjIjoibGF1bmNoZXIiLCJ0IjoicyIsImljIjp0cnVlLCJleHAiOjE2NTE4MzY2MjksImlhdCI6MTY1MTgwNzgyOSwianRpIjoiZjlhZTBjZmU3NzdhNDIzNTkwZjgxMTY5ZWFjZGNjMWMifQ.AGRf7nRuuhhRPU-a966hyEveyr5I8r0i3f5S7sLy6n3U18G-h-tfmBkMk99SlYXhWzmt6ZEPB465j_DFZp5paSdy"
        , "EPIC_SSO": "Marker"
        , "EPIC_LOCALE_COOKIE": "zh-CN"
        , "_epicSID": "744c92035dea4b9b86d437c7ef2d6354"
        ,
        "ecma": "eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJhcHAiOiJsYXVuY2hlciIsInN1YiI6IjdjNWY2ZDBiYzU0MTRhMmNiNGQ3ZTY2YWQwMjJjZDFjIiwiZHZpZCI6IjlhNmU1YzQ2NDI3NDhiNTI4ZGIxYzQ5NGZlYzJiYzE5IiwibXZlciI6ZmFsc2UsImNsaWQiOiIzNGEwMmNmOGY0NDE0ZTI5YjE1OTIxODc2ZGEzNmY5YSIsImRuIjoi6JCk54Gr55yg55ygIiwiYW0iOiJleGNoYW5nZV9jb2RlIiwicCI6ImVOcWxXRTF2SWprUVwvVCtJdzhDR1pHV0pReFJOZGcram1kV3dxejFHMVhaMVkrRzJlXC94Qnd2NzZyVExkMEFRSVRUZ040N2JMVmErcVhqM0g0MXJqcTJoU1liUVVIaHZubzRqZ0s0enp5Vmk2dWs1V1M0amEyU0MwamVndEdOb0hTZ1NNVWRzcXpLZnY5K0ZidXcra2RNbEd3ZGFtNDN4SldOS1o3cjdHTzVWa0ZIUVFLK2MzODhsa25BTDZienBFTVJJUGNsYmVxeStGbk4xTjdtQXFpenYxZ1BmM29MNU1wMUpONUljMmpaTmc5SFwvWnBmbGtOamFRckZ5aUY4cTlXdU1vQUtQWFNDWVVydEc0Qm4zajlScmtaaGZZNWZ2dngyaWpqZ1pyK3BkTWpVU05JVURGN2x3OFRENUpwOUNqd3JwaEw3c0lMcDBVZkl4aGQxNngxMDdTcGM2THNBUXlKdkxxWlNPTno2bW5MSU9QdWdTQ3JOQVdPQW16TVNZRDBZTmM5WUJWT2pRR05sQjV6UEhlbHA0eW1WSWJrNEY3R0ZNQmdISFZMb1N5Uk04Uk5yREpWdzFGcGlDVGRGbGJkMlNncThEV1FQZmZya0lmVTF3R3VwK3lINXlGN25zWWxMM1R0cWtvemtjZExEUmg2ZGd6NUtaQkx6RzNWZVhocWhLZ0dpYVhsN3A1V3FKY1wvZTFXYUhPXC9IdFJUaXlhdllEMmZYVldlWXNRaE9sK0JiWnRJZ0txMTNVRjQyY1hlMlV3U2h6a2U5Ykl6R0hZS0lJSWlRXC9tNFB5QXZvMWZJNExkUXQ2c0JyQ3JjR3lXNDFpRXdGMHpIQlhIREtuUE01VFRmbmV3Rmo2R2hxSENBZ1JQRTA3ckltSElZSVRvQ1JBZnAxdWczM1JYUk5Wb3licnZ6UmhlZStsUG9pSFg0c0xscU1nZE1wdVwvcW1ralJyVktUU1lcL1piMzliNTF2eUpneHA3RVNrYlZ4UzdEdFVLSmkxQjlaVUY4YlFVbWZTaWJwR0FjWncxSVE5V21xYmw4dCszcDNBS0tSaVh3azlGdXErY3c5UjFqNFZJSWZYUWI2YklrTWI1dlNRMnRmS2VUYmpJbnFIS2pSTjZBYmMrVHFCRUhqT2MwN0NjSktWTkRDNHVHNGFQNytTbHF1XC9rcGRMQ0l4MzZTR3B6a1pMKzNtTk8rZ3d0cTcrZzVPYVJFWkVxSU1nMlRHaTdpKzlScXNDWmRGYWxGczVNcUNjYnlDaWI0XC9cL2ZIXC82OCt2UGw4WGl4OHVQNStkY0F5YzVLTVwvc0F6YlpFZlNXVFphYXEyMXpQdEdnRk8wTitHSDNzd010TkFHQkFCNEN3RnZkTkxROTk4VVE1Y1d6SmlQY0lVMHJ0Vk83aVBmYXNMZEtQODhnUUNzWTRrNWE4QzRJUklFMDFxZ05RZGVpS1pWVzRvV3VPUTRjdlhlZVJrc1B1TzFSRjZtWEZ0dW93cjg2TGhkUTQ4SlIxZUd6ODRcL3R3UDU5VEwyOTFoSzFKUitJV25JN1hkRVFyK1FPSDJEa1I0ZTBFVGFCcXZVRGlTeEpTMGZzQURzdTl1SDBXQ1N6SXNhN1FqKzN4SEZGcE5GQllJVnpVK3VYbE9WZTU1UHNsb2lXVkFrZTZEK1JQeHhUMjJCRXlNOWpQaVZpekdHZnkwZlwvYWNOejdobzBzK0dHMkpHMFdWXC9VSmZab3lHdmlOcmtyRkphUVRPeHJob1BIenRhXC9Gdm05eU41dFB2NzA2UWRLWWtMTG1aN1wvTmk2U05rcmIwb244cXlaWldHTFl6cTJUXC9aS1wvOUlpall6YnkzaG16VzZYZlBjb2ZwajZHN3U0TGZBZjBUS0FTSVhCc2hWbHNQMldWTUx1dEViYTl6eSt3VDQrZkl4V2NnN3kyamw1Sld1VW4ranVOM2szYVwvZnpoRjhDV1d4a1Q1MXQ5djRXalwveG9lXC9rN29IZUs3RG9UQXhjUHRMWDk0cXJnOEZZXC9KSklBaHhiamVqcFV1d0JhWml1YkJpWmYwVU55eTZaXC81anliejZmODFDQVBUIiwiaWFpIjoiN2M1ZjZkMGJjNTQxNGEyY2I0ZDdlNjZhZDAyMmNkMWMiLCJzZWMiOjAsImNsc3ZjIjoibGF1bmNoZXIiLCJ0IjoicyIsImljIjp0cnVlLCJleHAiOjE2NTE4MzY2MjksImlhdCI6MTY1MTgwNzgyOSwianRpIjoiZjlhZTBjZmU3NzdhNDIzNTkwZjgxMTY5ZWFjZGNjMWMifQ.AGRf7nRuuhhRPU-a966hyEveyr5I8r0i3f5S7sLy6n3U18G-h-tfmBkMk99SlYXhWzmt6ZEPB465j_DFZp5paSdy"
    }

    # get_epic_itemplaytime(cookie=cookie_playtime_dict)
    # get_epic_user_games_lib(cookie=cookie_wish_dict)
    # get_epic_user_games_lib(cookie=cookie_playtime_dict)
    get_eipc_achievements(cookie_dict)
