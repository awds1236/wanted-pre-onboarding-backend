from django.contrib.auth import authenticate, login
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from .forms import LoginForm
from rest_framework_jwt.settings import api_settings

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)

                request.session['token'] = token  # 토큰을 세션에 저장
                return HttpResponseRedirect('/')
            else:
                form.add_error(None, "아이디 혹은 비밀번호가 틀립니다.")
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})

def show_token(request):
    token = request.session.get('token')  # 세션에서 토큰 가져오기
    if token:
        html = f"<html><body>Your JWT token: {token}</body></html>"  # 토큰 출력 HTML
        return HttpResponse(html)
    else:
        return HttpResponse("No token found.")
