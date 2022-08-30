
📌 Introduction
- 프로젝트면: 펫트라슈
- 사이트: petrasche.com
- 기간: 2022.07.07(목) ~ 2022.08.04(목)
- 김주훈: 웹소켓 실시간 채팅 기능
- 나성근: 엘라스틱 서치 검색기능
- 이민기: 아티클, 댓글, 좋아요, 애견 월드컵
- 엄관용: 마이페이지, 유저프로필, 펫프로필
- 한예슬: 회원가입, 로그인(카카오API), 산책커뮤니티(카카오지도API), 팔로우
- Petrasche_front: https://github.com/Super-fast-decision-making/Petrasche_front
- Petrasche_classification: https://github.com/Super-fast-decision-making/Petrasche_classification
![img_1.png](/static/img_1.png)

📌 로그인/회원가입
- 유효성 검사, 아이디 중복 검사, JWT Token사용, 카카오 소셜 로그인

📌 메인 페이지
- 강아지 히스토리 CRUD
- 댓글 CRUD
- 좋아요, 좋아요 취소
- 인기 게시글 상단 노출
- 엘라스틱서치 엔진을 사용한 초성, 해시태그 검색 기능

📌 마이페이지
- 개인 프로필 CRUD
- 펫 프로필 CRUD
- 자신의 반려동물 프로필 이미지 등록시 AI로 강아지vs고양이 구분 (fastAPI사용, ec2 분리)
- 페이지네이션

📌 산책 매칭 페이지
- 카카오 지도 API 사용하여 게시글 등록시 위치 제공
- 매칭 게시판 CRUD (CKEditor 사용)
- 날짜, 지역, 성별, 시간대등 필터 설정으로 검색
- 실시간 채팅 기능 (Websocket & Django Channels)

📌 애견 월드컵
- 자신의 반려동물을 자랑하는 이벤트 페이지
- 이달의 인기 반려동물  (월별 초기화)
 
📌 Nginx / Gunicorn / Daphne
- Nginx : Proxy 역할
- Gunicorn : Django 배포용 WSGI서버 http protocol 요청 처리 (worker : 2)
- Daphne : Django 배포용 ASGI서버 WebSocket portocol 요청 처리


📌 피그마
-

- 회원가입/로그인
- ![img_5.png](/static/img_5.png) ![img_6.png](/static/img_6.png)


- 메인페이지 / 디테일 모달
![img_7.png](/static/img_7.png)
![img_8.png](/static/img_8.png)

- 애견월드컵 뽐뽐뽐
![img_9.png](/static/img_9.png)

- 산책매칭 / 디테일 모달
![img_10.png](/static/img_10.png)
![img_11.png](/static/img_11.png)

- 실시간 채팅 
![img_12.png](/static/img_12.png)

- 마이페이지 / 프로필 / 좋아요
![img_13.png](/static/img_13.png)
![img_14.png](/static/img_14.png)
![img_15.png](/static/img_15.png)

# Petrasche

# 1. 프로젝트 정보
> 개발 기간
- 2022.06.02 ~ 2022.06.13

> 프로젝트 형태
- 팀 프로젝트(4인)

> 프로젝트 설명
- Petrasche는 인스타그램을 모티브로 사진을 통해 ***반려동물의 일상을 공유, 자랑, 소통*** 하는 커뮤니티 서비스입니다.
기본 서비스 이외에도 ***반려동물 월드컵*** 을 통한 셀럽 반려동물 만들기와 나의 반려동물과 함께할 ***동네 산책친구 찾기***  등 다양한 서비스로 이용자에게 즐거움을 주고자 노력합니다.

<br>

# 2. 사용 기술
> Back-end
- Python 3  
- Django 4.0.5  
- FastAPI
- PostgresSQL

> Front-end
- Javascript
- HTML
- CSS

> Server
- AWS EC2
- AWS S3
- AWS RDS
- Docker

<br>

# 3. 기획 및 설계
> ### ERD 설계
>

> ### Mock-up
> <img width="916" alt="스크린샷 2022-07-11 오후 10 33 53" src="https://user-images.githubusercontent.com/100769423/187410368-85907cb4-cade-4119-abc9-9a06601099e7.png">

<br>

# 4. 핵심 기능
### 🍷 와인 추천 기능

<details>
  <summary>기능 설명 펼치기</summary>
  <br>

## 4.1. 기능 타입
> ### 무작위 와인 추천  
메인페이지 진입 시 데이터셋에 존재하는 4개의 와인을 무작위로 추천합니다.

> ### 유사 와인 추천  
특정 와인의 상세페이지 하단부에 해당 와인의 정보와 유사한 4개의 와인을 추천합니다.
  
  <br>
  
## 4.2 기능 흐름
  
  <br>
  
> ### 📌 Step 1. 추천 와인 선별  

- #### 무작위 선별(링크) 
- 메인페이지 진입 시 무작위로 4개의 와인을 선별합니다.
  
- #### 유사도 체크(링크) 
- 상세페이지 진입 시 특정된 와인과 유사한 4개의 와인을 선별합니다.
- 선별 방법은 준비된 유사도 측정 모델(.csv)을 이용해 유사도가 높은 순으로 선별합니다.
  
  <br>
  
> ### 📌 Step 2. 이미지 크롤링
- 선별된 와인의 이미지 주소를 크롤링합니다.
- 크롤링한 이미지 주소를 선별된 와인 데이터에 추가합니다. 
  
  <br>
  
> ### 📌 Step 3. 데이터 응답 
- 준비가 완료된 와인 데이터로 클라이언트에 응답합니다.

  <br>
</details>


### ✔ 그 외 기능

> 커뮤니티  

📌 게시물 / 댓글 CRUD  
  - 인기 게시물 메인화면 상단 노출  
  
📌 좋아요 / 팔로우  

📌 게시물 검색(Elastic Search)  

📌 개인 / 반려동물 프로필 CRUD  

📌 반려동물 월드컵  

📌 회원가입 / 로그인 (카카오 소셜 가능)  

<br>

> 산책친구 찾기  

📌 사용자 위치 등록(카카오 API)  

📌 모집 게시물 CRUD  

📌 게시물 필터 설정(날짜, 지역, 성별, 시간대 등)  

📌 실시간 채팅(Websocket & Django Channels)  

<br>

# 5. 트러블 슈팅
## 5.1 주어진 데이터에 이미지 파일 혹은 주소가 없어 웹페이지에서 와인 이미지를 보여줄 수 없는 상황
- 와인별 이미지를 별도로 크롤링하기 위해, 셀레니움 크롤링이라는 대안을 찾았지만 기술의 학습/진행시간 대비 프로젝트 마감기한을 고려해 추후 과제로 미루었습니다.
- 임시 대안으로, 이미지 데이터를 미리 가지고 있는 방식이 아닌 필요한 와인의 이미지 주소만 크롤링하는 실시간 크롤링 방식을 선택했습니다.
- 와인 이미지가 필요한 페이지에 진입 시, 실제 서비스 중인 와인 판매사이트에서 와인 이름으로 이미지 주소를 크롤링합니다.

