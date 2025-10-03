from django.test import Client, TestCase
from bs4 import BeautifulSoup
from .models import Post, Category
from django.contrib.auth.models import User

# Create your tests here.
class TestView(TestCase): 
    def setUp(self):
        self.client = Client()
        self.user_eddi = User.objects.create_user(username='eddi',password='somepassword')
        self.user_tangball = User.objects.create_user(username='tangball',password='somepassword')
        self.category_programming = Category.objects.create(name='programming', slug='programming')
        self.category_music = Category.objects.create(name='music', slug='music')
    
        self.post_001 = Post.objects.create(
            title='첫 번째 포스트입니다.',
            content='Hello World. We are the world.',
            author=self.user_tangball,
            category=self.category_music,
        )
        self.post_002 = Post.objects.create(
            title='두 번째 포스트입니다.',
            content='함께 테스트 페이지를 만들어 보아요..',
            author=self.user_eddi,
            category=self.category_programming,
        )
        self.post_003 = Post.objects.create(
            title='세 번째 포스트입니다.',
            content='이번 포스트는 카테고리가 없어요.',
            author=self.user_eddi,
        )

    def category_widget_test(self, soup):
        categories_widget = soup.find('div', id='categories-widget')
        self.assertIn('Categories', categories_widget.text)
        self.assertIn(f'{self.category_programming.name} ({self.category_programming.post_set.count()})', categories_widget.text)
        self.assertIn(f'{self.category_music.name} ({self.category_music.post_set.count()})', categories_widget.text)
        self.assertIn('미분류 (1)', categories_widget.text)

    def test_post_list(self): #index_template 화면인 localhost/blog 페이지의 테스트 코드

        # 포스트는 3개 있다.
        self.assertEqual(Post.objects.count(),3)

        # 포스트 목록 페이지를 가져온다.
        response = self.client.get('/blog/')
        # 정상적으로 페이지가 로드된다.
        self.assertEqual(response.status_code, 200)
        # 페이지 타이틀은 'Blog Home'이다.
        soup = BeautifulSoup(response.content, 'html.parser')

        self.assertEqual(soup.title.text, 'Blog Home')

        #navbar는 navbar_test로 이관
        self.navbar_test(soup)
        #category는 category_widget_test로 이관
        self.category_widget_test(soup)

        # 메인 영역에 '아직 작성된 포스트가 없습니다.'라는 문구는 보이지 않는다.
        main_area = soup.find('div',id='main-area')
        self.assertNotIn('아직 작성된 포스트가 없습니다.', main_area.text)

        #각 포스트 카드 점검 -1
        post_001_card = main_area.find('div', id='post-1')
        self.assertIn(self.post_001.title, post_001_card.text)
        self.assertIn(self.post_001.category.name, post_001_card.text)

        #각 포스트 카드 점검 -2
        post_002_card = main_area.find('div', id='post-2')
        self.assertIn(self.post_002.title, post_002_card.text)
        self.assertIn(self.post_002.category.name, post_002_card.text)

        #각 포스트 카드 점검 -3
        post_003_card = main_area.find('div', id='post-3')
        self.assertIn(self.post_003.title, post_003_card.text)
        self.assertIn('미분류', post_003_card.text)

        #각 작성자 이름 확인
        self.assertIn(self.user_tangball.username.upper(), main_area.text)
        self.assertIn(self.user_eddi.username.upper(), main_area.text)

        # 포스트 모두 삭제
        Post.objects.all().delete()
        # 메인 영역에 게시물이 하나도 없는가?
        self.assertEqual(Post.objects.count(),0)
        # 포스트 목록 페이지를 새로고침 했을 때
        response = self.client.get('/blog/')
        # soup 내용 리셋
        soup = BeautifulSoup(response.content, 'html.parser')
        # '아직 작성된 포스트가 없습니다.'라는 문구가 보인다.
        main_area = soup.find('div',id='main-area')
        self.assertIn('아직 작성된 포스트가 없습니다.', main_area.text)


    def test_post_detail(self):


        # 포스트 생성을 생략하고 setup의 포스트를 이용

        # 1.2 그 포스트의 url은 '/blog/1/'이다(생성한 포스트의 url 확인.)
        self.assertEqual(self.post_001.get_absolute_url(),'/blog/1/')

        # 2. 첫 번째 포스트의 상세 페이지 테스트
        # 2.1 첫 번째 포스트의 url로 접근하면 정상 작동함.
        response = self.client.get(self.post_001.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        # 2.2 포스트 목록 페이지와 같은 네비게이션 바 존재.
        self.navbar_test(soup)
        #category는 category_widget_test로 이관
        self.category_widget_test(soup)
        # 2.3 첫 번째 포스트의 제목이 탭 타이틀에 존재.
        self.assertIn(self.post_001.title, soup.title.text)
        # 2.4 첫 번째 포스트의 제목이 포스트 영역에 있다.
        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('article', id='post-area')
        comment_area = main_area.find('section', id='comment-area')
        self.assertIn(self.post_001.title, post_area.text)
        # 2.5 첫 번째 포스트의 작성자가 포스트 영역에 있다.
        self.assertIn(self.user_tangball.username.upper(), post_area.text)
        # 2.6 첫 번째 포스트의 내용이 포스트 영역에 있다.
        self.assertIn(self.post_001.content, post_area.text)
        # 첫 번째 포스트의 카테고리 = music이 포스트 영역에 있다.
        self.assertIn(self.category_music.name, post_area.text)

    def navbar_test(self, soup):
        # 1.1 내비게이션 바가 있다.
        navbar = soup.nav
        # 1.2 Landing, About Me, Blog 라는 문구가 내비게이션 바에 있다.
        self.assertIn('Blog', navbar.text)
        self.assertIn('AboutMe', navbar.text)
        self.assertIn('Landing', navbar.text)
        # 1.3 navbar의 버튼들이 정상적으로 링크를 연결하는가?
        logo_btn = navbar.find('a', text='BLOG with Django')
        self.assertEqual(logo_btn.attrs['href'], '/')
        blog_btn = navbar.find('a', text='Blog')
        self.assertEqual(blog_btn.attrs['href'], '/blog/')
        about_me_btn = navbar.find('a', text='AboutMe')
        self.assertEqual(about_me_btn.attrs['href'], '/about_me/')
        landing_btn = navbar.find('a', text='Landing')
        self.assertEqual(landing_btn.attrs['href'], '/')
    

