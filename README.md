# django_web_app
Django 학습용 토이프로젝트 식당 평가 및 추천 웹페이지


1일차
github 레포지토리 만들고 clone (private이기 때문에 ssh 키 이용.) -> ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBTc68rGmhY4r7SEK2JxALn+A/GEPvSm1p0Ct3KM95V4 tangball264@gmail.com
가상환경(venv)생성 -> source venv/bin/activate 명령어로 가상환경 실행. deactivate로 종료. pip list로 현재 패키지 확인

2일차
가상환경에 django 설치(pip install django)
(venv) (base) godayeong@godayeong-ui-MacBookAir django_web_app % pip list
Package  Version
-------- -------
asgiref  3.9.1
Django   5.2.5
pip      25.0.1
sqlparse 0.5.3

장고 프로젝트 생성
(venv) (base) godayeong@godayeong-ui-MacBookAir django_web_app % django-admin st
artproject django_web_app .
(venv) (base) godayeong@godayeong-ui-MacBookAir django_web_app % ls
README.md       django_web_app  manage.py       venv

python manage.py runserver 로 정상 서버 실행 확인
python manage.py migrate db 생성. sqlite3 사용.
python manage.py createsuperuser 로 관리자계정 생성
(kdy, kdy@learndjango.com, mysuperuser)

(venv) (base) godayeong@godayeong-ui-MacBookAir django_web_app % git add . (터미널에 현재 서버 변경 기록 추가)
(venv) (base) godayeong@godayeong-ui-MacBookAir django_web_app % git commit -m "Django 프로젝트 생성" (커밋 메시지, 커밋)

3일차
앱(maps) 생성 -> map으로 할걸 그랬다. 저장(maps 앱 생성하기)


4일차
내용 드리프트해서 일단 책 내용 따라가보기로.
Q : 왜 새로운 앱을 만들면 프로젝트폴더/settings.py의 installed app에 등록해야 하는가?
blog의 model 작성 -> makemigrations -> migrate -> 그런데 이미 이전 app에서 migrate를 gitignore에 등록. 저장 상태 확인 필요.
admin.py에 post 모델 import
Q : admin.py를 작성할 때, admin.site.register(Post)는 무슨 의미지?
*오류로그 : /blog/admin.py 에 from models import Post 라고 작성 -> from .models import Post라고 작성해야.
    왜? : Django에서 앱 내부의 models.py를 불러올 때는 상대 경로(import) 대신 현재 앱 패키지를 기준으로 가져와야(gpt 왈)
        -> 즉, models는 독립된 모듈이 아니라 blog.models(축약 .models)라는 풀네임을 가져야 함.
admin에서 post를 볼 수 있음. 정상적으로 작성 가능.
post모델에 __str__ 함수 선언
Q : str 함수란 무엇이고 왜 이렇게(__str__) 작성하는가?
Q : 또한 str 함수에 포함된 self.pk는 무엇인가? 또한 왜 이런 양식으로 작성하는가?
프로젝트 파일 내 settings.py의 TIME_ZONE 항목 "Asia/Seoul" 로 수정.

5일차
*장고 셀 사용하기 (python manage.py shell) -> 파이썬 특유의 한줄씩 실행 가능. 끝내기(exit())
작성 시각과 수정 시각의 자동 저장
Q : models의 항목에 auto_now_add와 auto_now는 뭐가 다르지?
*오류로그 : 기존 models.py에서 changed_at 을 null 가능으로 해둠 -> 이번에 auto_now로 하면서 null 불가 -> 기존 post의 null을 어떻게 처리할지
    따라서 어떤 방식으로 수정할지 반문함. 
    ->나는 1번(하나의 디폴트 값으로 일단 전부 채운다)을 선택. 어떤 디폴트를 쓸지 반문하자 timezone.now(파이썬 언어로 답해야?)로 현재시간으로 지정. -> 장고 셸과 같은 부분?
실행후 확인하자 시간 입력칸이 사라짐.

