import os
import mylib3
import requests
import urlparse

keyPath=os.path.join(os.getcwd(),'key.properties')
key=mylib3.getKey(keyPath)
KEY=str(key['gokr'])
TYPE='xml'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX=str(1)
END_INDEX=str(10)
LINE_NUM=str(2)
params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)
print params[31:]

_url='http://openAPI.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)
print url

data=requests.get(url).text
print data[:500]