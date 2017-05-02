import os
import requests
import mylib3
import urlparse
keyPath=os.path.join(os.getcwd(),'key.properties')
key=mylib3.getKey(keyPath)

_url='http://openAPI.seoul.go.kr:8088'
_key=str(key['gokr'])
_type='xml'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'
_maxIter=2
_iter=0
while _iter<_maxIter:
    _api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon)
    #print _api
    _api = _api.replace("\\",'/')
    response = requests.get(_api).text
    print response
    _start_index+=5
    _end_index+=5
    _iter+=1