# selen.py 파일 사용법

## 1. 필요 설치 요소
 - 크롬드라이버
 - Selenium 패키지
 - dotenv 패키지


## 2. 크롬드라이버


### 2.1 크롬드라이버 버전 확인
 - 크롬 창 오픈, 좌상단 점 3개 클릭
 - 도움말
 - Chrome 정보 클릭
 - Chrome 정보란에서 버전 확인(ex 115.0.5790.171, 버전이 달라도 전혀 문제 없음)


### 2.2 크롬드라이버 다운로드
 - https://chromedriver.chromium.org/downloads
 - 해당 사이트에서 가능한 가까운 버전 기기 사양(Win, Linux, Mac M1 etc)에 맞게 다운로드
 - 만약, 크롬드라이버 버전이 115이거나 그 이상의 숫자로 시작한다면 https://googlechromelabs.github.io/chrome-for-testing/ 해당 주소에서 다운로드


### 2.3 크롬드라이버 셋팅
 - 압축파일을 풀면 chromedriver.exe 파일이 있습니다.
 - 다운로드 후 경로를 별도로 지정할 수도 있지만, selen.py, swea.sh 파일과 같은 곳에 두면 경로 설정 없이 바로 실행 가능합니다.


### 3.1 셀레니움 패키지
 - 'Selenium'은 웹 크롤링, 사이트 자동화 등에 사용되는 모듈
 - cmd를 열어서, pip install selenium으로 설치가 가능합니다
 - 설치시 시간이 다소 소요될 수 있습니다.
 - 배포 당시 버전 4.11.2


### 4.1 dotenv 패키지
 - cmd 창에서 pip install python-dotenv 명령어를 통해 설치
 - 함께 첨부된 .env 파일 내의 ID와 pw 값에 개인 ID와 pw 입력
 - 배포 당시 버전 1.0.0


### 5.1 Selen.py 파일 설정
 - 창이 다 켜지면 '프로그램이 완료되었습니다. 엔터키를 눌러 ~~ 하는 문장이 나오는데, 제가 창이 자동으로 종료되는 걸 막기 위해 인풋을 넣어 추가한 구문입니다. 
 ```python
 input("프로그램이 완료되었습니다. 용무가 끝나면 엔터키를 눌러 종료해주세요:") 
 ```
 해당 gitbash나 cmd 창에서 input을 만족하면 창이 종료됩니다. 직접 크롬 창을 끄셔도 문제없습니다.