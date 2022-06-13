# 프로젝트 :  Airbnb clone 
<!-- <img src="https://img.shields.io/badge/Airbnb-FF5A5F?style=flat-square&logo=Airbnb&logoColor=white"/> -->

## :clipboard: 개발환경
* PyCharm
* Django
* Jenkins
* GitHub

## :clipboard: 사용 기술
### 백엔드
#### 
* <img src="https://img.shields.io/badge/Django-00C853?style=flat-square&logo=Django&logoColor=white"/>
* <img src="https://img.shields.io/badge/Python-673AB7?style=flat-square&logo=Python&logoColor=white"/>


#### DB
* <img src="https://img.shields.io/badge/MySQL-29B6F6?style=flat-square&logo=Mysql&logoColor=white"/>

#### AWS
* <img src="https://img.shields.io/badge/AWS-FFEE58?style=flat-square&logo=Amazon AWS&logoColor=white"/>
* <img src="https://img.shields.io/badge/s3-569A31?style=for-the-badge&logo=Amazon S3&logoColor=white">


### 프론트엔드
* <img alt="Html" src ="https://img.shields.io/badge/HTML-E34F26.svg?&style=for-the-badge&logo=HTML5&logoColor=white"/>
* <img alt="Css" src ="https://img.shields.io/badge/CSS-1572B6.svg?&style=for-the-badge&logo=CSS3&logoColor=white"/> 





## 🕹기능
* 회원관련 : 회원가입/로그인/회원탈퇴/회원정보수정/비밀번호변경

* 호스트모드 : 숙소 등록 / 현재 게스트 상황 / 메세지
 

* 게스트: 숙소 검색 / 숙소 예약 / 결제 / 메세지

## :link: API 설계도
|page|request|feature|api|event|설&nbsp;명|담&nbsp;당|비&nbsp;고|&nbsp;구현여부&nbsp;|
|------|-----|-----|-----|-----|-----|-----|-----|-----|
|헤더|GET|검색|/room|click / enter||규호||  ○
||GET|마이페이지|/mypage|click|마이페이지 버튼 클릭시 마이페이지로 이동|규호|| ○
||GET|호스트페이지|/hostpage|click|호스트모드 버튼 클릭시 호스트 모드 페이지로 이동|규호||○ 
|||||||||
|메인페이지|GET|현재숙소목록|/|default|메인페이지에 유형에 따라 이미지 요청|규호|| ○
||
||GET|캘린더로 숙소  |/날짜들|click|모든 숙소중 원하는 날짜에 예약가능한 숙소 검색|규호||○
|||||||||
|호스트모드|GET|숙소등록|/register|Click|숙소등록 페이지로 이동|재중|| ○
||PUT|숙소 정보 수정|/register/modify|Click|숙소 정보 수정|재중|| ○
|||||||||
|숙소등록페이지|POST|숙소유형선택|/register|click|숙소 유형 몇 가지 중 선택|재중|| ○
||POST|숙소위치|/register|Click|숙소 위치 지도 api를 사용하여 선택|재중|| △
||POST|숙소인원수|/register|Click|숙소 인원수 입력|재중|| △
||POST|숙소 사진|/register|Click|숙소 사진 등록|재중|| ○
||POST|숙소 옵션|/register|Click|숙소 옵션 선택하기|재중|| ○
||POST|숙소 기간|/register|Click|숙소 사용 가능 기간 선택하기|재중||○
||POST|숙소 가격|/register|Click|숙소 가격 입력|재중|| ○
|||||||||
|로그인및 회원가입|GET|로그인페이지|accounts/login|Click|로그인 페이지로 접속|규호|| ●
||POST|로그인|accounts/login|Click|로그인시 아이디 비밀번호 받는다|규호|| ●
||GET|회원가입페이지|accounts/signup|Click|회원가입 페이지로 이동|규호|| ●
||POST|회원가입|accounts/signup|Click|아이디,비밀번호,닉네임 외에 회원가입에 필요한 정보를 받는다|규호||●
||GET|이메일 유효성검사|accounts/singup|Click|가입된 이메일로 메일을 보내고 이를 확인해야 회원가입가능|규호|| ●
||GET|이메일로그인|accounts/login|Click|이메일로 로그인|규호|| △
||GET|구글 로그인|accounts/login|Click|구글 아이디로 로그인|규호|| △
||GET|카카오 로그인|accounts/login|Click|카카오로 로그인|규호|| △
|||||||||
|회원정보수정|GET|회원정보 수정 페이지|users/<int:pk>/|Click|회원정보 수정페이지로 접속|규호|| ○
||POST|회원정보수정|users/<int:pk>/modify|Click|아이디 비밀번호를 제외한 회원가입에 입력한 정보를 수정한다.|규호|| ○
||POST|비밀번호변경|users/change_password|Click|비밀번호를 변경한다.|규호|| ○
||DELETE|회원탈퇴|users/user_delete|Click|회원정보를 삭제한다|규호|| ○
|||||||||
||
|숙소검색리스트|GET|숙소간략정보|/room|Default|검색한 애용에 따라 숙소정보 요청|규호|| △
||
|||||||||
|숙소예약|GET|예약할 숙소정보|/room/reservation|Default|숙소정보들(이름, 사진, 옵션, 가격, 기간등을 요청)|재중|| △
||GET|리뷰리스트|/room/reservation|Default|리뷰리스트 나열|재중|| ●
||POST|리뷰 등록|/room/reservation/review|Click|리뷰를 등록|재중|| ●
||PUT|리뷰 수정|/room/reservation/review|Click|리뷰를 수정|재중|| △
||DELETE|리뷰삭제|/room/reservation/review|Click|리뷰를 삭제|재중|| ○
|||||||||
|숙소결제시스템|GET|숙소 결제|/room/pay|Click|결제토큰 받아오기|규호||●
||POST|숙소 결제|/room/pay|Click|결제 정보등을 입렵이 전송되면 예약번호도 같이 받는다|규호||●
||GET|숙소 결제 확인|/room/paycheck|Click|결제완료된 정보를 확인|규호||●
|||||||||


## :link: ERD 설계

<img width="70%" src="https://user-images.githubusercontent.com/67016829/173347836-54aa64df-965b-4c1e-ad1a-69049a67e272.png"/>




## ✏참고
* Airbnb
<!-- * https://github.com/farukipekcom/airbnb-clone -->


