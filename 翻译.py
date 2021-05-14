import urllib.request
import json
import time
while True:
    content = input('输入你要翻译的内容 若输入q!退出程序:')
    if content == 'q!':
        break
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'

    data = {}
    data['i'] = content
    data['doctype'] = 'json'


    data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')

#print(html)

    target = json.loads(html)
    target = target['translateResult'][0][0]['tgt']
    print(target)

    time.sleep(5)





'''
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
data = {}
data['from'] = 'en'
data['to'] = 'zh'
data['query'] = 'love'
data['transtype'] = 'translang'
data['simple_means_flag'] = '3'

data['domain'] = 'common'

data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url,data)
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52")
'''
