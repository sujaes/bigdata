import matplotlib.pyplot as plt

myRddex=spark.sparkContext\
    .textFile(os.path.join("data","overview.txt"))

wc2=myRddex\
    .flatMap(lambda x:x.split())\
    .map(lambda x:(x,1))\
    .reduceByKey(lambda x,y:x+y)\
    .map(lambda x:(x[1],x[0]))\
    .sortByKey(False)\
    .take(100)
        
count = map(lambda x: x[0], wc2)
word = map(lambda x: x[1], wc2)
plt.figure(figsize = (5,18))
plt.barh(range(len(count)), count, color = 'grey')
plt.yticks(range(len(count)), word)
plt.show()