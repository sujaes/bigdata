import os
import requests
import mylib3
import urlparse

keyPath=os.path.join(os.getcwd(),'key.properties')
key=mylib3.getKey(keyPath)
_key=str(key['gokr'])
TYPE='xml'
SERVICE='CardSubwayStatisticsService'
START_INDEX='1'
END_INDEX='10'
LINE_NUM='201306'
params=os.path.join(_key,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)
_url='http://openAPI.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)

params = url.replace("\\",'/')
print params
data=requests.get(params).text
print data