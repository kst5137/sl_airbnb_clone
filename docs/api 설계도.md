|page|request|feature|api|event|설명|담당|비고|구현여부|
|------|-----|-----|-----|-----|-----|-----|-----|-----|
|헤더|GET|검색|/room|click / enter|||||
||GET|마이페이지|/mypage|click|마이페이지 버튼 클릭시 마이페이지로 이동|||
||GET|호스트페이지|/hostpage|click|호스트모드 버튼 클릭시 호스트 모드 페이지로 이동|||
|||||||||
|메인페이지|GET|현재숙소목록|/|default|메인페이지에 유형에 따라 이미지 요청|||
||GET|랜덤한 숙소|/randomroom|click|모든 숙소중 랜덤하게 요청||필수는 아님|
|||||||||
|호스트모드|GET|현재 게스트 상황|/|Default|현재의 게스트 상황을 요청|||
||GET|메세지|/message|Default|메세지 이력 요청|||
||GET|숙소등록|/register|Click|숙소등록 페이지로 이동|||
||PUT|숙소 정보 수정|/register/modify|Click|숙소 정보 수정|||
|||||||||
|숙소등록페이지|POST|숙소유형선택|/register|click|숙소 유형 몇 가지 중 선택|재중||
||POST|숙소위치|/register|Click|숙소 위치 지도 api를 사용하여 선택|재중||
||POST|숙소인원수|/register|Click|숙소 인원수 입력|재중||
||POST|숙소 사진|/register|Click|숙소 사진 등록|재중||
||POST|숙소 옵션|/register|Click|숙소 옵션 선택하기|재중||
||POST|숙소 기간|/register|Click|숙소 사용 가능 기간 선택하기|재중||
||POST|숙소 가격|/register|Click|숙소 가격 입력|재중||
|||||||||
|로그인및 회원가입|GET|로그인페이지|/login|Click|로그인 페이지로 접속|규호||
||POST|로그인|/|Click|로그인시 아이디 비밀번호 받는다|규호||
||GET|회원가입페이지|/signup|Click|회원가입 페이지로 이동|규호||
||POST|회원가입|/signup|Click|아이디,비밀번호,닉네임 외에 회원가입에 필요한 정보를 받는다|규호||
||GET|전화번호 문자 전송|/login|Click|가입된 번호가 있는지 확인하고 있다면 인증번호를 받아서 로그인|규호|없어도 됨|
||GET|이메일로그인|/|Click|이메일로 로그인|규호||
||GET|구글 로그인|/|Click|구글 아이디로 로그인|규호||
||GET|카카오 로그인|/|Click|카카오로 로그인|규호||
|||||||||
|회원정보수정|GET|회원정보 수정 페이지|/updatemyinfo|Click|회원정보 수정페이지로 접속|||
||POST|회원정보 수정|/login|Click|수정할 아이디 비번 외에 회원정보 받는다|||
|||||||||
|숙소검색리스트|GET|요금과 유형외에 분류|/room|Click|숙소 분류에 따라 재정렬|||
||GET|숙소간략정보|/room|Default|검색한 애용에 따라 숙소정보 요청|||
||GET|페이지에 나온 숙소들 위치 지도에 출력|/room|Default|검색한 내용에 따라 숙소 정보 요청|||
|||||||||
|숙소예약|GET|예약할 숙소정보|/room/reservation|Default|숙소정보들(이름, 사진, 옵션, 가격, 기간등을 요청)|||
||GET|리뷰리스트|/room/reservation|Default|리뷰리스트 나열|||
||POST|리뷰 등록|/room/reservation/review|Click|리뷰를 등록|||
||PUT|리뷰 수정|/room/reservation/review|Click|리뷰를 수정|||
||DELETE|리뷰삭제|/room/reservation/review|Click|리뷰를 삭제|||
|||||||||
|숙소결제시스템|GET|숙소 결제|/room/pay|Click|결제토큰 받아오기|||
||POST|숙소 결제|/room/pay|Click|결제 정보등을 입렵이 전송되면 예약번호도 같이 받는다|||
||GET|숙소 결제 확인|/room/paycheck|Click|결제완료된 정보를 확인|||
|||||||||
