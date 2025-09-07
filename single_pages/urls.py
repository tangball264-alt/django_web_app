from django.urls import path
from . import views

urlpatterns = [
    #이제부터 blog 하위 페이지는 여기
    path('about_me/', views.about_me),
    path('',views.landing),
]