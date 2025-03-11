"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import Http404, HttpResponse
from django.shortcuts import render
from fake_db import user_db

# db 역할을 하는 변수 (가짜 데이터)
_db = user_db

# 메인 페이지
def index(request):
    return render(request, 'index.html')
    # 'index.html' 템플릿을 렌더링

# user_list
def user_list(request):
    # db에서 이름과 id를 가져옴
    names = [{'id': key, 'name': value['이름']} for key, value in _db.items()]
    return render(request, 'user_list.html', {'data': names})
    # 'user_list.html' 템플릿을 렌더링하고, 사용자 목록 데이터(names)를 'data'라는 이름으로 전달

# user_info (특정 사용자 정보)
def user_info(request, user_id):
    # user_id가 db에 없으면 404 오류 표시
    if user_id > len(_db):
        raise Http404('User not found')
    # 사용자 정보를 가져옴
    info = _db[user_id]
    return render(request, 'user_info.html', {'data': info})
    # 'user_info.html' 템플릿을 렌더링하고, 사용자 정보(info)를 'data'라는 이름으로 전달

# url 패턴 설정
urlpatterns = [
    path('admin/', admin.site.urls),  # 관리자 페이지
    path('', index, name='index'),  # 메인 페이지
    path('users/', user_list, name='user_list'),  # 사용자 목록 페이지
    path('users/<int:user_id>/', user_info, name='user_info'),  # 사용자 상세 정보 페이지
]