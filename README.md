# wanted-pre-onboarding-backend

#지원자 : 안성균<br>
<br>
#애플리케이션 실행 방법<br>
anaconda 설치(https://repo.anaconda.com/archive/Anaconda3-2023.07-1-Windows-x86_64.exe)<br>
환경 변수 path에 C:\anaconda3\Scripts 추가 (anaconda 설치한 위치의 Scripts)<br>
conda create --name project python=3.10<br>
conda activate project<br>
pip install django<br> 
conda install -c anaconda mysqlclient<br> 
cd wanted-pre-onboarding-backend<br>
cd backend<br>
python manage.py runserver<br>
<br>
회원가입 : http://127.0.0.1:8000/join/<br>
로그인 : http://127.0.0.1:8000/login/<br>
게시글 목록 : http://127.0.0.1:8000/post/<br>
새로운 게시글 생성 : http://127.0.0.1:8000/post/posting<br>
특정 게시글 조회 : http://127.0.0.1:8000/post/(게시글 id)<br> 
(ex) http://127.0.0.1:8000/post/4<br>
특정 게시글 수정 : http://127.0.0.1:8000/post/edit/(게시글 id)<br>
(url로 게시글 수정 페이지로 이동하더라도 작성자가 아니라면 메인 페이지로 강제 이동, 작성자만 활성화되는 게시물 수정 버튼으로 수정 가능)<br>
특정 게시글 삭제 : http://127.0.0.1:8000/post/delete/(게시글 id)<br>
(주소 입력으로 삭제 불가, 작성자만 활성화 되는 게시물 삭제 버튼으로 삭제)<br>
<br>
#데이터베이스 테이블 구조<br>
<br>
User<br>
![user](https://github.com/awds1236/wanted-pre-onboarding-backend/assets/102665306/9914b8c6-6046-4eba-a65d-f0d141dde9ea)
<br>
Post<br>
![post](https://github.com/awds1236/wanted-pre-onboarding-backend/assets/102665306/31277cb7-ae13-470a-8a8f-93dab8dbf95c)
<br>
	
