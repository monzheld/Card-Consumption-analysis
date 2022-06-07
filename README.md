# 카드 소비 데이터 분석
위드 코로나 시대 카드 소비 데이터 분석을 통한 2023년 1분기 카드 상품 기획

<br>

## 제작 기간
2022.04.20 ~ 2022.05.02

<br>

## 발표 자료
- [📘 Presentation](https://drive.google.com/file/d/1lnMJn4KfeJUzAmgHTuovSxUKE58PHY17/view?usp=sharing)

<br>

## 프로젝트 기획 의도
코로나19 상황이 장기화되면서 변화된 소비 트렌드 파악 및 위드 코로나 시대 맞춤 카드 상품 기획

<br>

## 문제 정의
코로나19 장기화로 변화된 소비 트렌드로 인한 새로운 소비 인사이트 탐색 필요 

<br>

## 가설 검정
- 소비 건수가 많은 연령대와 소비 금액이 많은 연령대는 동일하다. -> **False**
- 코로나19 상황에서도 연도별 카드 소비 트렌드는 다르다. -> **True**
- 2022년 1분기에 코로나19 확진자가 급증하면서 2020년 1분기보다 병원 소비가 증가했다. -> **True**
- 코로나19 발생 이후 연도별 인터넷Mall 소비에 차이가 있다. -> **True**
- 가맹점의 지역구와 업종은 연관이 있다. -> **True**
- 지역구별 소비 건수의 분포는 차이가 있다. -> **True**


<br>

## 사용 기술

#### EDA
- pandas
- numpy
- matplotlib
- seaborn

#### 데이터 적재
- MySQL

#### 대시보드 개발
- Docker
- Metabase

#### 가설 검정
- scipy.stats
- Two sample Chi-square Test
- One sample Chi-square Test
- statsmodels
- ANOVA Test

<br>

## 데이터셋
- 카드사용금액정보(상대성지표) (2020.01-2020.03, 2021.01-2021.03, 2022.01-2022.03)
- 전처리 후 데이터셋 크기: (398494, 10)
- [데이터 출처](https://bdp.kt.co.kr/invoke/SOKBP2603/?goodsCode=BCCSALERATE002019V01)

<br>

- 서울시 코로나19 확진자 발생동향
- 전처리 후 데이터셋 크기: (787, 8)
- [데이터 출처](https://data.seoul.go.kr/dataList/OA-20461/S/1/datasetView.do)

<br>

- 서울시 코로나19 자치구별 확진자 발생동향
- 전처리 후 데이터셋 크기: (40924, 7)
- [데이터 출처](https://data.seoul.go.kr/dataList/OA-20470/S/1/datasetView.do)

<br>

## 결론

#### 타깃 
- 30대 여성

#### 업종
- 유통업영리

#### 카드 상품 종류
- PLCC 카드

=> 2020년 ~ 2022년 1분기 카드 소비 데이터 분석 결과, <br> 
**2023년 1분기에는** 소비 금액과 건수가 가장 많은 연령대와 성별인 **30대 여성을 타깃**으로 <br>
2020년 1월 대비 소비가 가장 많이 증가하고 연도별 소비가 가장 많은 업종인 **유통업영리 업종을 대상으로 한** <br>
**PLCC(상업자 표시 신용카드) 카드 상품을 기획**.
