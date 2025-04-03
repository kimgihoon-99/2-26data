# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:02:08 2025

@author: Admin
"""
import numpy as np
import pandas as pd
import pymysql
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()
import MySQLdb

host = 'localhost'
user = 'root'
password = 'lovekgh33'
db = 'test'
charset = 'utf8'

df = pd.read_csv('./data/2024년 1월 국내노선 여객 이용률.csv')
df.rename(columns = {'대한항공' : 'KAL',
                     '아시아나' : 'AAR',
                     '에어부산' : 'ABL',
                     '이스타항공' : 'ESR',
                      '제주항공' : 'JJA',
                      '진에어' : 'JNA',
                      '티웨이항공' : 'TWB',
                     '에어로케이' : 'EOK' }, inplace = True)
                    


engine = create_engine(f"mysql+mysqldb://{user}:{password}@{host}/{db}") 
conn = engine.connect()

df.to_sql(name = 'air_month', con=engine, if_exists = 'replace', index=False)


df1 = pd.read_csv('./data/2024년 1월 국내노선 여객 이용률.csv')
df2 = pd.read_csv('./data/2024년 2월 국내노선 여객 이용률.csv')
df3 = pd.read_csv('./data/2024년 3월 국내노선 여객 이용률.csv')
df4 = pd.read_csv('./data/2024년 4월 국내노선 여객 이용률.csv')
df5 = pd.read_csv('./data/2024년 5월 국내노선 여객 이용률.csv')
df6 = pd.read_csv('./data/2024년 6월 국내노선 여객 이용률.csv')
df7 = pd.read_csv('./data/2024년 7월 국내노선 여객 이용률.csv')
df8 = pd.read_csv('./data/2024년 8월 국내노선 여객 이용률.csv')

print(df3)

df1_mean = df1['이용율'].mean()   # 82.17064
df2_mean = df2['이용율'].mean()   # 84.207
df3_mean = df3['이용률'].mean()   # 77.67876
df4_mean = df4['이용률'].mean()   # 83.6284403669725
df5_mean = df5['이용률'].mean()   # 84.9500
df6_mean = df6['이용률'].mean()   # 81.82905
df7_mean = df7['이용률'].mean()   # 77.7151
df8_mean = df8['이용률'].mean()   # 84.825


# 한글을 표기하기 위한 글꼴 변경(원도우, macOS에 대한 각각 처리)
from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname= path).get_name()
    rc('font', family = font_name)
elif platform.sytem() == 'Darwin':
    rc('font', family = 'AppleGothic')
else:
    print('Check your OS system')




df_labels = ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월"]
means = [82.17064, 84.207, 77.67876, 83.62844, 84.9500, 81.82905, 77.7151, 84.825]

# 막대 그래프 그리기
plt.figure(figsize=(10, 6))
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(means)))  # 색상 지정

plt.bar(df_labels, means, color=colors, alpha=0.8)

# 그래프 제목 및 축 레이블
plt.title("이용률 평균 비교", fontsize=14)
plt.xlabel("월", fontsize=12)
plt.ylabel("이용률", fontsize=12)
plt.ylim(75, 90)  # Y축 범위 설정

# 값 표시
for i, v in enumerate(means):
    plt.text(i, v + 0.3, f"{v:.2f}", ha='center', fontsize=10)

# 그래프 출력
plt.show()

df1 = pd.read_csv('./data/2024년 총 국내노선 여객 이용률.csv')

KAL = df1['항공사'].value_counts().get('KAL', 0) # 166
AAR = df1['항공사'].value_counts().get('AAR', 0) # 102
ABL = df1['항공사'].value_counts().get('ABL', 0) # 42
ESR = df1['항공사'].value_counts().get('ESR', 0) # 57
JJA = df1['항공사'].value_counts().get('JJA', 0) # 98
JNA = df1['항공사'].value_counts().get('JNA', 0) # 218
TWB = df1['항공사'].value_counts().get('TWB', 0) # 67
EOK = df1['항공사'].value_counts().get('EOK', 0) # 14
ASV = df1['항공사'].value_counts().get('ASV', 0) # 15


# 항공사별 개수 데이터
airline_counts = {
    'KAL': 166, 'AAR': 102, 'ABL': 42, 'ESR': 57, 'JJA': 98,
    'JNA': 218, 'TWB': 67, 'EOK': 14, 'ASV': 15
}

# 데이터 분리
airlines = list(airline_counts.keys())  # 항공사 코드 리스트
counts = list(airline_counts.values())  # 개수 리스트

# 막대그래프 생성
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
plt.bar(airlines, counts, color='skyblue', edgecolor='black')

# 그래프 제목 및 라벨 설정
plt.title("항공사별 운항 횟수", fontsize=14)
plt.xlabel("항공사 코드", fontsize=12)
plt.ylabel("운항 횟수", fontsize=12)

# 각 막대 위에 숫자 표시
for i, count in enumerate(counts):
    plt.text(i, count + 5, str(count), ha='center', fontsize=10)

# 그리드 추가 (선택 사항)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 그래프 표시
plt.show()

adult = df1['성인'].sum() # 17923697
child = df1['유아'].sum() # 209327

# 데이터 설정
labels = ['성인', '유아']
sizes = [17923697, 209327]  # 성인과 유아의 총합
colors = ['skyblue', 'lightcoral']  # 색상 설정
explode = (0.1, 0)  # 성인을 강조 (조금 튀어나오게 설정)

# 파이 차트 생성
plt.figure(figsize=(7, 7))
plt.pie(
    sizes, labels=labels, autopct='%1.1f%%', colors=colors, 
    explode=explode, startangle=140, shadow=True
)

# 그래프 제목 추가
plt.title("성인 vs 유아 인원수 비율", fontsize=14)

# 그래프 표시
plt.show()

adult = df1['성인'].mean() # 22979
child = df1['유아'].mean() # 269

# 데이터 설정
categories = ['성인', '유아']
values = [22979, 269]  # 성인과 유아의 평균값
colors = ['skyblue', 'lightcoral']  # 색상 설정

# 막대그래프 생성
plt.figure(figsize=(6, 5))
plt.bar(categories, values, color=colors, edgecolor='black')

# 그래프 제목 및 라벨 추가
plt.title("평균 성인 vs 유아 승객 수", fontsize=14)
plt.xlabel("구분", fontsize=12)
plt.ylabel("평균 승객 수", fontsize=12)

# 각 막대 위에 숫자 표시
for i, v in enumerate(values):
    plt.text(i, v + 500, str(v), ha='center', fontsize=10)

# y축 범위 조정 (가독성을 위해)
plt.ylim(0, max(values) * 1.2)

# 그래프 표시
plt.show()
