6일차
실제 포스트 페이지 만들기 과정
일단 urls.py에 blog 계열 주소를 등록. 하위 페이지 주소를 위해 blog 앱에 urls.py 파일을 새로 만들어두기. 
이제 blog/urls.py를 채우는 일을 FBV로 할 것인가, CBV로 할 것인가?
일단 교재 내용 따라서 진행 예정
blog/urls.py에 기본(localhost/blog/)주소지 path 지정. views.index 메서드. 메서드에서 blog/templates/blog/index.html 렌더. html 파일 내용은 일단 그냥 '블로그 페이지입니다.' 향후 부트스트랩 활용해 디자인 챙겨야.
포스트 목록 출력은 views.py의 index 함수 수정. models.py 파일의 Post 모델을 import 하고,index 내에서 posts 변수에 Post.objects.all()쿼리로 데이터베이스의 레코드를 받아온다.
반환할 렌더 함수의 변수에 > 'posts':posts를 추가.
마지막으로 index.html에서 posts를 받아 출력하는 for문을 {% %}와 {{}}을 이용해 작성.
Q : 렌더 함수의 변수는 어떤 것이 들어갈 수 있고, 어떤 형식을 취하는가?
Q : html 안의 for문, 변수 등은 어째서 이런 형태를 취하는가? 이런 형태를 뭐라고 부르는가?
정상적으로 출력되는 것을 확인함. 세부 페이지 정보 출력 예정.
최신순 정렬을 위해 views에서 posts를 가져올 때 쿼리문에 order_by 를 이용하는 것이 171p에 있으나, 나의 경우 내용의 연속적인 이해를 위해 작성 순서로 정렬을 유지할 것. 따라서 해당 항목 생략.

7일차
개별 페이지 만듦. single_post_page를 urls, views, html 작성.
def single_post_page(request, pk): -> 여기에 pk를 함께 받아올 수 있구나. 앞에 urls에서 주소에서 <int:pk>를 받는데 이게 영향이 있으려나?
    post = Post.objects.get(pk=pk) -> all과 달리 get은 하나의 항목만 받아오는 쿼리.
posts페이지에 링크 만들기 -> <a href>로 p.get_absolute_url 을 지정 -> get absolute url? -> 그러나 연결 x. 실제 실행 시 <a href="">로 처리됨. -> 모델 수정 및 값 작성 필요.
get_absolute_url은 model에 def로 함수 작성. -> str처럼? -> view on site 기능 작성됨.
Q : history나 view on site는 기본 django에 있는 건가? 그러면 get absolute url 함수도 기본으로 있는거 쓰는건가?
A : 실제로 이미 존재하는 메서드가 맞으며, 메서드 오버라이딩을 위해 우리가 models에 작성하는 것.

8일차
single_pages 앱의 about_me 페이지와 landing 페이지 작성.
single_pages/urls.py 와 html 파일 작성.
models 안적어도 app 작성이 가능함. 

9일차
기존 페이지(FBV 방식)을 CBV 방식으로 전환
blog/views.py에 PostList 클래스 생성.(ListView 클래스 상속-사용.) 모델=포스트
urls.py에 index path대신  postlist 이용해서 path 지정 하도록 함.
*오류로그 : path는 끝에 쉼표 빼먹으면 서버 실행도 못함.
Q : blog/urls.py의 as_view()는 뭐지? 이 문법은 무슨 의미지?
view에서 postList에 템플릿 네임 지정.(혹은 post_list.html 파일을 만들어  사용.)
전자 이용했으므로 index.html 파일의 posts for문을 post_list(혹은 object_list)에 대한 for 문으로 변경
부트스트랩 blog 페이지 가져오기. 
*오류로그 : css 위치 틀렸는지, 부트스트랩 파일이 틀렸는지 정상 작동 안됨.

