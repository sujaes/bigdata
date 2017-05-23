#coding:utf-8
import matplotlib.pyplot as plt
import pyspark
import os
import sys 

os.environ["SPARK_HOME"]="C:\Users\sujae\code\s_201311240\spark-2.0.0-bin-hadoop2.7"
os.environ["PYLIB"]=os.path.join(os.environ["SPARK_HOME"],'python','lib')
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'py4j-0.10.1-src.zip'))
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'pyspark.zip'))


myConf=pyspark.SparkConf()
spark = pyspark.sql.SparkSession.builder.master("local").appName("myApp").config(conf=myConf).config('spark.sql.warehouse.dir','file:///C:/Users/sujae/code/s_201311240/data').getOrCreate()


myRddex=spark.sparkContext\
    .textFile(os.path.join("data","ds_spark_wiki.txt"))

wc2=myRddex\
    .flatMap(lambda x:x.split())\
    .map(lambda x:(x,1))\
    .reduceByKey(lambda x,y:x+y)\
    .map(lambda x:(x[1],x[0]))\
    .sortByKey(False)\
    .take(100)
        
#         기계에서 하는거랑 마스터에서 하는거랑 차이는 reducebykey와 groupbykey 차이
count = map(lambda x: x[0], wc2)
word = map(lambda x: x[1], wc2)
plt.figure(figsize = (5,18))
plt.barh(range(len(count)), count, color = 'blue')
plt.yticks(range(len(count)), word)
plt.show()