# wanted-pre-onboarding-backend

지원자 : 안성균<br>

애플리케이션 실행 방법
anaconda 설치(https://repo.anaconda.com/archive/Anaconda3-2023.07-1-Windows-x86_64.exe)
환경 변수 path에 C:\anaconda3\Scripts 추가 (anaconda 설치한 위치의 Scripts)
conda create --name project python=3.10 
conda activate project
pip install django 
conda install -c anaconda mysqlclient 
cd wanted-pre-onboarding-backend
cd backend
python manage.py runserver

회원가입 : http://127.0.0.1:8000/join/
로그인 : http://127.0.0.1:8000/login/
게시글 목록 : http://127.0.0.1:8000/post/
새로운 게시글 생성 : http://127.0.0.1:8000/post/posting
특정 게시글 조회 : http://127.0.0.1:8000/post/(게시글 id) 
(ex) http://127.0.0.1:8000/post/4
특정 게시글 수정 : http://127.0.0.1:8000/post/edit/(게시글 id)
(url로 게시글 수정 페이지로 이동하더라도 작성자가 아니라면 메인 페이지로 강제 이동, 작성자만 활성화되는 게시물 수정 버튼으로 수정 가능)
특정 게시글 삭제 : http://127.0.0.1:8000/post/delete/(게시글 id)
(주소 입력으로 삭제 불가, 작성자만 활성화 되는 게시물 삭제 버튼으로 삭제)

데이터베이스 테이블 구조

User
![user](https://github.com/awds1236/wanted-pre-onboarding-backend/assets/102665306/9914b8c6-6046-4eba-a65d-f0d141dde9ea)

Post
![post](https://github.com/awds1236/wanted-pre-onboarding-backend/assets/102665306/31277cb7-ae13-470a-8a8f-93dab8dbf95c)

	