from django.urls import path
from . import views

urlpatterns = [
    #이제부터 blog 하위 페이지는 여기
    path('',views.PostList.as_view()),
    #path('', views.index),#이 경로(=blogs/'')로 들어가면 views.py에 작성한 index 함수를 실행한다.FBV 버전
    path('<int:pk>/', views.PostDetail.as_view()),
    # path('<int:pk>/',views.single_post_page), FBV 방식 때 쓰던 거. CBV 방식으로 변경했으니 불필요.
    path('category/<str:slug>/', views.category_page),
    path('tag/<str:slug>/', views.tag_page),
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view())
]
#현재 존재하는 페이지
#포스트 목록
#포스트 상세
#카테고리 검색
#태그 검색
#포스트 작성
#포스트 수정