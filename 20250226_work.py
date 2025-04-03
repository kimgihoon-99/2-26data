import pymysql
from matplotlib import font_manager, rc
import platform
if platform.system() == 'Windows':
    path = 'C:/Windows/Fonts/malgun.ttf'  # Windows: 맑은 고딕 폰트 경로
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
from matplotlib import font_manager, rc
import platform
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


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

# cursor 생성 : query를 실행하는 excute()
cursor = conn.cursor(pymysql.cursors.DictCursor)
query0 = """
        SELECT c.name AS category, COUNT(r.rental_id) AS rental_count, sum(p.amount) as total_amount
        FROM rental r
        JOIN inventory i ON r.inventory_id = i.inventory_id
        JOIN film f ON i.film_id = f.film_id
        JOIN film_category fc ON f.film_id = fc.film_id
        JOIN category c ON fc.category_id = c.category_id
        JOIN customer cu ON r.customer_id = cu.customer_id
        JOIN address a ON cu.address_id = a.address_id
        JOIN city ci ON a.city_id = ci.city_id
        JOIN country co ON ci.country_id = co.country_id
        join payment p on r.rental_id = p.rental_id
        WHERE co.country = 'United States'
        GROUP BY c.name
        ORDER BY  sum(p.amount) DESC;
        """

query = """
        SELECT c.name AS category, COUNT(r.rental_id) AS rental_count
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
GROUP BY c.name
ORDER BY rental_count DESC;
        """

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
SELECT f.film_id, c.name as category_name, ac.first_name, ac.last_name
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor ac ON ac.actor_id = fa.actor_id
JOIN category c ON fc.category_id = c.category_id
JOIN customer cu ON r.customer_id = cu.customer_id
JOIN address a ON cu.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE co.country = 'United States';
"""

cursor.execute(query)
execute_result = cursor.fetchall()
category_df = pd.DataFrame(execute_result)

cursor.execute(query1)
film_result = cursor.fetchall()
film_df = pd.DataFrame(film_result)

cursor.execute(query2)
actor_result = cursor.fetchall()
actor_df = pd.DataFrame(actor_result)

cursor.execute(query0)
execute_result = cursor.fetchall()
payment_df = pd.DataFrame(execute_result)

# db 연결 종료
conn.close()


# 장르별 매출 현황 
# 막대 그래프 그리기
plt.figure(figsize=(15, 6))
plt.bar(payment_df['category'], payment_df['total_amount'], color='pink', edgecolor='black')

# 그래프 제목 및 레이블 설정
plt.xlabel("vedio Categories")
plt.ylabel("Rental Count")
plt.title("Categories/total_amount in the USA (Sakila)")

# 그래프 출력
plt.show()


# 어느 장르의 영화가 가장 인기가 많은지 시각화 하기
# 막대 그래프 그리기
plt.figure(figsize=(15, 6))
plt.bar(category_df['category'], category_df['rental_count'], color='skyblue', edgecolor='black')
# 그래프 제목 및 레이블 설정
plt.xlabel("vedio Categories")
plt.ylabel("Rental Count")
plt.title("Top Rented vedio Categories in the USA (Sakila)")
# 그래프 출력
plt.show()

# 어느 정도의 영화 길이가 가장 인기가 많은지 시각화 하기
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

# 데이터 설정
categories = ["Documentary", "Sports", "Drama", "Animation", "Family"]
length_means = [110.5, 130.08, 127.97, 118.51, 113.29]

# 색상 그라데이션 설정
colors = plt.cm.viridis(np.linspace(0.4, 1.0, len(categories)))  # 'viridis' 컬러맵 사용

# 막대 그래프 그리기
plt.figure(figsize=(10, 6))
bars = plt.bar(categories, length_means, color=colors, edgecolor='black')

# 그래프 제목 및 레이블 설정
plt.xlabel("Movie Categories")
plt.ylabel("Average Runtime (minutes)")
plt.title("Average Runtime by Movie Category")

# 각 막대 위에 수치 표시
for bar, mean in zip(bars, length_means):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, f"{mean:.1f}",
             ha='center', va='top', fontsize=12, color='white', fontweight='bold')

# 그래프 출력
plt.show()

# 어떤 배우를 써야 가장 인기가 많은지 시각화 하기
# full_name 칼럼 생성
actor_df["full_name"] = actor_df["first_name"] + " " + actor_df["last_name"]

# top5 카테고리 중 가장 많이 출연한 배우 상위 10명

target = ["Documentary", "Sports", "Drama", "Animation", "Family"]
filtered_df = actor_df[actor_df["category_name"].isin(target)]
top_10 = filtered_df["full_name"].value_counts().nlargest(10)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 5))
sns.barplot(x=top_10.values, y=top_10.index, palette="viridis")
plt.xlabel("Count")
plt.ylabel("Full Name")
plt.title("Top 10 Most Frequent Full Names in Categories top5")
plt.show()

# top5 카테고리 별 출연한 배우 상위 5명 씩
category_top_5 = (
    filtered_df.groupby("category_name")["full_name"]
    .value_counts()
    .groupby(level=0, group_keys=False)  # category_name 그룹 유지
    .nlargest(5)  # 각 그룹에서 상위 5명 선택
    .reset_index(name="count")  # 컬럼 이름 설정
)

plt.figure(figsize=(12, 6))
sns.barplot(
    data=category_top_5,
    x="full_name",
    y="count",
    hue="category_name",
    dodge=False  # 카테고리별로 같은 축에서 보기 쉽게 설정
)

plt.xticks(rotation=45, ha="right")
plt.xlabel("Actor Name")
plt.ylabel("Movie Count")
plt.title("Top 5 Actors by Category")
plt.legend(title="Category", bbox_to_anchor=(1.05, 1), loc="upper left")  # 범례 위치 조정
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