10일차
파일 구조 수정하자 정상적으로 css 적용이 됨.
파일 구조
DJANGO_WEB_APP
├── blog/                  # 앱
│   ├── templates/         # HTML 템플릿 폴더
│   │   └── blog/          # 앱 이름과 같은 하위 폴더 생성 권장
│   │       ├── index_template.html
│   │       └── single_post_page.html
│   │
│   ├── static/            # 정적 파일 (CSS, JS, 이미지)
│   │   └── blog/          # 앱 이름과 같은 하위 폴더 생성 권장
│   │       ├── css/
│   │       │   └── styles.css
│   │       ├── js/
│   │       │   └── scripts.js
│   │       └── bootstrap/
│   │           ├── bootstrap.min.css
│   │           └── bootstrap.min.js
│   │
│   ├── views.py
│   ├── ...
│   └── models.py
이하생략
이제 이 디자인을 내 웹에 맞추어 수정.
포스트 리스트-카드를 for 문으로 사용했더니, 한 줄에 두 개의 카드가 아닌, 한 줄에 하나의 카드만 나오는 문제. 
따라서 {% if forloop.first %}를 이용, 첫 번째 p만을 큰 카드로 하고, 이후 다른 p를 모두 {% else %}로 처리. 이후 {% endif %}로 마무리.
페이지 리스트 지워야 할까?
다른 페이지에도 모두 템플릿의 공통 요소 적용. -> 공통 요소란? : navbar
navbar 아래 조금 띄우도록 할 필요 있음.

11일차
포스트 상세 페이지 부트스트랩 템플릿 적용
원래 교재에서는 부트스트랩 4 써서 
<script src="https://code.iquery.com/jquery-3.5.1.slim.min.js" integr-ity"sha8d-ofidz7htPllsSSnCTpuj/zy4C=CGpamoFVySBHVBnE+IOoVYUJew +0rCXaRkfj"
crossorigin="anonymous"></script>
<script sre-"htps:/an.jsdelivr.mnet/npm/pocer.isg1.16.1/cist/umd/pooper.min.is" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7n iu7355k7lN"
crossorigin="anonymous"></script>
<script src-"https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap. min.js"
integrity="sha384-w104orYj80ndcko6inVbzY0tgp4pl6+1z71r36Ikzbvr/aHKhXdBN mNb5092v7s"
crossorigin="anonymous"></script>
을 각 html 파일 마지막에 작성하라고 하는데, 나는 5 써서 기존 것을 유지해도 괜찮다.
*단, GPT 추천 사항으로는 '무결성'검증을 위해 <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script> 코드를 <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4"
        crossorigin="anonymous"></script> 로 변경할 것 권고 + <script src="{% static 'blog/js/post_scripts.js' %}"></script> 로 static_url 로 불러오기.

무결성 검증은 나중에 보안 부분에 초점 두고 다시 훑을 거니 두고, js파일만 정리.
기존 파일에서는 텍스트를 한 줄 한줄 띄우는데, 나 역시 이렇게 해야 할까?
*오류로그 : 페이지 목록에서 큰 카드와 작은 카드를 병용하는 데 성공하고 해결된 줄 알았지만, 사실 포스트가 2개라서 몰랐는데, 세 번째 카드와 두 번째 카드가 같은 높이에 있어야 하는데 이게 줄 나눔 되었음.
-> if post_list 로 포스트 리스트에 내용이(하나의 포스트라도) 존재한다면 첫 번째 포스트를(post_list.0) 큰 카드에 형식에 맞게 출력
-> 그리고 for 문을 row 아래, col 위에 {% for p in post_list|slice:"1:" %} 로 작성해 두 번째 포스트부터 
1 2
3 4 형식으로 순서 배열되게 함.
추가적으로 내용이 길어지니 포스트의 세로 길이를 고정하고 나머지를 ....으로 줄여 생략하는 기능을 넣고 싶음.
우선 navbar fixed-top 부분을 지우라고 지시하는데, 애초에 nav를 통일하려고 덮어씌웠더니 지워짐. 탑 패딩도 생략함.
전체 텍스트를 <p>로 묶어 입력하니, 줄바꿈이 모두 생략됨. 해당 사항에 대하여 수정 필요.
현재 수정이 필요한 사항
1. 포스트 목록 화면에서 목록 카드의 길이를 고정하고, 긴 콘텐츠를 후략 하는 것.
2. 포스트 상세 페이지에서 콘텐츠 내용에 줄바꿈이 포함되어 단락이 구분되도록 하는 것.
3. 포스트에 이미지 추가.

