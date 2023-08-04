# wanted-pre-onboarding-backend

## 지원자 : 안성균<br>

## 애플리케이션 실행 방법<br>
* anaconda 설치(https://repo.anaconda.com/archive/Anaconda3-2023.07-1-Windows-x86_64.exe)<br>
* 환경 변수 path에 C:\anaconda3\Scripts 추가 (anaconda 설치한 위치의 Scripts)<br>

* conda create --name project python=3.10<br>
* conda activate project<br>
* pip install django<br> 
* conda install -c anaconda mysqlclient<br> 
* cd wanted-pre-onboarding-backend<br>
* pip install requirements.txt<br>
* cd backend<br>
* python manage.py runserver<br>
	(django 서버 시작)<br>
<hr>

* 회원가입 : http://127.0.0.1:8000/join/<br>
* 로그인 : http://127.0.0.1:8000/login/<br>
* 게시글 목록 : http://127.0.0.1:8000/post/<br>
* 새로운 게시글 생성 : http://127.0.0.1:8000/post/posting<br>
* 특정 게시글 조회 : http://127.0.0.1:8000/post/(게시글 id)<br> 
	(ex) http://127.0.0.1:8000/post/4<br>
* 특정 게시글 수정 : http://127.0.0.1:8000/post/edit/(게시글 id)<br>
	(url로 게시글 수정 페이지로 이동하더라도 작성자가 아니라면 메인 페이지로 강제 이동, 작성자만 활성화되는 게시물 수정 버튼으로 수정 가능)<br>
* 특정 게시글 삭제 : http://127.0.0.1:8000/post/delete/(게시글 id)<br>
	(주소 입력으로 삭제 불가, 작성자만 활성화 되는 게시물 삭제 버튼으로 삭제)<br>

## 데이터베이스 테이블 구조<br>

* User<br>
	![user](https://github.com/awds1236/wanted-pre-onboarding-backend/assets/102665306/9914b8c6-6046-4eba-a65d-f0d141dde9ea)

* Post<br>
	![post](https://github.com/awds1236/wanted-pre-onboarding-backend/assets/102665306/31277cb7-ae13-470a-8a8f-93dab8dbf95c)
<br>

## 구현한 API의 동작을 촬영한 데모 영상 링크<br>
https://youtu.be/U5Q4o9zu8UU<br>

## 구현 방법 및 이유에 대한 간략한 설명<br>
### 과제 1. 사용자 회원가입 엔드포인트<br>
* 이메일에 @이 포함되어 있지 않거나 비밀번호가 8자리 미만이면 경고창이 출력되며 회원가입이 불가능하게 구현<br>
* 비밀번호 암호화 - Django에서 User model 사용 후 PasswordField로 저장 시 SHA-256 알고리즘으로 자동 암호화되어 DB에 저장<br>

### 과제 2. 사용자 로그인 엔드포인트<br>
* 이메일에 @이 포함되어 있지 않거나 비밀번호가 8자리 미만이면 경고창이 출력되며 로그인이 불가능하게 구현<br>
* 아이디(이메일)와 비밀번호가 DB와 일치하지 않으면 로그인이 불가능하게 구현<br>
* 성공적으로 인증이 되면 메인 페이지로 이동, 동시에 콘솔창에 JWT 출력<br>

### 과제 3. 새로운 게시글을 생성하는 엔드포인트<br>
* 제목과 내용을 작성 후 등록하기 버튼을 누르면 DB에 저장
	
### 과제 4. 게시글 목록을 조회하는 엔드포인트<br>
* DB에 게시글 id를 바탕으로 작성일, 제목, 작성자 출력 구현<br>
	* 동일한 제목이 있어도 작성자와 작성시간으로 구분 가능 <br>
* Pagination 기능으로 게시글 10개, 25개, 50개, 100개 선택해서 조회가 가능하고 해당 개수 초과 시 다음 페이지가 생성되어 게시글 이동 구현<br>

### 과제 5. 특정 게시글을 조회하는 엔드포인트<br>
* DB에 저장된 post의 id에 따른 제목, 작성일, 작성자, 내용 출력 구현

### 과제 6. 특정 게시글을 수정하는 엔드포인트
* 특정 게시글 조회에 수정하기 버튼으로 수정이 가능하게 구현<br>
* 게시글의 id를 바탕으로 제목과 내용을 수정 가능<br>
* 게시글의 작성자만 수정이 가능하며 url로 강제로 이동하더라도 작성자가 아니라면 수정 페이지에 접속이 불가능하게 구현<br>

### 과제 7. 특정 게시글을 삭제하는 엔드포인트
* 특정 게시글 조회에 삭제하기 버튼으로 삭제가 가능하게 구현<br>
* 게시글의 작성자만 삭제가 가능하며 url로 강제로 이동하더라도 작성자가 아니라면 삭제가 불가능하게 구현<br>

## API 명세(request/response 포함)

### 회원가입

#### Endpoint
	/join/
#### Method
	POST
#### Request Body
	{
	    "username": "<사용자 아이디>",
	    "password": "<비밀번호>",
	    "password_check": "<비밀번호 확인>"
	}
#### Successful Response
	HTTP 302 Found
	Location: /login/
#### Failed Response
	HTTP 200 OK
	Content: 회원 가입 페이지 with form errors

### 로그인

#### Endpoint
	/login/
#### Method
	POST
#### Request Body
	{
	    "username": "<사용자 아이디>",
	    "password": "<비밀번호>"
	}
#### Successful Response
	HTTP 302 Found
	Location: /
#### Failed Response
	HTTP 200 OK
	Content: 로그인 페이지 with error message "아이디 혹은 비밀번호가 틀립니다."
 
### 게시글 조회

#### Endpoint
	/post/
#### Method
	GET

#### Successful Response
	HTTP 200 OK
	Content: 게시글 목록 페이지 (post/post.html) with a list of all posts

### 게시글 작성

#### Endpoint
	/post/posting/
#### Method
	POST
#### Request Body
	{
	    'post_title" : <게시글 제목>",
	    "post_content" : "<게시글 본문>",
	}	
#### Successful Response
	HTTP 302 Found
	Location: /post/

#### Failed Response
	HTTP 200 OK
	Content: 게시물 작성 페이지 with form errors

### 특정 게시글 조회

#### Endpoint
	/post/<int:pk>/
#### Method
	GET
	
#### Successful Response
	HTTP 200 OK
	Content: 게시글 상세 정보 페이지 (post/post_detail.html) with the post details

#### Failed Response
	HTTP 404 Not Found
	Content: 404 error page

### 게시글 수정

#### Endpoint
	 /post/edit/<int:post_id>/
#### Method
	POST

#### Authentication
	Required 
 
#### Request Body
	{
	    'post_title" : <게시글 제목>",
	    "post_content" : "<게시글 본문>",
	}	
#### Successful Response
	HTTP 303 See Other
	Location: /post/<int:pk>/
	Redirects to the post detail page of the updated post (for POST request)

#### Failed Response
	HTTP 404 Not Found
	Content: 404 error page
	Error occurs if the requested post ID does not exist.

### 게시글 삭제

#### Endpoint
	/post/delete/<int:post_id>/
#### Method
	POST

### Request Body
	None

#### Successful Response
	HTTP 200 OK
	Content:
 		{
		  "success": true
		}

#### Failed Response
	HTTP 500 Internal Server Error
	Content:
 		{
		  "success": false,
		  "error": "Post not found"
		}







 





 
