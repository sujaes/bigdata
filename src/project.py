#coding:UTF-8
from bs4 import BeautifulSoup
import requests
f=open('it_list.txt','w')
for i in range(1,3):
    _url = 'http://news.joins.com/money/itview/list/'
    _url = _url+str(i)
    r=requests.get(_url)
    soup=BeautifulSoup(r.text,'html.parser')
    it_list=soup.find_all('strong',class_="headline mg")
    f.write('\n')
    print '--------'
    for data in it_list[1:]:
        print data.a.text
        f.write((data.a.text).encode('utf-8'))
        f.write((' ').encode('utf-8'))
        f.write(('\n').encode('utf-8'))
f.close()
import os
import sys 
os.environ["SPARK_HOME"]="C:\Users\sujae\code\s_201311240\spark-2.0.0-bin-hadoop2.7"
os.environ["PYLIB"]=os.path.join(os.environ["SPARK_HOME"],'python','lib')
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'py4j-0.10.1-src.zip'))
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'pyspark.zip'))
import pyspark
myConf=pyspark.SparkConf()
spark = pyspark.sql.SparkSession.builder.master("local").appName("myApp").config(conf=myConf).config('spark.sql.warehouse.dir','file:///C:/Users/sujae/code/s_201311240/data').getOrCreate()
import matplotlib.pyplot as plt

myRddex=spark.sparkContext\
    .textFile(os.path.join("it_list.txt"))
    


wc2=myRddex\
    .flatMap(lambda x:x.split())\
    .map(lambda x:(x,1))\
    .reduceByKey(lambda x,y:x+y)\
    .map(lambda x:(x[1],x[0]))\
    .sortByKey(False)\
    .take(100)
        
count = map(lambda x: x[0], wc2)
word = map(lambda x: x[1], wc2)
# plt.figure(figsize = (5,60))
# plt.barh(range(len(count)), count, color = 'blue')
# plt.yticks(range(len(count)), word)
# plt.show()

