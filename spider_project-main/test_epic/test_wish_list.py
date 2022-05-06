# _*_coding:utf-8 _*_
# @Time　　:2022/5/6   16:11
# @Author　 : Ben
# @ File　　  :test_wish_lis.py
# @Software  :PyCharm
# @Description
import requests

cookies = {
    'EPIC_EG1': 'eg1~eyJraWQiOiJ0RkMyVUloRnBUTV9FYTNxY09kX01xUVQxY0JCbTlrRkxTRGZlSmhzUkc4IiwiYWxnIjoiUFMyNTYifQ.eyJhcHAiOiJncmFwaHFsd2Vic2l0ZSIsInN1YiI6IjdjNWY2ZDBiYzU0MTRhMmNiNGQ3ZTY2YWQwMjJjZDFjIiwiZHZpZCI6ImMyNGM1ZTEwMGQ4MDQzZjRiZWIyMWQ0ZDZlODA4OGFkIiwibXZlciI6ZmFsc2UsImNsaWQiOiIzMTllMTUyN2QwYmU0NDU3YTEwNjc4MjlmYzBhZDg2ZSIsImRuIjoi6JCk54Gr55yg55ygIiwiYW0iOiJ0b2tlbl90b190b2tlbiIsInAiOiJlTnFkVmRGdTJ6QU1cL0o4Z0QwMldwSmdBXC84R0FEZHNYMEJMdEVKRWxRNVRTWmNQK2ZaUml1Mm5qSWU2ZUVsc2llYndqendIUGhDK3FUN1VsclFMMlBrUVZJYlFZcTgyYXZTYXdxZzArOWF3Y3F4TlE4Rnh0OW12UTJpY1h4OGp4Y1ZWdDE0a3hmQ0dPNmxudm00TjVxdlYrdDluQlZ0Yzc4NHlIQTVpbjdWYWJUYTZuMGNWdkZpNFlXQ0l0MVFIQ1pVeEtFYnY4V3U1UXROakpyenhwYnpDZ3dhNlA1TjE0OTJHdEhKYVQ5Y0dicENmZ0RNN1VcL21jNXdtUWhCdEFuY3EzaUkwZ1ZnY2k5ZDR4SGFjaUh5XC90YlF4WkQzRXNYMEFZc01CXC9Da1R3RHVUVXM3cUU2ekVMTW5NXC9MOFk4QWVZTWNKN0N2V0VCSE9sTWNCWkFESDFwdzlBc0sxV0E2Y3BQVUR4bVwvamMzME5qSmJUalJWSWtGREZwZG8xbldpVHhrNERSR3NuMjE2K09YSENUdU1ZQ1JSQ1g4M1NKUGdSbWlwUG8rYzlCRGlSWWlVb1Q2VFJuTENuTk5ZcHBYajR2RjdJVDdtZ056S25DYVRHdlhsTE1zZ2dLUkNlTE9kbGs0b1FPWUh1TWZRRVE5eGQzczdVcCtyZndoMjlNQ3hGSlhlMGJYa2NFVHNtd2FES2dkU3NyWmVueFp0ZmJYWnplN1F1R2tMRXF5ektBNER1WWh0dUE1bnlndTRaSVVzSktlUEFuMTBtOUZtcG9NK0JYMEVRVkphdkpvR01vcnFhdldZTWl1TWZYVldtTXFCY1BGcG92djZkSFZaXC9vQkh2QXI1MjBFblBJSEdQMlVwXC90Y0xVNlphTlRKejFhZDFuY2dhY28xWDVaK3NIRFZpRUdWSjdoQ3NKS0FKaE03OHdCaEZQMTVDK2pWaXdkVXlvRysrQWcrN3ljSkg2bENCdGRsbWtoVjNzY1dHaHhTWkpwbWFtK1wvSWNoZTdDZUk3UGtpTVNFeWxxMlZNRnZVMnMwY01Wb2JyUEh6Y0JwY2JnTGRaN1dMRG9yTXN2a1ptSHhZelUxSlwvTCtOV2JmOENuUjNBS0E9PSIsImlhaSI6IjdjNWY2ZDBiYzU0MTRhMmNiNGQ3ZTY2YWQwMjJjZDFjIiwic2VjIjowLCJjbHN2YyI6ImdyYXBocWx3ZWJzaXRlIiwibHB2IjoxNjUxODA2OTkzLCJ0IjoicyIsImljIjp0cnVlLCJleHAiOjE2NTE4NDgyNDEsImlhdCI6MTY1MTgxOTQ0MSwianRpIjoiMmEwZjQxYTViNTk0NDBjNzhmMWYwODA5YTNhZDdmYmIifQ.AQ8OyK7L8wENvGuVu2JxFuFf9r3ufW1N1eDOyItGib6yHm0XunLMKcdOGFhO6_Ddfr6HYHnDuGHvu-hXOINkTrpT',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'referer': 'https://store.epicgames.com/zh-CN/',
}

params = (
    ('operationName', 'getWishlist'),
    ('variables', '{"accountId":"7c5f6d0bc5414a2cb4d7e66ad022cd1c"}'),
    ('extensions', '{"persistedQuery":{"version":1,"sha256Hash":"40e7770852757ee6aaa43b0f6fce65de984754e8d32572a1c978910cbf26f02e"}}'),
)

response = requests.get('https://store.epicgames.com/graphql', headers=headers, params=params, cookies=cookies)
print(response.text)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://store.epicgames.com/graphql?operationName=getWishlist&variables={"accountId":"7c5f6d0bc5414a2cb4d7e66ad022cd1c"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"40e7770852757ee6aaa43b0f6fce65de984754e8d32572a1c978910cbf26f02e"}}', headers=headers, cookies=cookies)
