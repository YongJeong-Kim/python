"""django_jwt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),

    # form 데이터로 username, password(superuser)를 POST로 전송
    path('api/token/', obtain_jwt_token),

    # 파라미터 JSON 형태로 { "token": "받은 토큰(헤더에 넣었던 앞에 jwt 빼고)" } 추가하여 POST로 호출
    # 정상이면 토근과 동일한 데이터 응답,
    # 유효하지 않다면 { "non_field_errors": ["Error decoding signature."] } 응답.
    path('api/token/verify/', verify_jwt_token),

    # api/token에서 받은 토큰을 Header: Authorization, value: jwt 받은 jwt 형태로 추가 후 POST 호출
    # 정상이면 새로운 토큰 응답.
    # 유효하지 않다면 { "non_field_errors": ["Signature has expired."] } 응답.
    path('api/token/refresh/', refresh_jwt_token),

    # api/token에서 받은 토큰을 Header: Authorization, value: jwt 받은 jwt 형태로 추가 후 POST 호출
    path('api/myapp/', include('myapp.urls'))
]
