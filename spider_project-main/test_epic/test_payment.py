# _*_coding:utf-8 _*_
# @Time　　:2022/5/6   16:13
# @Author　 : Ben
# @ File　　  :test_payment.py
# @Software  :PyCharm
# @Description
import requests

cookies = {
    'EPIC_BEARER_TOKEN': 'c73820d6ebf04b3fadd42dcbd445d184',
}

headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
}

params = (
    ('locale', 'zh-CN'),
)

response = requests.get('https://www.epicgames.com/account/v2/payment/ajaxGetOrderHistory', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.epicgames.com/account/v2/payment/ajaxGetOrderHistory?locale=zh-CN', headers=headers, cookies=cookies)

print(response.text)
# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://www.epicgames.com/account/v2/payment/ajaxGetOrderHistory?locale=zh-CN', headers=headers)
