from django.urls import path
from . import views

urlpatterns = [
    #이제부터 blog 하위 페이지는 여기
    path('', views.index),#이 경로(=blogs/'')로 들어가면 views.py에 작성한 index 함수를 실행한다.
]