df = spark.createDataFrame(
    [
        [1,u'결혼하러 강남간다는 옛말…휘청이는 강남 웨딩홀'],
        [1,u'헌재 혼잣말로 한 영어 욕설 모욕적인 표현으로 단정 못해'],
        [0,u'현대차에 가세한 또 한 명의 스타 디자이너, 사이먼 로스비가 디자인 차는?'],
        [1,u'제주서 고병원성 AI 간이검사 양성 추가 발생…12만 마리 살처분 예정'],
        [1,u'공짜표 법정다툼 6년만에 상영관 승리'],
        [1,u'빅뱅 탑 경찰청 홍보단서 퇴출'],
        [0,u'우리 강아지 벌레 있어요 도와주세요'],
        [0,u'우리 강아지 귀여워 너 사랑해'],
        [1,u'강아지 공원 가지마 바보같이'],
        [1,u'강아지 음식 구매 마세요 바보같이'],
        [0,u'가야사 복원이 여의도 핫이슈 떠오른 까닭'],
        [0,u'오늘의 날씨 6월 6일'],
        [0,u'물을 위한 마라톤'],
        [0,u'창조인상 받은 제주올레길 주역 … 서명숙 이사장, 국민훈장 동백장'],
        [0,u'올해만 8만여 대, 현대기아 친환경차 궤도 올랐다'],
        [0,u'어르신 자선공연 19년 “봉사도 중독 되나봐요”'],
        [0,u'더러워진 흰색 가죽 운동화, 선크림으로 닦으면 말끔'],
        [0,u'올여름 패션 마침표, 슬리퍼'],
        [0,u'이슬람 사원이 보증합니다 … 냉장 할랄고기 내놓는 몇 안 되는 곳'],
        [0,u'복부비만 예방, 촉촉한 피부 … 우유가 돕습니다'],
        [1,u'빈집 털던 전과 16범, 집주인 아들에게 혼쭐난 사연'],
        [1,u'아직 교정중인데, 치과 폐업하고 연락두절…피해사례 속출'],
        [1,u'서울시, 가뭄 상황 관심단계 발령… 샤워는 짧게 빨래는 모아서'],
        [1,u'AI 위기경보 심각 격상…전국 가금농가에 일시이동중지 명령'],
        [1,u'제주 농가 AI 고병원성 바이러스 확진…위기경보 심각으로 높여'],
        [0,u'현충일인 6일 전국에 단비'],
        [0,u'심상찮은 현대기아차 친환경차…누적 하이브리드카 판매 50만대 돌파'],
        [1,u'빅뱅 탑 부대 옮긴 뒤 직위해제 대마초 때문에…'],
        [1,u'대마초 흡연 빅뱅 탑 불구속 기소.. 과거 지드래곤은 기소유예, 왜?'],
        [1,u'갓 태어난 아기 비닐봉지에 버린 여고생 입건'],
        [1,u'아동학대 논란 안아키 한의사, 최소 12명 더 있다'],
        [0,u'전자담배 아이코스 판매 효과? 편의점 CU 주가 활짝'],
        [0,u'국정원 감찰실장에 조남관 서울고검 검사 내정'],
        [1,u'돈봉투 만찬 이영렬·안태근 감찰 종료...7일쯤 징계 윤곽'],
        [0,u'생방송 중 꾸벅꾸벅, 그래도 사랑받는 설현 닮은 아나운서'],
        [1,u'다문화가정 초등학생 학업중단율 0.9%...일반 가정의 4.5배'],
        [1,u'5세 실명케 한 동거남·폭행 방치한 엄마...엄마 걱정해 비명 안 질러'],
        [1,u'정규직에 차별받은 기아차 비정규직 노조'],
        [0,u'미국 스타벅스에 아무도 앉지 않는 원형 식탁이 마련된 이유'],
        [1,u'이례적 초여름 AI 군산 오골계 종계 농장이 발원지'],
        [0,u'교도소에 드론 띄워 재소자 감시'],
        [1,u'재판 6개월차 최순실의 변신'],
        [1,u'중간고사 한 번 망치면 자퇴까지? 입시 절벽 고민 큰 고1'],
        [1,u'재판 6개월차 최순실의 변신'],
        [0,u'오늘의 날씨 6월 5일'],
        [1,u'재판 6개월차 최순실의 변신'],
        [0,u'서울로7017, 어떻게 가꾸어 갈지 시민 목소리 더 들어야'],
        [1,u'우유 급식 전면 시행하겠다는 정부 … 학교 먹기 싫다고 버리는 애 많은데'],
        [1,u'권익현 자유한국당 고문 별세'],
        [0,u'실적 회복 르노삼성, 신규 채용 늘려 화답'],
        [0,u'도시 속 숲 아닌 숲속 도시 조성, 산림정책 발상 전환할 때'],
        [0,u'직원 아이디어 발표회 큰 성과…승객 중심 서비스 개선에 총력'],
        [0,u'한글교실·건강관리·마실음악회 경로당 143곳은 행복 공동체'],
        [0,u'SK하이닉스 15조5000억원, LG생활건강 3800억원 투자 약속'],
        [0,u'찾아가는 Good-Job 행복드림 버스, 18~34세 구직 활동비 지원'],
        [1,u'경북 성주 야산서 산불…5시간여 만에 큰불 잡혀'],
        [1,u'정유라 영장 재청구 불투명...추가 혐의 적용하려면 덴마크 정부 승인 필요'],
        [1,u'한웅재 검사 웃지말라 … 재판 6개월차 최순실의 3단 변신'],
        [1,u'정유라 거주 미승빌딩, 과거 외벽 붙은 인터넷 주소 치니 YG 관계사 나와'],
        [1,u'중간고사 한번 망치면 자퇴?.. 입시 절벽에 고민 커진 고1'],
        [1,u'분노 유발자 층간소음…이웃 간 주먹다짐에 살인까지'],
        [1,u'아들 보고 싶다…덴마크에 있는 아들 귀국 준비 시작한 정유라'],
        [1,u'시각장애 흑인 탑승 거부한 미국 항공사'],
    ],
    ['cls','sent']
)

