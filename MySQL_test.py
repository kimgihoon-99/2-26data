# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:51:31 2025

@author: Admin


MySQL 연동


pip install pymysql

"""
import pymysql
import pandas as pd

# python mysql에 연결
host = 'localhost'
user = 'root'
password = 'lovekgh33!@'
db_name = 'sakila'

# 접속 : pymysql.connect()
# host=접속주소(IP)
# user = 사용자 아이디
# password = 비밀번호
# db = 데이터베이스
# charset = 인코딩 (utf8)
conn = pymysql.connect(host = host,
                       user = user,
                       password = password,
                       db = db_name,
                       charset = 'utf8')

# 커서 생성 : query를 실행하는 execute()
# key.value => DictCursor
cursor = conn.cursor(pymysql.cursors.DictCursor)

query = '''
SELECT *
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
JOIN customer cu ON r.customer_id = cu.customer_id
JOIN address a ON cu.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE co.country = 'United States'
'''


# execute()로 query 실행
cursor.execute(query)

# 결과를 반환된 테이블의 모든 행을 가져오기 : cursor.fetchall()
execute_result = cursor.fetchall()

# 데이터 프레임
us = pd.DataFrame(execute_result)

# DB 연결 종료
conn.close()





import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# connect python to mysql
host = 'localhost'
user = 'root'
password = 'lovekgh33!@'
db_name = 'sakila'

# pymysql.connect()
conn = pymysql.connect(host=host,
                       user=user,
                       password=password,
                       db=db_name,
                       charset='utf8')

#cursor 생성 : query를 실행하는 excute()
cursor = conn.cursor(pymysql.cursors.DictCursor)

query1 = """
SELECT f.film_id, f.length, f.rating, c.category_id, c.name as category_name
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
JOIN customer cu ON r.customer_id = cu.customer_id
JOIN address a ON cu.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE co.country = 'United States';
"""

query2 = """
SELECT f.film_id, ac.first_name, ac.last_name
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor ac ON ac.actor_id = fa.actor_id
JOIN customer cu ON r.customer_id = cu.customer_id
JOIN address a ON cu.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE co.country = 'United States';
"""

# execute()로 query 실행
cursor.execute(query1)

# 결과로 반환된 테이블의 모든 행을 가져오기
film_result = cursor.fetchall()
film_df = pd.DataFrame(film_result)

cursor.execute(query2)

actor_result = cursor.fetchall()
actor_df = pd.DataFrame(actor_result)

# db 연결 종료
conn.close()

film_df = film_df.drop(film_df.columns[1], axis=1)

Documentary = film_df.loc[film_df['category_name']=='Documentary']
Sports =  film_df.loc[film_df['category_name']=='Sports']
drama = film_df.loc[film_df['category_name']=='Drama']
Animation = film_df.loc[film_df['category_name']=='Animation']
Family = film_df.loc[film_df['category_name']=='Family']

Documentary_mean = Documentary['length'].mean()

Sports_mean = Sports['length'].mean()

drama_mean = drama['length'].mean()

Animation_mean = Animation['length'].mean()

Family_mean = Family['length'].mean()


























