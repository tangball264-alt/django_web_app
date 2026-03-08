from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Category, Tag
from django.core.exceptions import PermissionDenied

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context
    
class PostCreate(LoginRequiredMixin, UserPassesTestMixin ,CreateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'attachment', 'category']

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (self.request.user.is_staff or self.request.user.is_superuser): #이 유저가 인증되었으며, 스태프거나 수퍼유저일 것.
            form.instance.author = current_user
            return super().form_valid(form)
        else : 
            return redirect('/blog/')

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'attachment', 'category', 'tags']

    template_name = 'blog/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            #요청자가 인증(로그인)됨+요청자가 지금 오브젝트(포스트)의 작성자와 동일인이면
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
            #포스트업데이트 가능.
        else:
            raise PermissionDenied #아니면 '권한이 없음' 판정 = 403 오류 메시지.
        


def category_page(request, slug): #위의 둘과 달리 FBV 방식. 필수인 request와 추가적으로 slug를 매개변수로 받는다.
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else :
        category = Category.objects.get(slug=slug)
        post_list =  Post.objects.filter(category=category)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count,
            'category': category,
        }
    )

def tag_page(request, slug): #FBV 방식. 필수인 request와 추가적으로 slug를 매개변수로 받는다.
    
    tag = Tag.objects.get(slug=slug)
    post_list =  tag.post_set.all()

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'tag' : tag,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count,
        }
    )