from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, HashingTF, StopWordsRemover, RegexTokenizer
stopwords=list()
_mystopwords=[u"나",u"너", u"우리"]
for e in _mystopwords:
    stopwords.append(e)

labelIndexer = StringIndexer(inputCol="cls", outputCol="label")
regexTok = RegexTokenizer(inputCol="sent", outputCol="wordsRegex", pattern="\\s+")
#tokenizer = Tokenizer(inputCol="sent", outputCol="words")
stop = StopWordsRemover(inputCol="wordsRegex", outputCol="nostops")
_stopwords=stop.getStopWords()
for e in _stopwords:
    stopwords.append(e)
stop.setStopWords(stopwords)

hashingTF = HashingTF(inputCol="nostops", outputCol="features")
pipeline = Pipeline(stages=[labelIndexer,regexTok,stop,hashingTF])
model=pipeline.fit(df)
trainDf = model.transform(df)

trainDf.select('cls','label','features').show()

from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import Vectors

trainRdd = trainDf\
    .rdd\
    .map(lambda row: LabeledPoint(row.label,Vectors.fromML(row.features)))
trainRdd.take(1)

from pyspark.ml.classification import *
lr = LogisticRegression(maxIter=10, regParam=0.01)
lrModel = lr.fit(trainDf)
# print "* summary: ", lrModel.summary
# print "* coefficients: ", lrModel.coefficients
# print "* intercept: ", lrModel.intercept

from pyspark.mllib.classification import LogisticRegressionWithSGD
lrm = LogisticRegressionWithSGD.train(trainRdd, iterations=10)

from pyspark.ml.classification import DecisionTreeClassifier

dt = DecisionTreeClassifier(labelCol="label", featuresCol="features")
model=dt.fit(trainDf)


from pyspark.mllib.regression import LabeledPoint
#_rdd=df.rdd.map(lambda x:LabeledPoint(x.class,[1,1]))
_rdd=df.rdd.map(lambda x:LabeledPoint(x.cls,[1,1]))
_rdd.first()

from pyspark.mllib.clustering import LDA
#from pyspark.mllib.linalg import SparseVector, Vector, Vectors
from pyspark.ml.feature import CountVectorizer, RegexTokenizer

regexTok = RegexTokenizer(inputCol="sent", outputCol="wordsRegex", pattern="\\s+")
reDf=regexTok.transform(df)
cv = CountVectorizer(inputCol="wordsRegex", outputCol="cv")
cvModel=cv.fit(reDf)
cvDf=cvModel.transform(reDf)

from pyspark.mllib.linalg import SparseVector, Vector, Vectors
testRdd = cvDf.select("cls", "cv").rdd.map(lambda (x,y): [x,Vectors.fromML(y)])

voca=cvModel.vocabulary
nword=len(voca)
ntopic=20
ndoc=df.count()
print u'단어수: ',nword
print u'문서수: ',ndoc
for i,v in enumerate(voca):
    print i,v,'-'
ldaModel = LDA.train(testRdd, k=ntopic, seed=1)
topic=ldaModel.describeTopics(maxTermsPerTopic=10)
for k in range(ntopic):
    print "* Topic: ", k, topic[k]
for k in range(ntopic):
    print "Topic ",k
    for w in topic[k][0]:
        print voca[w],
    print "\n-----"
word_topic=ldaModel.topicsMatrix()
print len(word_topic)
word_topic[0]
# for k in range(ntopic):
#     for w in range(nword):
    
        
#print voca[w], '\t\t',word_topic[w]
    
sum=0
for i in range(len(word)):
    for j in range(nword):
        if(word[i]==voca[j]):
            sum = sum+1
print u'-------부정적기사--------'            
print sum
plt.figure(figsize = (5,60))
plt.barh(range(len(count)), count, color = 'blue')
plt.yticks(range(len(count)), word)
plt.show()
