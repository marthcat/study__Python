from multiprocessing.dummy import current_process
from urllib.request import Request
from urllib.request import urlopen
import json
import pandas as pd
import numpy as np
from urllib import parse
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pymysql
pymysql.install_as_MySQLdb()
# ModuleNotFoundError: No module named 'MySQLdb'
# 해결:Pymysql이 mysqlDB처럼 인식하게 코딩
import sqlalchemy


#naver map api key
# https://www.ncloud.com/
client_id= "i2kspvwhmm"
client_pw = 'xECyjX225lLeh1x9PkpFqqHhQjQdkNb01XvvjKBX'
api_url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query='

#MySQL 에서 데이터 pandas로 가져오기 
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='Teamprj',charset='utf8')
cur= conn.cursor()
sql = "SELECT * FROM good"
df_food = pd.read_sql_query(sql, conn)
# print(df_food)

#네이버 api 사용 위도 경도 

geo_coordi= [] #위,경도 리스트
for add in df_food['addr1']:
    add_urlenc = parse.quote(add)
    url = api_url + add_urlenc
    request = Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_pw)
    try:
        response = urlopen(request)
    except HTTPError == e:
        print('HTTP Error')
        latitude = None
        longitude = None
        
    else:
        rescode = response.getcode()
        if rescode == 200:
            response_body = response.read().decode('utf-8')
            response_body = json.loads(response_body)   # json
            if response_body['addresses'] == [] :
                print("'result' not exist!")
                latitude = None
                longitude = None
            else:
                latitude = response_body['addresses'][0]['y']
                longitude = response_body['addresses'][0]['x']
                print("Success!")
        else:
            print('Response error code : %d' % rescode)
            latitude = None
            longitude = None
        
    geo_coordi.append([latitude, longitude])
    
    

np_geo_coordi = np.array(geo_coordi)
df_geo_coordi = pd.DataFrame({"addr1": df_food['addr1'].values,
                              "lat": np_geo_coordi[:, 0],
                              "lon": np_geo_coordi[:, 1]})

#음식점 데이터와 위도경도데이터 합치기  
df_seoul_food = pd.merge(df_food, df_geo_coordi)
# print(df_seoul_food)

# 완성된 데이터프레임 sql에 새로운 테이블에 저장 
# sqlalchemy <- 파이썬 데이터 프레임을 sql 테이블에 저장해주는 역할
engine = sqlalchemy.create_engine("mysql://root:1234@127.0.0.1:3306/teamPrj",encoding='utf8')
conn1 = engine.connect()
df_seoul_food.to_sql(name="good_food", con=engine, if_exists='append',index=False)
conn1.close()


