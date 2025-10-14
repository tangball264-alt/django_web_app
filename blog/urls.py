from django.urls import path
from . import views

urlpatterns = [
    #이제부터 blog 하위 페이지는 여기
    path('',views.PostList.as_view()),
    #path('', views.index),#이 경로(=blogs/'')로 들어가면 views.py에 작성한 index 함수를 실행한다.FBV 버전
    path('<int:pk>/', views.PostDetail.as_view()),
    # path('<int:pk>/',views.single_post_page), FBV 방식 때 쓰던 거. CBV 방식으로 변경했으니 불필요.
    path('category/<str:slug>/', views.category_page),
    path('tag/<str:slug>/', views.tag_page)
]