다음 단계로 포스트 이미지 추가

12일차
이미지 파일 넣기
1. 이미지를 저장할 수 있게 만들고
2. admin의 post 작성에서 이미지를 넣을 수 있게 하고
3. 화면상에 맞게 출력하기
+그러면 모델도 수정해야 하겠네.

settings에 media url과 media root 지정. 특히 root는 os 라이브러리 이용하는데
Q : os 라이브러리는 뭐고 os.path.join(BASE_DIR, '_media')가 뜻하는 말은 뭐지?
그리고 모델 수정해서 헤드 이미지 항목을 추가. imagefield를 이용해 업로드 폴더와 공백 가능 설정을 추가해 저장.
모델 수정했으니 makemigrations하면 python -m pip install Pillow 커맨드로 pillow 라이브러리를 설치하라고 요청받음. 사유 : 파이썬은 이미지 처리에 이 라이브러리 사용.
이미지 업로드 후 확인. 이 프로젝트 폴더에는 이미지가 올라오고, 수정하며 필요 없어진 이미지도 저장되는데다가 중복 이미지도 이름이 바뀌어 저장됨. 하지만 아직 수정 안한 블로그 페이지 뿐만 아니라, 이미지를 업로드한 admin 페이지에서도 이미지를 확인하는 것은 오류 발생. -> urls.py에서 media url 설정 필요.
기존 url이 urlpatterns=[] 인데, 미디어 url은 기존 url에 이미지가 포함되면 /media/를 덧붙이는 거니까, urlpatterns += 로.
Q : from django.conf import settings와 from django.conf.urls.static import static를 import 했는데, 이는 settings.py파일과 static 폴더를 쓴다는 소리래. 왜?
이제 admin에서 이미지 확인하려고 링크 누르면 http://localhost:8000/media/blog/images/2025/09/11/스크린샷_2024-03-26_오후_1.34.35.png 같은 식으로 /media/아래로 지정한 주소 방식/이름 해서 이미지 뜸.
index_template.html 파일을 수정 + head image 없는 경우 if 문을 이용해 더미 이미지 출력.
전부 세팅 했는데, ![alt text](https://file%2B.vscode-resource.vscode-cdn.net/var/folders/kq/jy9fwtwj4vg59mpcmm2n8k3r0000gn/T/TemporaryItems/NSIRD_screencaptureui_WSbOAy/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202025-09-11%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.45.29.png?version%3D1757598336864)
* 오류 로그 : 이렇게 오류 발생. 왜 정상적으로 업로드가 안되는걸까?
    ->실수로 이미지 출력 src에 {{p.head_image}}라고 작성. {{p.head_image.url}}이라 작성해야 함.
상세페이지 이미지 출력 기능 추가.

13일차
filefield로 위와 같이 파일 업로드 기능 추가.
모델 수정했으나, runserver에서 새로고침하자 오류 -> makemigrations와 migrate 안해서.
하고 정상 업로드. html 수정해서 포스트 창에서 확인 및 다운 가능하게 해야.
포스트 리스트 + 싱글 페이지에 이미지 없을 경우 출력 생략
단, 포스트 리스트의 top 포스트가 이미지 없을 경우 lorem picsum으로 더미 이미지 출력('https://picsum.photos/가로픽셀수/세로픽셀수'
랜덤 포스트를 새로고침 시에도 고정하기 위해서, 시드 사용 -> picsum.photos/seed/id값(p.id)/가로픽셀수/세로픽셀수
항상 1번 포스트를 위에 올려두면 기능 확인이 어려우니, 포스트 순서 최신순으로 변경.(views 의 class postlist에 ordering = '-pk' 추가.)
첨부파일 다운로드를 별도 버튼 이용 : 
    기존 버튼 코드인 <button type="button" class="btn btn-outline-primary">Primary</button>에 다운로드할 파일 url 삽입해
    <a href="{{ post.attachment.url }}" button type="button" class="btn btn-outline-primary">Primary</button> 이렇게 했는데 문법 틀림.
    따라서 이를 해결한 ai 추천 코드인 <a href="{{post.attachment.url}}" download class="btn btn-outline-primary">다운로드</a>
    그런데 교재 추천의 경우 role = "button"이 웹 접근성 표준을 보다 충족함. 따라서 이것으로 변경.
    -> 최종적으로는, 하이퍼링크(a href)로 다운로드(download) 기능을 만들고 + 기존 css에 이미 존재하는 버튼 디자인을 차용해 버튼 모양으로 만들고(class) + 시각장애인용 스크린 리더 등에서 시스템적으로 버튼 취급(role)
모델에 함수 get_file_name, get_file_ext 추가. 각각 '파일명.확장자', '확장자'리턴. (ext : extension)
포스트 리스트의 카드 글자 수 제한 : truncatewords 할까, truncatechars할까. 생략이 단어에 맞추어 깔끔하게 떨어지는 것과 길이조정에 안정감있는 것 중에서.
일단 예시 기준으로 단어 단위로 자름. 이미지 있는 것과 없는 것 단어수 다르게 잘랐고, 요약문 추가 기능은 입력 시 손이 가는 부분이라 불필요할 것 같아 잘라냄.

추가적으로 해보고 싶은 것들
-최신 포스트를 위한 랜덤 이미지를 사용할 때, 로딩 시간 동안 spinner 적용하기
-포스트 리스트 좌우 카드 길이 동일하게 맞추기.
-첨부파일 다운 버튼을 button group 으로 바꿔서, "열기 | 다운"으로 나누기

14일차
테스트 기능
tests.py에서 수행함. DB수정 없이 다양한 상황 테스트 가능
Class TestView에, setup(기본 제공 오버라이딩)과 post list 테스트 -> 두 개 메서드(def).
포스트 목록 페이지 구조와 DB 상황에 따른 페이지 상태를 어떤 것을 검사할지 주석으로 나열.
pip install beautifulsoup4 (bs4 설치 완료)
코드 작성 및 실행.
>> python manage.py test 
Found 1 test(s). 
Creating test database for alias 'default'... 
System check identified no issues (0 silenced). 
F  # 여기까지 테스트 실행 중
====================================================================== 
FAIL: test_post_list (blog.tests.TestView.test_post_list) # 테스트 실패. test_post_list 메서드에서 실패함.
---------------------------------------------------------------------- 
Traceback (most recent call last):
 File "/Users/godayeong/Documents/GitHub/django_web_app/blog/tests.py", line 22, in test_post_list
  self.assertIn('About Me', navbar.text) #About Me가 있다는 것을 확인하는 코드
  ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^ 
AssertionError: 'About Me' not found in '\n\nBLOG with Django\n\n\n\nLanding\nAboutMe\nBlog\n\n\n\n' #우측 문구 보면 About Me는 없음(띄어쓰기 문제)
---------------------------------------------------------------------- 
Ran 1 test in 0.014s FAILED (failures=1)

AboutMe로 수정 후 재실행.
self.assertIn('아직 작성된 포스트가 없습니다.', main_area.text)
                                         ^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'text'
main_area가 어떤 값도 없는(None) 오브젝트라, text 라는 속성이 없다.
정확히는,         main_area = soup.find('div',id='main-area') 에서 main-area라는 id의 div를 찾지 못해 아무것도 main_area에 반환하지 못했고, 따라서 이 객체는 None(값 없음)이며, 이 경우 타입이 논타입으로 분류됨.
즉, 메인 에어리어를 만들 것.
blog entries의 div에 id 추가. <div class="col-lg-8" id="main-area">
                    
15일차
포스트 상세페이지 테스트 코드 -> post-area 추가. <div class="col-lg-8">에 임시로 추가하나, 해당 코드가 지금은 삭제된 '댓글'란을 포함하는 영역이기에, 향후 댓글란을 추가하게 되면 <article>의 바로 위 또는 아래로 div태그를 삽입해 해당 태그를 포스트 영역으로 할 것.
포스트 리스트 페이지도 main area를 footer와 navbar를 제외한 div class = container로 수정.  상세 포스트 페이지도 container에 main-area