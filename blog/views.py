from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'

    
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render( #render 함수는 두 번째 변수의 페이지를 보여주고, 세 번째 변수의 내용을 페이지로 전한다.
        request,
        'blog/index.html',
        {
            'posts' : posts,
        }#딕셔너리 형태로 세 번째 변수 'posts'를 지정.
    ) # index(요청)을 실행하면, '요청'의 내용을 반영해 blog/index.html 페이지를 화면에 출력(렌더링?)한다.

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        'blog/single_post_page.html',
        {
            'post' : post,
        }
    )