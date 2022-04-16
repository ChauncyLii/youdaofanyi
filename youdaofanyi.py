import requests
import execjs

# 获取有道翻译里面的加密参数并且返回
def get_parameters(data,ua):
    with open('youdao.js','r',encoding='utf-8')as f:
        youdao_js = f.read()
    params = execjs.compile(youdao_js).call('getEncryptedParams',data,ua)
    parameters = {
        'i': data,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': params['salt'],
        'sign': params['sign'],
        'lts': params['lts'],
        'bv': params['bv'],
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    return parameters
'''
表单中的参数

salt: 16499896252204  // 加密参数
sign: 2969aadd9a77abcab6f2de1320311c5d // 加密参数
lts: 1649989625220 // 时间戳 13位数 
bv: c795a332c678d5063a1ee5eb15253848 // 加密参数
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME
'''

# 获取翻译之后的结果
def get_translation_result(parameters,ua,url):
    headers = {
        'User-Agent': ua,
        'Host': 'fanyi.youdao.com',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://fanyi.youdao.com',
        'Referer': 'https://fanyi.youdao.com/',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="21", " Not;A Brand";v="99"',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=1971701027@10.108.162.134; OUTFOX_SEARCH_USER_ID_NCOO=1022143169.8741976; JSESSIONID=aaa3Jp_7d-okr-lqPUWay; fanyi-ad-id=305572; fanyi-ad-closed=1; ___rl__test__cookies= {0}'.format(parameters['lts'])
    }
    response = requests.post(url=url, headers=headers, data=parameters)
    result = response.json()
    return result

def main():
    # 定义User-Agent参数
    # 定义翻译接口的url地址
    url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    ua = "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    data = "输入要翻译的词句"
    result = get_parameters(data,ua)
    translation_result = get_translation_result(result,ua,url)
    print(translation_result)

if __name__ == '__main__':
    main()