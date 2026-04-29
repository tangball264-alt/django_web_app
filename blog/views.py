from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Category, Tag, Comment
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify
from .forms import CommentForm
from django.shortcuts import get_object_or_404

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
        context['comment_form'] = CommentForm
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
            response = super(PostCreate, self).form_valid(form)

            tags_str = self.request.POST.get('tags_str')
            if tags_str:
                tags_str = tags_str.strip()#문자열의 공백 등을 제거하여 반환

                tags_str = tags_str.replace(',',';') #쉼표를 세미콜론으로 변환한 문자열을 반환. 
                tags_list = tags_str.split(';')#지정 문자를 기준으로 그 전후를 분할해 반환. 지정 문자는 버린다.

                for t in tags_list:
                    t = t.strip()
                    tag, is_tag_created = Tag.objects.get_or_create(name=t) #태그(t)를 tag 변수에. 또한 기존Tag.objects에 없어 create해야 한다면 is_tag_created=True
                    if is_tag_created:
                        tag.slug = slugify(t, allow_unicode=True)
                        tag.save() #기존에 없다면 slug를 만들고 저장.
                    self.object.tags.add(tag)#이 포스트에 태그 추가.

            return response
        else : 
            return redirect('/blog/')

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'attachment', 'category']

    template_name = 'blog/post_update_form.html'

    def get_context_data(self, **kwargs):
        context =  super(PostUpdate, self).get_context_data()
        if self.object.tags.exists(): #이 포스트에 태그가 존재한다면
            tags_str_list = list() #우선 빈 리스트를 만들고
            for t in self.object.tags.all(): #그 리스트에 이 포스트의 모든 태그를 넣는다.
                tags_str_list.append(t.name)
            context['tags_str_default'] = '; '.join(tags_str_list) #리스트의 내용들을 '; '을 끼고 이어붙인다. 이걸 반환할 정보에 포함.

        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            #요청자가 인증(로그인)됨+요청자가 지금 오브젝트(포스트)의 작성자와 동일인이면
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
            #포스트업데이트 가능.
        else:
            raise PermissionDenied #아니면 '권한이 없음' 판정 = 403 오류 메시지.
        
    def form_valid(self, form):
        #권한 확인은 dispatch에서 맡는다. author는 이미 채워졌다.
        response = super(PostUpdate, self).form_valid(form)
        self.object.tags.clear() #기존 tag를 모두 지우고 새로이 쓴다.
    
        tags_str = self.request.POST.get('tags_str')
        if tags_str:
            tags_str = tags_str.strip()

            tags_str = tags_str.replace(',',';') 
            tags_list = tags_str.split(';')

            for t in tags_list:
                t = t.strip()
                tag, is_tag_created = Tag.objects.get_or_create(name=t)
                if is_tag_created:
                    tag.slug = slugify(t, allow_unicode=True)
                    tag.save()
                self.object.tags.add(tag)

        return response

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model=Comment
    form_class=CommentForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user==self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
            # 위에서 super().으로 작성할 수도 있으나, 이 코드는 교재에 따라 명시적으로 표기하는 구버전을 사용
        else : 
            raise PermissionDenied


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

def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk) #댓글을 달 포스트를 가져온다. 해당 pk가 없으면 404를 띄운다.
        
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment=comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else : 
                return redirect(post.get_absolute_url())
    else : raise PermissionDenied

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url())
    else :
        raise PermissionDenied