import random

import requests

url = 'https://m.ctrip.com/restapi/soa2/21881/json/getHotelScript'


def callback():
    t = ""
    a = 'qwertyuiopasdfg$hjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for i in range(10):
        t += a[random.randint(0, len(a)-1)]
    return t

# cookies = {
#     'ibulanguage': 'CN',
#     'ibulocale': 'zh_cn',
#     'cookiePricesDisplayed': 'CNY',
#     'MKT_CKID': '1679751483493.gp2v1.cg0n',
#     'MKT_CKID_LMT': '1679751483493',
#     'GUID': '09031125117698908168',
#     '_RSG': 'Vzqd7Ac1QIC8WSjxaFsLX9',
#     '_RDG': '28abdab3b7735a257a0829384e2252062f',
#     '_RGUID': 'c49a0662-879f-4f5f-9855-d8f93bb5c808',
#     '_bfaStatusPVSend': '1',
#     'MKT_Pagesource': 'PC',
#     'login_uid': 'AFD72B50E208A2F338B67D03C65F9C15',
#     'login_type': '0',
#     'cticket': 'F9842C7D324CD4D08B1DED6A6E76B37D397B63FC2B132B818C7751785A3B1831',
#     'AHeadUserInfo': 'VipGrade=0&VipGradeName=%C6%D5%CD%A8%BB%E1%D4%B1&UserName=&NoReadMessageCount=0',
#     'DUID': 'u=AFD72B50E208A2F338B67D03C65F9C15&v=0',
#     'IsNonUser': 'F',
#     'UUID': '2CA37D2349B24EEAB48A2639C45082B3',
#     'librauuid': '',
#     'nfes_isSupportWebP': '1',
#     'manualclose': '1',
#     '_bfi': 'p1%3D102002%26p2%3D102002%26v1%3D25%26v2%3D24',
#     'Session': 'smartlinkcode=U130727&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=',
#     'Union': 'AllianceID=4902&SID=130727&OUID=&createtime=1679834661&Expires=1680439460983',
#     '_bfaStatus': 'send',
#     '_RF1': '223.104.63.30',
#     '_jzqco': '%7C%7C%7C%7C1679751576349%7C1.1812229885.1679751483498.1679834661331.1679834666139.1679834661331.1679834666139.0.0.0.24.24',
#     '__zpspc': '9.4.1679832330.1679834666.14%233%7Ccn.bing.com%7C%7C%7C%7C%23',
#     '_bfa': '1.1679751483396.4003l8.1.1679817353074.1679832322103.4.27.1',
#     '_bfs': '1.15',
#     '_ubtstatus': '%7B%22vid%22%3A%221679751483396.4003l8%22%2C%22sid%22%3A4%2C%22pvid%22%3A27%2C%22pid%22%3A102002%7D',
# }

headers = {
    'authority': 'm.ctrip.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; MKT_CKID=1679751483493.gp2v1.cg0n; MKT_CKID_LMT=1679751483493; GUID=09031125117698908168; _RSG=Vzqd7Ac1QIC8WSjxaFsLX9; _RDG=28abdab3b7735a257a0829384e2252062f; _RGUID=c49a0662-879f-4f5f-9855-d8f93bb5c808; _bfaStatusPVSend=1; MKT_Pagesource=PC; login_uid=AFD72B50E208A2F338B67D03C65F9C15; login_type=0; cticket=F9842C7D324CD4D08B1DED6A6E76B37D397B63FC2B132B818C7751785A3B1831; AHeadUserInfo=VipGrade=0&VipGradeName=%C6%D5%CD%A8%BB%E1%D4%B1&UserName=&NoReadMessageCount=0; DUID=u=AFD72B50E208A2F338B67D03C65F9C15&v=0; IsNonUser=F; UUID=2CA37D2349B24EEAB48A2639C45082B3; librauuid=; nfes_isSupportWebP=1; manualclose=1; _bfi=p1%3D102002%26p2%3D102002%26v1%3D25%26v2%3D24; Session=smartlinkcode=U130727&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4902&SID=130727&OUID=&createtime=1679834661&Expires=1680439460983; _bfaStatus=send; _RF1=223.104.63.30; _jzqco=%7C%7C%7C%7C1679751576349%7C1.1812229885.1679751483498.1679834661331.1679834666139.1679834661331.1679834666139.0.0.0.24.24; __zpspc=9.4.1679832330.1679834666.14%233%7Ccn.bing.com%7C%7C%7C%7C%23; _bfa=1.1679751483396.4003l8.1.1679817353074.1679832322103.4.27.1; _bfs=1.15; _ubtstatus=%7B%22vid%22%3A%221679751483396.4003l8%22%2C%22sid%22%3A4%2C%22pvid%22%3A27%2C%22pid%22%3A102002%7D',
    'origin': 'https://hotels.ctrip.com',
    'p': '84480519757',
    'pragma': 'no-cache',
    'referer': 'https://hotels.ctrip.com/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

json_data = {
    'callback': callback(),
    'a': 0,
    'b': '2023-03-28',
    'c': '2023-03-30',
    'd': 'zh-cn',
    'e': 2,
    'head': {
        'Locale': 'zh-CN',
        'Currency': 'CNY',
        'Device': 'PC',
        'UserIP': '2409:8955:3814:1ef4:b119:1b10:5688:f516',
        'Group': '',
        'ReferenceID': '',
        'UserRegion': 'CN',
        'AID': '4902',
        'SID': '130727',
        'Ticket': '',
        'UID': '',
        'IsQuickBooking': '',
        'ClientID': '09031125117698908168',
        'OUID': '',
        'TimeZone': '8',
        'P': '84480519757',
        'PageID': '102002',
        'Version': '',
        'HotelExtension': {
            'WebpSupport': True,
            'group': 'CTRIP',
            'Qid': '173101740895',
            'hasAidInUrl': False,
        },
        'Frontend': {
            'vid': '1679751483396.4003l8',
            'sessionID': 4,
            'pvid': 27,
        },
    },
    'ServerData': '',
}

response = requests.post(
    'https://m.ctrip.com/restapi/soa2/21881/json/getHotelScript',
    # cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"callback":"gmjRfdSIev","a":0,"b":"2023-03-28","c":"2023-03-30","d":"zh-cn","e":2,"head":{"Locale":"zh-CN","Currency":"CNY","Device":"PC","UserIP":"2409:8955:3814:1ef4:b119:1b10:5688:f516","Group":"","ReferenceID":"","UserRegion":"CN","AID":"4902","SID":"130727","Ticket":"","UID":"","IsQuickBooking":"","ClientID":"09031125117698908168","OUID":"","TimeZone":"8","P":"84480519757","PageID":"102002","Version":"","HotelExtension":{"WebpSupport":true,"group":"CTRIP","Qid":"173101740895","hasAidInUrl":false},"Frontend":{"vid":"1679751483396.4003l8","sessionID":4,"pvid":27}},"ServerData":""}'
#response = requests.post('https://m.ctrip.com/restapi/soa2/21881/json/getHotelScript', cookies=cookies, headers=headers, data=data)
print(response.text, file=open('function.json', 'w'))
print(response.text)

