import requests
import json
url='https://v1.hitokoto.cn?c=f&c=d&c=j'
res=requests.get(url).json()
msg=res['hitokoto']+'\n'+'from:'+res['from'] #这里我们只取内容和来源
print(msg)





token = '' #在pushplus网站中可以找到
title= '一言' #改成你要的标题内容
content =msg #改成你要的正文内容
url1='http://www.pushplus.plus/send?token={}&title=XXX&content=XXX&template=html&topic={}' #topic 群组号
data = {
    "token":token,
    "title":title,
    "content":content
}
body=json.dumps(data).encode(encoding='utf-8')
headers = {'Content-Type':'application/json'}
requests.post(url1,data=body,headers=headers)
