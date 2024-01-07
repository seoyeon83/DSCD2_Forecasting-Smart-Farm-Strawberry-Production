# DSCD2_Forecasting-Smart-Farm-Strawberry-Production
- 2023년 3학년 2학기 데이터사이언스캡스톤디자인2 아카이빙 레포지토리입니다.
- 코드 정리 중...

<br/><br/>
## 프로젝트 정보
- 현재 농업은 평균 연령 증가, 기후 변화, 환경 오염과 같은 다양한 문제로 인해 지속 가능성에 어려움을 겪고 있습니다.
- 이런 상황에서 스마트팜은 혁신적인 대안으로 부상하고 있습니다.
- 본 프로젝트는 스마트팜의 효율적인 운영을 지원하기 위해 **딸기 생산량을 예측하는 모델**을 제공합니다.
- 프로젝트 기간
  
    > 전체:
    > 
    > 모델 구현:
    
<br/><br/>
## 팀원 소개
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/seoyeon83">
        <img src="https://github.com/seoyeon83/DSCD2_Forecasting-Smart-Farm-Strawberry-Production/blob/main/images/seoyeon83.png" width="100px;" alt=""/>
        <br/>
        <sub><b>김서연</b></sub>
      </a>
        <br>
        <sub>데이터사이언스학과</sub>
        <br>
        <sub>21학번</sub>
    </td>
    <td align="center">
      <a href="https://github.com/economy0">
        <img src="https://github.com/seoyeon83/DSCD2_Forecasting-Smart-Farm-Strawberry-Production/blob/main/images/economy0.png" width="100px;" alt=""/>
        <br />
        <sub><b>경재영</b></sub>
      </a>
        <br>
        <sub>데이터사이언스학과</sub>
        <br>
        <sub>21학번</sub>
    </td>
    <td align="center">
      <a href="https://github.com/SongyeonK">
        <img src="https://github.com/seoyeon83/DSCD2_Forecasting-Smart-Farm-Strawberry-Production/blob/main/images/SongyeonK.png" width="100px;" alt=""/>
        <br />
        <sub><b>김송연</b></sub>
      </a>
        <br>
        <sub>데이터사이언스학과</sub>
        <br>
        <sub>21학번</sub>
    </td>
    <td align="center">
      <a href="https://github.com/eunbinee14">
        <img src="https://github.com/seoyeon83/DSCD2_Forecasting-Smart-Farm-Strawberry-Production/blob/main/images/eunbinee14.png" width="100px;" alt=""/>
        <br />
        <sub><b>이은빈</b></sub>
      </a>
        <br>
        <sub>데이터사이언스학과</sub>
        <br>
        <sub>21학번</sub>
    </td>
    <td align="center">
      <a href="https://github.com/cchhooinaa">
        <img src="https://github.com/seoyeon83/DSCD2_Forecasting-Smart-Farm-Strawberry-Production/blob/main/images/cchhooinaa.png" width="100px;" alt=""/>
        <br />
        <sub><b>조인아</b></sub>
      </a>
        <br>
        <sub>데이터사이언스학과</sub>
        <br>
        <sub>21학번</sub>
    </td>
    <td align="center">
      <a href="https://github.com/onegyulim">
        <img src="https://github.com/seoyeon83/DSCD2_Forecasting-Smart-Farm-Strawberry-Production/blob/main/images/onegyulim.png" width="100px;" alt=""/>
        <br />
        <sub><b>한규림</b></sub>
      </a>
        <br>
        <sub>데이터사이언스학과</sub>
        <br>
        <sub>21학번</sub>
  </tr>
  <tr>
    </td>
  </tr>
</table>
</td>

<br/><br/>
## 1. 개발 환경
- Google Colaboratory
- python 3.10.12

<br/><br/>
## 2. 프로젝트 파이프라인
![pipeline](https://github.com/seoyeon83/DSCD2_Forecasting-Smart-Farm-Strawberry-Production/assets/113918499/23331fc3-6d20-442d-8eef-8a14266ef5f8)

<br/><br/>
## 3. 데이터 수집
> 농촌진흥청, 스마트팜 현장 농가 데이터 내의 시설 채소 중 딸기 농가의 환경, 생육 데이터 이용
  - **환경 데이터**
    - 농가의 내외부 환경 센서 측정 데이터
    - 1시간 단위 측정
    - 기상 정보: 일사량, 누적일사량, 풍향, 풍속, 강우 여부, 외부 온도
    - 내부 시설 정보: 내부 온도, 내부 상대습도, 잔존CO2, 토양 온도
      
  - **생육 데이터**
    - 농가별 4개 작물 개체의 생육 지표 데이터(농가에서 직접 측정)
    - 1주 단위 측정
    - 생육 정보: 액아구분, 초장, 엽수, 엽장, 엽폭, 엽병장, 관부직경, 화방번호, 화방별착과수

  - **기상청 데이터**
    - 기상자료개방포털 내의 종관기상관측(ASOS)을 이용하여 환경 데이터 중 기상 데이터 추가 수집
   
  - **농가 선정 기준**
    - 환경 데이터 : 결측치가 50% 이상일 경우 제외
    - 생육 데이터 : 3주 이상 기록이 없을 경우 제외 (통일되지 않은 기록 방식)

<br/><br/>
## 4. 데이터 전처리
- **환경 데이터**
  - 기록된 측정 시간의 분 단위를 제거
  - 1시간 단위로 맞춰 통일
 
- **생육 데이터**
  - 수기로 측정한 데이터이기 때문에 누락 데이터 존재하는 경우
  - 동일한 농가, 날짜, 개체번호, 본주를 기준으로 ‘엽수, 엽장, 엽폭, 엽병장, 관부직경’ 변수 데이터 수기 전처리
 
- **주 차 매핑**
  1) 정식일을 기준으로 주 차 매핑 진행
  2) 정식일과 데이터 측정 시작일의 차이가 존재할 경우 결측치로 간주
  
- **데이터 보간**
  1) 선형보간 
  2) 편차평균보간

- **기상데이터 결측치 대체**
    - 일사량, 외부 온도 변수의 결측치는 농가와 가까운 지역의 기상청 외부 데이터로 대체
      
- **병합 과정에서 나온 문제점**
    > 데이터를 시간 단위에서 주 단위로 통합할 때, 시간 단위 데이터가 가지는 추세를 충분히 고려해야함 ⇒ *다운샘플링 진행*
    - 이동 창 통계량 유형(MWS)
      
      - 시간 단위였던 데이터의 최대, 최소, 평균을 구해 일 단위로 변환
      - 일별로 추출한 데이터를 평균값으로 구해 주 단위로 변환
    - 주간 및 야간 유형(DAN)
      
      - 데이터를 주간, 야간으로 구분해 일별 흐름을 반영
     
- **변수 선정**
    - 종속변수 : 화방별 착과수
    - 독립변수 : 화방별 착과수를 제외한 생육 데이터, 환경(MWS, DAN) 데이터의 변수
    - 지연변수 ‘지난주 착과수’ 추가 : 예측일 대비 날짜가 가까울수록 상관관계가 커짐
 
  
