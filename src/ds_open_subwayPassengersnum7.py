# coding: utf-8
import os
import requests
import json
from pymongo import MongoClient
import mylib3

Client = MongoClient('localhost:27017')
_db=Client['ds_open_subwayPassengersDb'] #db created by mongo
_table=_db['db_open_subwayTable'] #collection
#db=Client.ds_rest_subwayPassengers

def saveJson(_fname,_data):
    import io
    with io.open(_fname, 'a', encoding='utf8') as json_file:
        _j=json.dumps(_data, json_file, ensure_ascii=False, encoding='utf8')
        json_file.write(_j+"\n")

def readJson(_fname):
    for line in open(_fname, 'r').readlines():
        _j=json.loads(line)
        #print _j['id'],_j['text']
        print _j['id']

def saveDB(_data):
    _table.insert_one(_data)

def readDB():
    for tweet in _table.find():
        print tweet['id'],tweet['text']

def saveFile(_fname,_data):
    fp=open(_fname,'a')
    fp.write(_data+"\n")

def doIt():
    keyPath=os.path.join(os.getcwd(),'key.properties')
    key=mylib3.getKey(keyPath)
    _url='http://openAPI.seoul.go.kr:8088'
    _key=str(key['gokr'])
    _type='json'
    _service='CardSubwayStatisticsService'
    _start_index=1
    _end_index=5
    _use_mon='201306'
    _maxIter=20
    _iter=0
    _jfname='src/ds_open_subwayPassengers.json'
    while _iter<_maxIter:
        _api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon)
        #print _api
        _api = _api.replace("\\",'/')
        r=requests.get(_api)
        _json=r.json()
        print _json
        saveJson(_jfname,_json)
        saveDB(_json)
        _start_index+=5
        _end_index+=5
        _iter+=1

if __name__ == "__main__":
    doIt()