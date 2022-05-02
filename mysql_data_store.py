# 터미널에서 pymysql 설치
#python3 -m pip install PyMySQL

import pymysql
import csv 

# MySQL DB에 접속
conn = pymysql.connect(host='localhost',
                       port=3306, 
                       user='root',
                       passwd='mysql423',
                       db = 'card_db',
                       charset='utf8') # 한글 깨짐 방지 

# 커서 생성
cur = conn.cursor()



## 카드사용금액정보(상대성지표) 데이터 삽입 ###

# 카드사용금액정보(상대성지표) 테이블 생성
cur.execute('DROP TABLE IF EXISTS card;')

cur.execute("""CREATE TABLE card (
                card_id INT NOT NULL,
                기준월 DATE, 
				연도 INT,
				월 INT,
                업종_대분류 VARCHAR(32),
                업종_중분류 VARCHAR(32),
                연령대 INT,
                성별 VARCHAR(32), 
                시군구 VARCHAR(32),
                금액지표 INT,
                건수지표 INT,
                PRIMARY KEY (card_id)
                );
			""")

# 데이터베이스에 저장할 csv file
with open('data/1Q_Seoul_dataset.csv', 'r') as card_csvfile:
    reader = csv.reader(card_csvfile, delimiter=',')
    card_data = [x for x in reader] # csv 파일을 리스트로 저장

# header 삭제
card_data.pop(0)

# Id 추가
for i in range(len(card_data)):
    card_data[i].insert(0, i)

# 다중 삽입문을 위한 빈 텍스트 생성
card_insert_text = ''

# 튜플형태로 변경하고 ','로 나누어 데이터 삽입
for i, card_text in enumerate(card_data):
    card_insert_text += str(tuple(card_text)) # 튜플로 변경하여 저장
    card_insert_text += ',' # ','로 데이터 나눔

card_insert_text = card_insert_text[:-1] # 삽입문의 마지막 ',' 제거


# 삽입문 전송
cur.execute("""INSERT INTO card (
                            card_id, 기준월, 연도, 월, 업종_대분류, 업종_중분류,
                            연령대, 성별, 시군구, 금액지표, 건수지표
                            ) VALUES {};
            """.format(card_insert_text))

# 데이터베이스에 내용 전송
conn.commit()



## 서울시 코로나19 확진자 발생동향 데이터 삽입 ###

# 서울시 코로나19 확진자 발생동향 테이블 생성
cur.execute('DROP TABLE IF EXISTS all_c;')

cur.execute("""CREATE TABLE all_c (
                all_id INT NOT NULL,
                기준일 DATE, 
				연도 INT,
				월 INT,
                일 INT,
                서울시_확진자 INT,
                서울시_추가확진 INT,
                전국_확진 INT, 
                전국_추가확진 INT,
                PRIMARY KEY (all_id)
                );
			""")

# 데이터베이스에 저장할 csv file
with open('data/corona_all.csv', 'r') as all_csvfile:
    reader = csv.reader(all_csvfile, delimiter=',')
    all_data = [x for x in reader] # csv 파일을 리스트로 저장

# header 삭제
all_data.pop(0)

# Id 추가
for j in range(len(all_data)):
    all_data[j].insert(0, j)

# 다중 삽입문을 위한 빈 텍스트 생성
all_insert_text = ''

# 튜플형태로 변경하고 ','로 나누어 데이터 삽입
for j, all_text in enumerate(all_data):
    all_insert_text += str(tuple(all_text)) # 튜플로 변경하여 저장
    all_insert_text += ',' # ','로 데이터 나눔

all_insert_text = all_insert_text[:-1] # 삽입문의 마지막 ',' 제거


# 삽입문 전송
cur.execute("""INSERT INTO all_c (
                            all_id, 기준일, 연도, 월, 일,
                            서울시_확진자, 서울시_추가확진, 전국_확진, 전국_추가확진
                            ) VALUES {};
            """.format(all_insert_text))

# 데이터베이스에 내용 전송
conn.commit()



## 서울시 코로나19 자치구별 확진자 발생동향 데이터 삽입 ###

# 서울시 코로나19 자치구별 확진자 발생동향 테이블 생성
cur.execute('DROP TABLE IF EXISTS gu_c;')

cur.execute("""CREATE TABLE gu_c (
                gu_id INT NOT NULL,
                기준일 DATE, 
				연도 INT,
				월 INT,
                일 INT,
                구 VARCHAR(32),
                구분 VARCHAR(32),
                확진자수 INT,
                PRIMARY KEY (gu_id)
                );
			""")

# 데이터베이스에 저장할 csv file
with open('data/corona_gu.csv', 'r') as gu_csvfile:
    reader = csv.reader(gu_csvfile, delimiter=',')
    gu_data = [x for x in reader] # csv 파일을 리스트로 저장

# header 삭제
gu_data.pop(0) 

# Id 추가
for k in range(len(gu_data)):
    gu_data[k].insert(0, k)

# 다중 삽입문을 위한 빈 텍스트 생성
gu_insert_text = ''

# 튜플형태로 변경하고 ','로 나누어 데이터 삽입
for k, gu_text in enumerate(gu_data):
    gu_insert_text += str(tuple(gu_text)) # 튜플로 변경하여 저장
    gu_insert_text += ',' # ','로 데이터 나눔

gu_insert_text = gu_insert_text[:-1] # 삽입문의 마지막 ',' 제거


# 삽입문 전송
cur.execute("""INSERT INTO gu_c (
                            gu_id, 기준일, 연도, 월, 일, 
                            구, 구분, 확진자수
                            ) VALUES {};
            """.format(gu_insert_text))

# 데이터베이스에 내용 전송
conn.commit()



# 데이터베이스에 제대로 저장되었는지 확인

# card 테이블 데이터 확인 
cur.execute("SELECT * FROM card")
result_card = cur.fetchall()
print('card')
print(result_card[-3:]) # 마지막 3개 row 출력 
print("------------------------------------")

# all_c 테이블 데이터 확인 
cur.execute("SELECT * FROM all_c")
result_all = cur.fetchall()
print('corona_all')
print(result_all[-3:]) # 마지막 3개 row 출력 
print("------------------------------------")

# gu_c 테이블 데이터 확인 
cur.execute("SELECT * FROM gu_c")
result_gu = cur.fetchall()
print('corona_gu')
print(result_gu[-3:]) # 마지막 3개 row 출력 



# 데이터베이스 연결 종료
conn.close()  