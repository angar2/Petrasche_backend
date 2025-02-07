# 🐕 Petrasche

# 1. 프로젝트 정보

> 프로젝트 소개
- Petrasche는 인스타그램을 모티브로 사진을 통해 ***반려동물의 일상을 공유, 자랑, 소통*** 하는 커뮤니티 서비스입니다.
기본 서비스 이외에도 ***반려동물 월드컵*** 을 통한 셀럽 반려동물 만들기와 나의 반려동물과 함께할 ***동네 산책친구 찾기***  등 다양한 서비스로 이용자에게 즐거움을 주고자 노력합니다.

> 연관 Github
- [Front-end](https://github.com/angar2/Petrasche_frontend)
- [AI (classification)](https://github.com/angar2/Petrasche_AI)

> 개발 기간
- 2022.07.07 ~ 2022.08.15

> 프로젝트 형태
- 팀 프로젝트(4인)

<br>

# 2. 사용 기술
> ### Back-end
- Python 3  
- Django 4.0.5  
- FastAPI
- PostgresSQL

> ### Front-end
- Javascript
- HTML
- CSS

> ### Server
- AWS EC2
- AWS S3
- AWS RDS
- Docker

<br>

# 3. 기획 및 설계
> ### ERD 설계

> ### Mock-up
<img width="916" alt="스크린샷 2022-07-11 오후 10 33 53" src="https://user-images.githubusercontent.com/100769423/187410368-85907cb4-cade-4119-abc9-9a06601099e7.png">

> ### 배포
![img_1.png](/static/img_1.png)

<br>

# 4. 핵심 기능

> ### 커뮤니티  

📌 게시물 / 댓글 CRUD  
  - 인기 게시물 메인화면 상단 노출  
  
📌 좋아요 / 팔로우  

📌 게시물 검색(Elastic Search)  

📌 개인 / 반려동물 프로필 CRUD  

📌 반려동물 월드컵  

📌 회원가입 / 로그인 (카카오 소셜 가능)  

<br>

> ### 산책친구 찾기  

📌 사용자 위치 등록(카카오 API)  

📌 모집 게시물 CRUD  

📌 게시물 필터 설정(날짜, 지역, 성별, 시간대 등)  

📌 실시간 채팅(Websocket & Django Channels)  

<br>
