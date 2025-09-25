from django.test import Client, TestCase
from bs4 import BeautifulSoup
from .models import Post

# Create your tests here.
class TestView(TestCase): 
    def setUp(self):
        self.client = Client()

    def test_post_list(self): #index_template 화면인 localhost/blog 페이지의 테스트 코드
        # 1.1 포스트 목록 페이지를 가져온다.
        response = self.client.get('/blog/')
        # 1.2 정상적으로 페이지가 로드된다.
        self.assertEqual(response.status_code, 200)
        # 1.3 페이지 타이틀은 'Blog Home'이다.
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Blog Home')
        #navbar는 navbar_test로 이관
        self.navbar_test(soup)

        # 2.1 메인 영역에 게시물이 하나도 없다면
        self.assertEqual(Post.objects.count(),0)
        # 2.2 '아직 작성된 포스트가 없습니다.'라는 문구가 보인다.
        main_area = soup.find('div',id='main-area')
        self.assertIn('아직 작성된 포스트가 없습니다.', main_area.text)

        # 3.1 게시물이 2개 있다면
        post_001 = Post.objects.create(
            title='첫 번째 포스트입니다.',
            content='Hello World. We are the world.',
        )
        post_002 = Post.objects.create(
            title='두 번째 포스트입니다.',
            content='함께 테스트 페이지를 만들어 보아요..',
        )
        self.assertEqual(Post.objects.count(),2)
        # 3.2 포스트 목록 페이지를 새로고침 했을 때
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code, 200)
        # 3.3 메인 영역에 포스트 2개의 타이틀이 존재한다.
        main_area = soup.find('div',id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        # 3.4 '아직 작성된 포스트가 없습니다.'라는 문구는 보이지 않는다.
        self.assertNotIn('아직 작성된 포스트가 없습니다.', main_area.text)

    def test_post_detail(self):
        # 1.1 포스트가 하나 있다.(하나의 테스트용 포스트를 생성)
        post_001 = Post.objects.create(
            title = '첫 번째 포스트입니다.',
            content = '누구든지 체포 또는 구속을 당한 때에는 즉시 변호인의 조력을 받을 권리를 가진다. 다만, 형사피고인이 스스로 변호인을 구할 수 없을 때에는 법률이 정하는 바에 의하여 국가가 변호인을 붙인다. 대통령은 헌법과 법률이 정하는 바에 의하여 공무원을 임면한다. 국회의원은 법률이 정하는 직을 겸할 수 없다. 국회에서 의결된 법률안은 정부에 이송되어 15일 이내에 대통령이 공포한다. 선거와 국민투표의 공정한 관리 및 정당에 관한 사무를 처리하기 위하여 선거관리위원회를 둔다. 선거운동은 각급 선거관리위원회의 관리하에 법률이 정하는 범위안에서 하되, 균등한 기회가 보장되어야 한다.대통령의 선거에 관한 사항은 법률로 정한다. 일반사면을 명하려면 국회의 동의를 얻어야 한다. 헌법에 의하여 체결·공포된 조약과 일반적으로 승인된 국제법규는 국내법과 같은 효력을 가진다.'
        )
        # 1.2 그 포스트의 url은 '/blog/1/'이다(생성한 포스트의 url 확인.)
        self.assertAlmostEqual(post_001.get_absolute_url(),'/blog/1/')

        # 2. 첫 번째 포스트의 상세 페이지 테스트
        # 2.1 첫 번째 포스트의 url로 접근하면 정상 작동함.
        response = self.client.get(post_001.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        # 2.2 포스트 목록 페이지와 같은 네비게이션 바 존재.
        self.navbar_test(soup)
        # 2.3 첫 번째 포스트의 제목이 탭 타이틀에 존재.
        self.assertIn(post_001.title, soup.title.text)
        # 2.4 첫 번째 포스트의 제목이 포스트 영역에 있다.
        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('article', id='post-area')
        comment_area = main_area.find('section', id='comment-area')
        self.assertIn(post_001.title, post_area.text)
        # 2.5 첫 번째 포스트의 작성자가 포스트 영역에 있다(아직 x)
        # 첫 번째 포스트의 내용이 포스트 영역에 있다.
        self.assertIn(post_001.content, post_area.text)

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