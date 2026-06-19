# django_web_app
Django 학습용 토이프로젝트 식당 평가 및 추천 웹페이지


## 1일차
github 레포지토리 만들고 clone (private이기 때문에 ssh 키 이용.) -> ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBTc68rGmhY4r7SEK2JxALn+A/GEPvSm1p0Ct3KM95V4 tangball264@gmail.com
가상환경(venv)생성 -> source venv/bin/activate 명령어로 가상환경 실행. deactivate로 종료. pip list로 현재 패키지 확인

## 2일차
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

## 3일차
앱(maps) 생성 -> map으로 할걸 그랬다. 저장(maps 앱 생성하기)


## 4일차
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

## 5일차
*장고 셀 사용하기 (python manage.py shell) -> 파이썬 특유의 한줄씩 실행 가능. 끝내기(exit())
작성 시각과 수정 시각의 자동 저장
Q : models의 항목에 auto_now_add와 auto_now는 뭐가 다르지?
*오류로그 : 기존 models.py에서 changed_at 을 null 가능으로 해둠 -> 이번에 auto_now로 하면서 null 불가 -> 기존 post의 null을 어떻게 처리할지
    따라서 어떤 방식으로 수정할지 반문함. 
    ->나는 1번(하나의 디폴트 값으로 일단 전부 채운다)을 선택. 어떤 디폴트를 쓸지 반문하자 timezone.now(파이썬 언어로 답해야?)로 현재시간으로 지정. -> 장고 셸과 같은 부분?
실행후 확인하자 시간 입력칸이 사라짐.

## 6일차
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

## 7일차
개별 페이지 만듦. single_post_page를 urls, views, html 작성.
def single_post_page(request, pk): -> 여기에 pk를 함께 받아올 수 있구나. 앞에 urls에서 주소에서 <int:pk>를 받는데 이게 영향이 있으려나?
    post = Post.objects.get(pk=pk) -> all과 달리 get은 하나의 항목만 받아오는 쿼리.
posts페이지에 링크 만들기 -> <a href>로 p.get_absolute_url 을 지정 -> get absolute url? -> 그러나 연결 x. 실제 실행 시 <a href="">로 처리됨. -> 모델 수정 및 값 작성 필요.
get_absolute_url은 model에 def로 함수 작성. -> str처럼? -> view on site 기능 작성됨.
Q : history나 view on site는 기본 django에 있는 건가? 그러면 get absolute url 함수도 기본으로 있는거 쓰는건가?
A : 실제로 이미 존재하는 메서드가 맞으며, 메서드 오버라이딩을 위해 우리가 models에 작성하는 것.

## 8일차
single_pages 앱의 about_me 페이지와 landing 페이지 작성.
single_pages/urls.py 와 html 파일 작성.
models 안적어도 app 작성이 가능함. 

## 9일차
기존 페이지(FBV 방식)을 CBV 방식으로 전환
blog/views.py에 PostList 클래스 생성.(ListView 클래스 상속-사용.) 모델=포스트
urls.py에 index path대신  postlist 이용해서 path 지정 하도록 함.
*오류로그 : path는 끝에 쉼표 빼먹으면 서버 실행도 못함.
Q : blog/urls.py의 as_view()는 뭐지? 이 문법은 무슨 의미지?
view에서 postList에 템플릿 네임 지정.(혹은 post_list.html 파일을 만들어  사용.)
전자 이용했으므로 index.html 파일의 posts for문을 post_list(혹은 object_list)에 대한 for 문으로 변경
부트스트랩 blog 페이지 가져오기. 
*오류로그 : css 위치 틀렸는지, 부트스트랩 파일이 틀렸는지 정상 작동 안됨.

## 10일차
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

## 11일차
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

## 12일차
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

## 13일차
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

## 14일차
테스트 기능
tests.py에서 수행함. DB수정 없이 다양한 상황 테스트 가능
Class TestView에, setup(기본 제공 오버라이딩)과 post list 테스트 -> 두 개 메서드(def).
포스트 목록 페이지 구조와 DB 상황에 따른 페이지 상태를 어떤 것을 검사할지 주석으로 나열.
> pip install beautifulsoup4 (bs4 설치 완료)
코드 작성 및 실행.
>> python manage.py test 
> Found 1 test(s). 
> Creating test database for alias 'default'... 
> System check identified no issues (0 silenced). 
> F  # 여기까지 테스트 실행 중
>==================================================================== 
> FAIL: test_post_list (blog.tests.TestView.test_post_list) # 테스트 실패. test_post_list 메서드에서 실패함.
> ---------------------------------------------------------------------- 
> Traceback (most recent call last):
> File "/Users/godayeong/Documents/GitHub/django_web_app/blog/tests.py", line 22, in test_post_list
>  self.assertIn('About Me', navbar.text) #About Me가 있다는 것을 확인하는 코드
>  ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^ 
>AssertionError: 'About Me' not found in '\n\nBLOG with Django\n\n\n\nLanding\nAboutMe\nBlog\n\n\n\n' #우측 문구 보면 About Me는 없음(띄어쓰기 문제)
> ---------------------------------------------------------------------- 
> Ran 1 test in 0.014s FAILED (failures=1)

AboutMe로 수정 후 재실행.
self.assertIn('아직 작성된 포스트가 없습니다.', main_area.text)
                                         ^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'text'
main_area가 어떤 값도 없는(None) 오브젝트라, text 라는 속성이 없다.
정확히는,         main_area = soup.find('div',id='main-area') 에서 main-area라는 id의 div를 찾지 못해 아무것도 main_area에 반환하지 못했고, 따라서 이 객체는 None(값 없음)이며, 이 경우 타입이 논타입으로 분류됨.
즉, 메인 에어리어를 만들 것.
blog entries의 div에 id 추가. <div class="col-lg-8" id="main-area">
                    
## 15일차
포스트 상세페이지 테스트 코드 -> post-area 추가. <div class="col-lg-8">에 임시로 추가하나, 해당 코드가 지금은 삭제된 '댓글'란을 포함하는 영역이기에, 향후 댓글란을 추가하게 되면 <article>의 바로 위 또는 아래로 div태그를 삽입해 해당 태그를 포스트 영역으로 할 것.
포스트 리스트 페이지도 main area를 footer와 navbar를 제외한 div class = container로 수정.  상세 포스트 페이지도 container에 main-area
저장
모듈화 단계
모듈화 진행에 앞서 불필요한 html 파일 제거하고(템플릿 적용 전 파일 등), 이름을 정리하여 둘 필요 있다.

## 16일차
모듈화와 함께 템플릿 계열 파일의 내용을 보존한 채, 간소화한 이름의 파일로 모듈 내용을 옮겨야 함.
교재의 파일명을 따라가기로 함.
base.html -> 신규 페이지. post_list의 header, navbar, footer 파트 사용.
post_list.html -> 신규 페이지, index_template의 main_area 사용.
post_detail.html -> 신규 페이지. post_page_template의 main area 사용.(예정)
기존의 템플릿 적용 전 파일 삭제.(정확히는, 그거 이름 바꾸고 내용 지워서 사용중.)
이에 따라 views.py의 내용에서 html 파일 렌더링을 수정.
test-ok -> 교재는 왜 post_detail은 오류난다고 하는지 모르겠다. 나는 post_detail은 아직 손 안대어서 멀쩡함. 이제 그 부분 수정해야.
참고로 일부만 테스트 할 시, python manage.py test blog.tests.TestView.test_post_list 로 하면 일부만 테스트 가능.
이렇게 할 경우, navbar의 현재 페이지 표시가 정상적으로 작동할 지 알 수 없다. -> 하지만 navbar의 다른 항목인 랜딩과 어바웃미는 다른 앱이므로 괜찮을듯?
post_detail 파일 작성 후 테스트
test-failed : head 부분의 <title>이 맞지 않음. 해당 태그 안에서, 내용만 block head_title로 분리. 포스트 디테일 페이지는 변경할 값을 넣고, 그 외는 베이스 파일에서 삭제하지 않은 <title>의 값을 디폴트로 가져감.
test-ok
테스트 코드의 navbar 부분을 분리하고, 해당 버튼 클릭 시 연결 링크를 점검하는 코드를 추가. 
test-failed
  File "/Users/godayeong/Documents/GitHub/django_web_app/blog/tests.py", line 86, in navbar_test
    self.assertEqual(logo_btn.attrs['href'], '/blog')
FAIL: test_post_list (blog.tests.TestView.test_post_list) ->         <a class="navbar-brand" href="/">BLOG with Django</a> 정상인데?
아하
복붙수정하면서 아래처럼 썼는데
        logo_btn = navbar.find('a', text='BLOG with Django')
        self.assertEqual(logo_btn.attrs['href'], '/') 
        blog_btn = navbar.find('a', text='Blog')
        self.assertEqual(logo_btn.attrs['href'], '/blog') <-여기를 수정해야 했던거.
        about_me_btn = navbar.find('a', text='AboutMe')
최종적으로 url에 /blog/, /about_me/등으로 뒤에 슬래시 넣어주는 것까지 수정해서 test ok

## 17일차
기존 main-area 와 그 외 파트 모듈화 -> extends(확장)으로 모듈화
navbar, footer 모듈화 -> include로 함
이미 모듈화 결과를 확인할 test파트의 수정은 마쳤으니, 모듈화 작업 진행(navbar.html)
Q : 교재에서는 nav 태그와 그 아래 modal관련 내용을 모두 넣으라는데, 내 자료는 modal 항목이 없음. 검색 돌려도 없다. 
그냥 사용한 거 차이고, 모달 = 로그인, 로그아웃, 회원가입 등 버튼을 눌렀을 때 뜰 작은 알림창.
test-ok
해야할 일
1. 포스트 리스트에서 페이지 넘기는 거 포스트 수 맞춰서 뜨게 하고 링크 연결 기능.
2. 오른쪽 서치, 카테고리, 사이드 위젯 등 처리
3. 로그인, 회원가입, 로그아웃 등 기능(나중에 auther쓰려면 필요)만들기 + 모달 창 삽입해도 좋다.
4. 포스트 리스트 카드 길이 조절


## 18일차
작성자 추가하기
-> 모델에서 Post 모델에 '작성자'항목 추가, 유저 모델 생성, 카테고리 모델 생성
작성자와 작성된 글의 카테고리를 구분하는 형태가 되도록.
다대일 관계(작성자-포스트)와 다대다 관계(포스트-카테고리)를 구현하는 연습이기도 함.
구현 전에, 공부 목적으로 mysql을 이용해 EER 다이어그램으로 내 모델 구조 그리기.

작성자 기능에 대하여 어떻게 구현할 것인가?
ForeignKey : 기본제공되는 User모델의 정보(유저 id?)를 Post 모델에 외래키로 사용.
유저 탈퇴 : 탈퇴 시 선택지(작성한 포스트 삭제|보존) 제공, 포스트 삭제 시 해당 유저의 포스트를 모두 삭제한다, 보존 시 포스트의 author를 unknown으로 변경한다.

## 19일차
작성자는 admin창에서 추가 가능.
기존 포스트들은 기본admin 아이디인 kdy로 하고, 새로 james만들어서 작동하는 거 확인.
유저 삭제 테스트  - 경고 문구와 포스트 삭제 확인.
저장
사용자 삭제 시 author 값 변경(포스트 보존)
models.CASCADE : 삭제 시 이 포스트 통째로 삭제
on_delete=models.SET_NULL : 삭제 시 포스트에서 null값을 가짐. * null=true godi.
set_default로 하면 unknown으로 바꿀 수 있을 듯? 하지만 지금의 null로도 None으로 바꿀 수 있으니 불필요.
저장
포스트 목록 페이지 수정.
tests.py 에서 테스트 코드 만들기(user 모델 임포트, setup에서 유저 정보 생성, 기존 포스트 레코드 생성 시 author정보 입력 등 + 유저이름 대문자 표기가 메인 에리어 텍스트 중에 있다.)
html 파일에 기존에는 post title위에 <div class="small text-muted">{{ post_list.0.created_at }}</div> 로 표기했는데, 작성자와 함께 이 작성 시각을 card-footer로 옮겨 작성.
정상적으로 옮겨지지 않는다. 
card-body바깥, 그 /div 바로 다음 작성해서
<div class="card-footer text-muted">
    Posted on {{ p.created_at }} by
    <a href="#">{{ p.author | upper }}</a>
</div>
했는데, 출력은 Posted on by 뿐임. {{이 안 내용}}이 전부 사라짐.
p 지정의 문제인가? post_list.0 로 작성해야 했던 구간임. 그냥 내 실수구나.
최신 포스트를 위한 큰 블럭은 위와 같이 작성하고, 작은 블럭은 저렇게 하면 줄바꿈이 일어나 보기에 나빠서 수정.
작은 포스트는 기존의 small text-muted를 title위에 두고, 아래는 posted by {{author}}만 해둠.
test - ok
심미적 이유로 마지막 하이퍼링크 부분을 수정.
<a href="#" class="text-muted text-decoration-none">{{ post_list.0.author | upper }}</a> 
하이퍼링크의 파란색+밑줄을 제거.
포스트 상세 페이지에 작성자 추가.
우선 test 부터 수정하고
html 파일 수정
a href의 수정을 위한 css를 별도로 만들기로. -> style.css파일에 다음의 두 가지 삽입.
a.no-style {
  color: inherit;            /* 부모 요소 색상 그대로 */
  text-decoration: none;     /* 밑줄 제거 */
}

a.no-style:hover {
  text-decoration: underline; /* hover 시에만 밑줄 표시 */
}
스타일 적용에 오류 생겨서 대대적으로 뒤엎으며 원인 찾았는데 원인 : style.css가 아니라 styles.css라고 적어야 했음. 
하
test-ok. runserver후 디자인 확인 ok
저장


## 20일차
카테고리 기능 구현하기
모델에 category 모델 만들기 : 이건 지금처럼 def로 함수 만들거나 속성 하나를 만드는 게 아니라 하나의 class를 새로 만드는 것.
속성은 이름과 slug
Q : slug가 뭐지? SlugField는 뭐야?
향후 출력 시 이름만 받도록 __str__메서드 작성.
포스트 모델에 외래키로 카테고리 추가.
* 오류 로그 : makemigration 시도 시 NameError: name 'Category' is not defined 에러 발생
    왜? : 기존 Post 모델 밑에 Category 모델 작성 + Post에 ForeignKey 추가 -> 앞에부터 읽으니 카테고리를 읽기 전, 포스트에서 '카테고리' 모델이 없다고 오류를 띄움.
          그러니 카테고리 모델을 포스트 모델보다 위로 올림. 즉시 해결.
마이그레이션 진행 후 
admin.py에 category 모델 등록
기존 admin.py는 기본 제공인 groups, users 외에 blog에서 제공하는 post 항목 해서 보이게 해둔 게 전부임.
이번에는 이전에 언급만 한 #class PostAdmin(admin.modeladmin) 해서 일부 데이터만 보이도록 할 수 있음. 을 이용.
카테고리 어드민으로 자동으로 slug 채움.
Categorys 출력 확인. 추가로 원래도 '최근 활동' 이 있었나? 
+Categorys말고 Categories로 변경해야 함. models.py에서 카테고리 모델 안에서 meta 클래스를 작성 -> 이 모델의 메타 설정을 직접 건드려 복수형 수정.
        verbose_name_plural = 'Categories'
실행해서 카테고리 작성. slug는 적합하지 않은 글자는 자동으로 변환해서 형태 조정함.
포스트 모델 수정해서 blank=true 추가
포스트에 카테고리 작성함. 이제 이 작성된 db 내용을 확인해야 하는데, html파일에서 출력을 작성 안함 -> 장고 셸로 DB 살펴보기
>> python manage.py shell
교재 313쪽부터 셸로 쓰는 다양한 명령 보여주니 참고.     기본적으로 파이썬 같네.
이를 더 편하게 보기 위해 '셸 플러스'를 이용하면 더 좋다.
>> pip install django_extentions
>> pip install ipython
settings.py의 install_apps에 django_extensions 추가.
이제 아래 명령어로 셸 플러스를 실행 가능
>> python manage.py shell_plus
이전 줄 수정도 되고 되게 편하다.
In [1]: for p in Post.objects.all():
   ...:     print(f'{p} :: category - {p.category}')
이것저것 확인 다 하며 포스트 목록 페이지 수정해야 함.
기본적으로 카테고리 위젯이 있으니, 그거 기반 수정.
우선 구상을 기반으로 test부터 수정하고
category_widget_test()함수를 따로 만드는데
Q : 왜 이거를 setup(self)안에 만들지? 다른 것들은 이 함수 바깥에 만들던데?
A : 지금 251쪽 보면 def setUp(self): 와 def test_post_list(self):는 같은 라인 그런데 321쪽에서는 이 둘이 하나씩 뒤로 밀려 있음. 
    나는 일단 기존의 class 바로 아래 높이로 모든 def를 맞출 것. 321쪽이 오류라고 판단하기로. 지금껏 정상 작동함.
test 수정 내용 : 
    setup에 카테고리 2개 만들고, 포스트도 여기서 3개 만든다.
    category_widget_test(self, soup)를 새로 만들고
    test_post_list(self)의 내용을 대폭 수정.
        -기본적으로 setup에서 포스트를 3개나 만들어 둔 채이기 때문에, '포스트 없는'상태를 먼저 체크할 수 없음
        -따라서, 포스트가 3개 있는 상태를 먼저 체크
        -+ 그 전에 navbar 테스트 함수와 category widget 테스트 함수를 soup 을 주면서 실행시키고
        -포스트가 있는 상태에서의 확인이 다 끝난 후, Post.objects.all().delete()를 이용해 포스트 개수를 0로 만들어 포스트가 없는 상태 확인
그리고 이제 html 파일에서 div 요소를 부여
views에서 category도 import 하고, 카테고리 위젯을 위한 정보 받아오기
** 내 views가 교재와 다른 점이 많으니 나중에 수정 필요 **
카테고리 위젯을 base로 옮기기. - 기존에는 <div class="container" id="main-area"> 바로 아래부터 블록했으나, 그 아래 div class=row 밑부터 블록으로 수정.
base에서 카테고리 위젯에 categories 정보 출력. -> base에 카테고리가 있으니 post_list 것 말고도 post_detail것도 수정되는데, 그 쪽은 카테고리 정보를 받아오도록 view 수정을 하지 않아서, 정상 작동하지 않음. 나중에 윗윗줄에서 말했듯 view 수정 들어가야 함.
카테고리 링크 -> 해당하는 포스트만 목록으로 보여주기. 아직 구현 x.

test - failed
왜 안되는거지?
ERROR: test_post_list (blog.tests.TestView.test_post_list)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/godayeong/Documents/GitHub/django_web_app/blog/tests.py", line 65, in test_post_list
    self.assertIn(self.post_001.title, post_001_card.text)
                  ^^^^^^^^^^^^^
AttributeError: 'TestView' object has no attribute 'post_001'
>> <div class="card mb-4" id="post-{{post_list.0.pk}}">랑 <div class="card mb-4" id="post-{{p.pk}}">를 했는데?
* 오류 로그 : 테스트 실행했는데 setUp에서 생성한 post_001을 포함한 포스트들을 다른 test의 함수들이 인식하지 못함
    왜?   : setUp에서 post 생성할 때, 나는 지역변수(post_001 = Post.objects.create())로 생성. self.post_001로 생성해야 정상 작동
이제 test상의 문제는 처리되었고, 니머지는 테스트와 html 간의 차이 찾아 html을 수정해야 함.
    포스트 카드에서 카테고리 이름과 같은 텍스트가 발견되지 않음. -> card-body에 span태그로 뱃지를 부착.
    부트스트랩 사이트에서 가져온 <span class="badge rounded-pill text-bg-info">Info</span> 이거 사용할 것. 나중에는 카테고리 모델에 '색'항목을 추가한 다음, 카테고리별로 다른 색을 붙여도 좋을 듯
+작성일을 이전에 card-body위에 했는데, 카테고리가 이거랑 같이 쓰니까 줄바꿈이 되어 시각적으로 별로. 못생김.
    따라서 한 줄 안에 쓸 수 있도록 gpt에게 물어 부트스트랩 유틸리티 클래서(flex)를 사용하는 형태로 수정.
    <div class="d-flex align-items-center">
        <div class="small text-muted me-2">{{ p.created_at }}</div>
        <span class="badge rounded-pill text-bg-info">{{ p.category }}</span>
    </div>
교재는 float-right로 오른쪽 끝에 배치하는데, 
메인은 <span class="badge badge-secondary float-right">{{ p.category }}</span> 이거 쓰고
근데 나는 이거 하면 안뜨는게, 부트스트랩 4에만 있는 부분같아. float-end로 float-right를 대신할 수 있대.
이거 사용 시 제목 공간의 우상단 일부를 사용하게 되는데, 대부분은 기존에 내가 선택한 방식이 더 마음에 들고, 큰 카드로 보여주는 부분만 이거 적용하기로.
test-ok
추가적으로 교재는 카테고리 목록을 옆에 점 붙이는데, 나는 없는 게 예뻐보여서 그대로 둘 것.
평소에 test를 
python manage.py test blog.tests.TestView.test_post_list   로 하는 대신 걍 평소에 test를 python manage.py test로 했더니 하다가 post_detail 테스트도 수정 마침.
get_contextdata를 postdetail 클래스에 추가.

views 수정하기
173p까지는 기존의 def 방식 사용.
아, 9일차에 CBV로 포스트 목록 페이지 만들기를 하면서 발생한 문제였다.
193페이지 내용을 참고하여 수정.
-views.py, urls.py 수정.
-정상적으로 실행됨.
그리고 335p로 돌아와, views.py에 get_context_data를 postdetail클래스에도 복사-붙여넣기
tests.py에서 post_list 부분에서도 카테고리 위젯과 포스트의 카테고리 출력 테스트하게 함.


## 21일차
카테고리 창 만들기
- 테스트 수정(카테고리 창을 위한 테스트 함수 별도 작성)
- models.py에서 카테고리에 get_absolute_url 함수 추가.
- urls.py에 위에서 지정한 url대로 카테고리창의 url 작성.
- urls에서 views.category_page로 주소에 포함된 slug를 넘기기로 했으니, views.py에 category_page()함수를 만든다. -> CBV에 따른 클래스 하위의 메서드가 아니라, FBV방식에 따라 클래스 바깥에 함수로 만들기.
- 큰 틀은 blog/post_list.html을 이용하되, 주어지는 포스트 정보를 필터링하는 형태로 간다.
- post_list.html 파일을 수정해 카테고리를 받을 때, 이를 h1  에서 배지 형태로 출력.
test - failed : views에서 render(request, html템플릿 주소, 기타)순으로 써야 하는데 request 빼먹음
test - failed : test_category_page()에 self.assertIn(self.category_programming.name, soup.h1.text) 라는 내용이 있는데, 이건 교재 예시에서는 <h1>이 페이지 전체에 한 번만 쓰이기 때문. 하지만 내가 고른 템플릿은 base.html의 헤더에 h1태그가 쓰이므로, 앞에 사용된 h1태그만을 인식하여 오류가 발생. h1_tag = main_area.find('h1') 를 추가하고, soup.h1.text대신 h1_tag.text로 수정하여 대상을 좁히는 방식으로 임시 변경. 이는 후일 디자인을 변경할 수 있다
-> header 부분에 'Blog' 와 '카테고리 뱃지'가 들어가도록 수정하거나?
-> 혹은 예시처럼 헤더 부분을 간소화하던가.
일단 테스트를 다음처럼 수정.
        h1_tag = main_area.find('h1')
        self.assertIn(self.category_programming.name, h1_tag.text)

        self.assertIn(self.category_programming.name, main_area.text)

현재는 '미분류' 카테고리 페이지 동작 x.
views.py의 category_page함수에서 if-else문 사용.

## 22일차
카테고리 페이지 이어서. 
오류 발생. 정확히는 모르겠지만, views.py의 카테고리 페이지 함수에서 
    else :
        post_list =  Post.objects.filter(category=category)
        category = Category.objects.get(slug=slug)
    이렇게 쓴 거를 else안의 두 줄 순서 바꿈.
    아마 post_list 정의에 category값이 필요한데 둘 순서를 잘못 둔 탓에 카테고리가 없어서 인듯.
수정 후 저장.

다대다 관계를 이용하여 tag모델 만들기
기본적으로는 카테고리 모델을 복붙해 쓰되, 복수형을 수정할 필요는 없으니 meta클래스만 삭제
이렇게 name, slug 필드 갖고 str과 url 함수가 있는 tag 모델 작성. 
post모델에 tag 필드 추가 -> 외래키가 아니라 manytomanyfield로 작성.
보통 만들 때 관계형 db 생각하면 이런 다대다 관계는 릴레이션이 '포스트', '태그', '포스트-태그' 해서 3개로 분리하는 게 정석일 텐데, 다대다 관계 전용 필드 형식이 있다니
    참고로 ManyToManyField로 만든 필드는 기본적으로 null=True 설정이기에 필드에 그걸 포함하면  WARNINGS: blog.Post.tag: (fields.W340) null has no effect on ManyToManyField. 같은 식으로 경고함.
이제 태그를 관리자 페이지에서 보고 사용하도록 admin.py 변경 : 카테고리의 클래스categoryadmin까지 복붙하여 tag로 수정(import도 하고)

테스트 코드 수정. (포스트 리스트)
post_list 수정 -> 왜 안됨?
        self.assertIn(self.tag_hello.name, post_001_card.text)
        이렇게 써야 정상인데 self.tag_hello만 쓰니 문자열 A가 문자열 B에 포함되었는가? 가 아니라 태그 A가 문자열 B에 포함되었는가? 가 된 것.
        형식을 맞추어 name으로 해야 함.
폰트어썸 삽입 안됨. 기존 교재 복붙했더니 배지가 부트스트랩 버전 변경으로 안나와서 문제였음.
일단 대충 처리했는데 시각적으로 별로이니 수정해야.
이전의 줄바꿈 생략인 
    <div class="d-flex align-items-center">
    이거 사용하려고 했는데, 줄바꿈 외에도 자연스러운 공백까지 생략해서 별로임.

폰트어썸 가입 후 사용으로 방향 결정.
이 프로젝트 파일을 저장한 github계정이 고다영(tangball264) 구글계정을 연동하여 로그인하므로, 같은 이메일로 폰트어썸 무료 계정 생성.
kit code 를 포함한 내 kit 만듦.
정상작동 확인. 향후 디자인 수정 권장. 
test-failed. 왜?
post-list에서 이미지 유무에 따라 다르게 했는데, 이 분리 과정에서 '이미지 있을 때' 버전에만 태그 추가함. 수정.
test-ok

테스트 코드 수정(상세페이지)
post_detail.html도 수정.
test-ok
저장

태그 페이지 만들기
해당 태그의 포스트만 보는 포스트 목록 페이지. 즉, 카테고리 페이지와 같은 방법으로 하면 되는 듯.
우선 테스트 함수 만들기. navbar, category 테스트 함수 가져와 재활용.
urls의 태그 페이지 주소 작성 및 views 에서 카테고리 페이지 함수 복붙한 태그 페이지(FBV) 만들기.
추가적으로 header와 "Blog (카테고리뱃지)" 적힌 게 h1 태그 중복이라 테스트 변형해서 뱃지를 main에 넣고 찾기도 거기서 했던 거를 카테고리, 태그 페이지에서는 헤더 대신 Blog (뱃지)보이게 수정. 디자인상 패딩 주려고 div 하나 씌움.
test-ok

## 23일차
전일 한 태그 페이지 저장
포스트 작성 페이지 만들기
-이건 로그인 페이지도 만들어서 로그인 기능을 구현하면 Author를 자동입력할 수 있을텐데. 일단 나중에 한다고 치자
-교재에서는 로그인 페이지는 만들었지만 기능은 아직이고

포스트 작성 페이지는 유저가 내용을 입력할 빈 칸(=폼)이 필요.
과정
1. 테스트 코드 def test_create_post(self)작성하기
2. views.py와 urls.py에 포스트 작성 페이지 관련 내용 추가
3. 포스트 작성 페이지를 위한 html 작성하기
4. test-ok

{% csrf_token %} : 장고가 제공하는 'csrf 공격' 방어 기능. 폼 태그 안에 넣기.
방문자의 입력값을 서버에 전달하는 방법 : Post와 Get. get의 경우 보다 간단하지만 길이제한 등이 있다.

실제 runserver 결과 서치랑 카테고리가 폼 옆이 아니라 밑에 붙어 나옴. 
다른 두 파일(포스트리스트, 포스트 디테일.html)에서는 
    <div class="col-lg-8"> 가 존재. 
    아마 교재에서는 이게 main-area 바깥 부분인듯. 나도 동일하게 수정한다.
그리고 위젯과 h1 모두 너무 위에 붙어 header 부분에 br(원래 hr하려고 했는데 그거는 줄 생기는 거라 바꿈)2개 추가.
폼 디자인 별로인데 수정 필요.

기본 폼의 형태가 교재랑 다른데 이에 대해서는 별도로 검색해야 할 듯. 오늘은 여기까지.

## 24일차
어제 이어서, 폼 디자인 변경.

폼 디자인이 다른 이유 : 
Bootstrap 5는 table 기반 폼 미지원.
Bootstrap 4까지는 form-horizontal 같은 테이블식 정렬을 썼지만, Bootstrap 5에서는 flex와 grid 기반으로 완전히 바뀜
따라서 <table>{{ form }}</table>를 쓰면 CSS 리셋(특히 Bootstrap의 table 스타일)이 기본 폼 구조를 깨뜨림.
→ 결과적으로 라벨과 입력칸이 들쭉날쭉하게 보여.
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit" class="btn btn-primary float-end">완료</button>
</form>
이 형태 추천.
기존의 <table> {{ form }} </table> -> {{ form.as_p }} 로 변경.
간격 문제가 조정됨. 그러나, 입력란 정렬은 안됨. 나중에 부트스트랩으로 편집하면 좋을 것.

로그인 시에만 포스트 작성이 가능하게 하고, 자동으로 작성자 입력하기
- 테스트 코드 작성 : test_create_post수정. 로그인 안한 기본상태에서는 status_code != 200. 에디로 로그인 후 200
- views.py postcreate 수정 : LoginRequiredMixin(장고 제공 클래스) 추가해서 로그인했을때만 정상적으로 페이지 보임.
    *PostCreate 클래스에 기존에 상속받던 CreateView 클래스와 함께 LoginRequiredMixin 클래스를 상속받게 하는 것.
     이게 CBV의 방식.
test - ok
runserver로 로그인 시 접속 안되는 거 확인.

http://127.0.0.1:8000/accounts/login/?next=/blog/create_post/
로그인 창 구현해두면 그곳으로 이어지도록 하는 것.

- 테스트 코드 수정 : 포스트 작성 및 submit 버튼 클릭까지 테스트.
- 즉시 실행해보면 test-failed. 작성 시 로그인된 계정 eddi가 자동으로 '작성자'로 등록되지 않음.
- views.py의 PostCreate 클래스 내에, form_valid 함수를 재정의
    * form_valid : 사용자가 제출한 폼이 유효할 때(form.is_valid() == True)
    * form_invalid : 사용자가 제출한 폼이 유효하지 않을 때(form.is_valid()==False)
    * user.is_authenticated : request.user 객체의 속성. 이 유저가 로그인되었는가?. 로그인 여부를 True/False로 반환.
** 수정 : 교재에서는 return super(PostCreate, self).form_valid(form) 를 사용하나, 파이썬 버전 3에서는 기본제공 리턴값처럼 return super().form_valid(form)를 사용할 것을 권고함. 저건 2의 방식. super(class, self)하는 것은 구문이 길고 중복 가능성이 있어 권장하지 않는다고 gpt가 말함
두가지 각각 테스트해볼 것.
return super(PostCreate, self).form_valid(form) : Test-ok
return super().form_valid(form) : test-ok
권장되고 간략한 후자로.

+ 리다이렉트 /blog/하는거는 주소 수정시 일일이 다 고쳐야 해서 권장하지 않고 return redirect('blog:post_list') 같이 URL 이름을 쓰거나 reverse()/reverse_lazy()를 사용하는 게 좋음 이라는데 너무 기본적이고 근본적인 페이지로 리다이렉트라서 그냥 둘 생각.

다음 단계는
스태프/최고관리자 권한 부여(그리고 해당 유저들만 글 작성 가능) -> 나는 글 삭제 권한에 대해 어떤 구조인지 체크해야 할 듯. 
-> 이건 삭제 기능부터 만들어야 하긴 함.
ddd


## 25일차
오랜만에 왔으니 진행도부터 체크하자.
마지막 git commit 은 '로그인한 사용자에게만 포스트 작성 페이지 열어주기' 다.
그런데 실행해서 검토해보니 태그 페이지에 태그 아이콘을 넣었는데 이게 깨져서 사각형애 X채워진 걸로 나옴. 
이거 우선 수정하고, 그 다음 테스트 파일 검토 후 390페이지부터 수행하자.
아이콘 적용해놓은게 단체로 깨짐.

아이콘 깨짐 ai로 이유 찾아보니 걍 폰트어썸 free에서는 regular 안되고 solid로 해야 되는 경우가 있다고. 특히 폰트어썸에서 무료-유료 변환으로 인해 발생하는 문제.
실제 수정하니까 그것만 정상 작동함.
이유는 찾았고, bootstrap 아이콘으로 바꿔버릴까 고민중.
여튼 태그 아이콘 문제 수정 완료
bootstrap으로 바꾸는 건 나중에 프로젝트 내용 전부 진행하고 하던가 하기로.

우선 390페이지 진행에 앞서 내가 아직 하지 않았고 교재에는 진행된 부분
: navbar에 login 추가

진행하기
관리자 페이지에서 user를 추가할 때, 권한을 부여할 수 있게 하기
-> 스태프만 포스트를 작성하능하게 만들기 위해, 우선 스태프를 구분.
-> UserPassesTestMixin 사용
우선 테스트 코드 수정해 임시유저에게 is_staff를 조정하기.
Q : 왜 '유저 계정 만들기' -> '해당 유저의 is_staff를 True로 조정' -> '해당 유저 정보 .save()'의 3단계를 거치는지. 즉, 왜 save를 별도로 하는지 궁금해.
그리고 테스트 코드 수정해서 create_post()가 스태프가 작성 페이지 들어가면 status code가 200이고 스태프 아닌 유저가 들어가면 아님(실패) 되는지 확인
수정 마쳤고, 즉시 테스트해보면 당연하게도 실패. views.py에 위에서 언급한 userpassestestmixin추가해야.
기존 로그인 시에만 가능으로 loginrequiremixin이 있었는데, 그 옆에 이것도 추가.
그리고 기존 로그인 시인 postCreate클래스에 is_staff 및 superuser 확인하는 함수 만들기. -> 이게 만드는 게 아니라 기존에 test_func 있어서 수정하는 거였음. 원래 이게 무슨 기능인가? 원래도 '이거에 접근해도 되는 사용자인가?'를 확인하는 목적이다.
 그리고 같은 클래스의 form_valid에서도 조금 수정해서 '인증된'유저 여부와 함께 superuser, staff 확인.
test-ok

포스트 작성 버튼은 내일.

## 26일차
생각보다 늦게 재시작하네.
일단 navbar 디자인을 조금 변경.
주요 navbar 링크들을 좌측으로 옮기고, 우측에 login 버튼 추가. 동시에 사이트 아이콘으로 코드</> 이 모양을 사용하기로 함. 추가.
* navbar 요소 위치 조정 방법 : ms-auto (우측정렬|권장). 좌측정렬은 ul에 정렬을 적지 않고 디폴트로 출력. 우측정렬은 ul에 이 ms-auto를 추가.

그 다음으로 new post 버튼 만들기
위치는 post_list.html 파일. 맨 위에(block 문 아래)
'로그인된'(=user.is_authentucated)상태에서만, 또한 그 권한이 슈퍼유저 혹은 스태프일 때 'New Post'버튼이 보인다.
제작 과정
<a class="btn btn-info float-right" href="#" role="button">New Post</a>
이렇게 기본 link button 쓰니 좌측, 그리고 아래 포스트 리스트에 너무 붙어버림. 분명 float right를 했는데 왼쪽에 붙음. 맞다. 이전에도 float-end로 바꾸었음.
그러자 최신 포스트 리스트의 오른쪽에 가버림.
base.html의 {% block header_text %} 파트를 예시와 같이 이 버튼 바로 아래 배치하여 위치 조정하기로. 옮기고 block은 삭제. 
또한 해당 페이지가 'BLOG'텍스트 외에도 메인 타이틀 기능을 하고 있었기에 현재와 같이 두면 메인 타이틀이 잘려버리는 문제 발생. 따라서 해당 파트 및, 그걸 유지하기 위해 해둔 각종 비효율적 조치 전체 삭제. 간략화.
추가적으로 버튼 위치가 너무 높아 상단에 여유 공간 두기. 아이콘 및 띄어쓰기는 교재 참고.
**챗지피티에서 float-end로 레이아웃 잡는 것이 부적절하다고 주장. 이것이 부트스트랩 버전차로 인한 영향인지, 혹은 할루시네이션인지 정확히 알 수 없음. chatgpt는 flex 사용 권장**
그리고 높이 조정을 위해 main-area 컨테이너에 mt-4 추가로 상단 공간 만들어둠.
나중에 getbootstrap 문서에서 form 파트 확인해서 form 디자인 수정하기.
오늘은 여기까지.

## 27일차
그동안 다른 자격증 공부하다가 오랜만에 복귀. 일단 현재 진행상황을 다시 보고, 진행하려던 단계 해야 함.
python manage.py runserver : 정상적으로 서버 동작. 로그인 버튼 존재함. 로그인 페이지 연결 안됨. admin으로 진행하여 로그인 필요. kdy, mysuperuser. 로그인 상태에서도 login 버튼 사라지지 않음. 로그인 상태에서만 new post 버튼 나타나는 것 확인됨. 포스트 작성 폼 확인됨.

만약 로그인 상태에서 폼으로 진입한 후 로그아웃을 하고 포스트 작성 완료를 누를 경우, 작성이 되는가?
Using the URLconf defined in django_web_app.urls, Django tried these URL patterns, in this order:
admin/
blog/
about_me/
^media/(?P<path>.*)$
The current path, accounts/login/, didn’t match any of these.
이렇게 실패하네. 404 page not found

스태프 권한 확인하기
adduser : staff1, staffaccount
adduser : common1, commonaccount
스태프권한으로 작성 가능 확인.
일반 권한으로는 아직 정상 로그인을 못해서 확인 불가.
대신 test쪽으로 확인해야 함.
test 결과 : failed. 
사유 : navbar 수정 중 <a>태그 안에 <i>태그 후 'BLOG with Django'텍스트가 들어가서.
기존의 정답에서는 <a>'BLOG with Django'</a>였기에 logo_btn = navbar.find('a', text='BLOG with Django') 가 정상적으로 찾을 수 있었는데, 이게 <a><i></i>'BLOG with Django'</a>가 되면서 탐색이 실패(NoneType 반환)하는 것.
즉, 디자인 변경이 들어가며 기존의 navbar 코드와 달라졌고, 따라서 테스트 코드에 변환이 필요.
하여 
#logo_btn = navbar.find('a', text='  BLOG with Django')
대신
logo_btn = navbar.find('a', text=lambda t: t and 'BLOG with Django' in t)
사용.
오늘의 TIL : lambda t: t and 'BLOG with Django' in t 로 사용한 '람다 함수'


test-ok : python manage.py test blog.tests.TestView.test_create_post 로 분리해서 보면 성공.
test-failed : % python manage.py test                                     
Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
E.EEE
======================================================================
ERROR: test_category_page (blog.tests.TestView.test_category_page)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/godayeong/Documents/GitHub/django_web_app/blog/tests.py", line 175, in test_category_page
    self.navbar_test(soup)
    ~~~~~~~~~~~~~~~~^^^^^^
  File "/Users/godayeong/Documents/GitHub/django_web_app/blog/tests.py", line 162, in navbar_test
    self.assertEqual(logo_btn.attrs['href'], '/')
                     ^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'attrs'

======================================================================
ERROR: test_post_detail (blog.tests.TestView.test_post_detail)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/godayeong/Documents/GitHub/django_web_app/blog/tests.py", line 132, in test_post_detail
    self.navbar_test(soup)
    ~~~~~~~~~~~~~~~~^^^^^^
  File "/Users/godayeong/Documents/GitHub/django_web_app/blog/tests.py", line 162, in navbar_test
    self.assertEqual(logo_btn.attrs['href'], '/')
                     ^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'attrs'

======================================================================
ERROR: test_post_list (blog.tests.TestView.test_post_list)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/godayeong/Documents/GitHub/django_web_app/blog/tests.py", line 66, in test_post_list
    self.navbar_test(soup)
    ~~~~~~~~~~~~~~~~^^^^^^
  File "/Users/godayeong/Documents/GitHub/django_web_app/blog/tests.py", line 162, in navbar_test
    self.assertEqual(logo_btn.attrs['href'], '/')
                     ^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'attrs'

======================================================================
ERROR: test_tag_page (blog.tests.TestView.test_tag_page)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/godayeong/Documents/GitHub/django_web_app/blog/tests.py", line 193, in test_tag_page
    self.navbar_test(soup)
    ~~~~~~~~~~~~~~~~^^^^^^
  File "/Users/godayeong/Documents/GitHub/django_web_app/blog/tests.py", line 162, in navbar_test
    self.assertEqual(logo_btn.attrs['href'], '/')
                     ^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'attrs'

----------------------------------------------------------------------
Ran 5 tests in 4.893s

FAILED (errors=4)
Destroying test database for alias 'default'...
전체 실행 시 실패. 

현재 실패한 테스트코드는
1. 카테고리 페이지(프로그래밍 카테고리)
2. 포스트 상세 페이지('/blog/1/')
3. 포스트 목록 페이지('/blog/')
4. 태그 페이지(헬로 태그)

테스트코드의 구성은 다음과 같다.
tests.py
  └─ TestView (TestCase 클래스)
     ├─ setUp()
     ├─ category_widget_test()
     ├─ navbar_test()
     │
     ├─ test_post_list()
     ├─ test_post_detail()
     ├─ test_category_page()
     ├─ test_tag_page()
     └─ test_create_post()
그 중,  카테고리 위젯 테스트와 내비게이션 바 테스트는 보조 함수로 다른 테스트에서 호출됨.
나머지 5개의 테스트 중, navbar_test를 호출하지 않는 test_create_post를 제외하고 나머지 넷 모두 같은 구간에서 오류 발생. 나중에 전체 수정해야 함.
현재 임의로 logo_btn 관련 파트 일괄 주석 처리하자 ok
logo_btn = navbar.find('a', href='/') 로 처리하고 실행해도 ok.

할 일 : logo_btn 문제 해결하기. 해결 과정에서 얻은 지식(lamda등) TIL 기록하기

logo_btn 수정.

## 28일차
포스트 수정 페이지를 만들자.
1. 테스트 코드 작성하기(이 단계에서 이 페이지의 기본 요건을 정의한다.)
2. urls.py와 views.py를 수정한다.
- view 만들 때, 권한과 CBV 사용에 주의.
3. 필요한 html을 작성한다.

## 29일차
테스트 코드 작성 완료 확인
urls.py : post의 pk값으로 url 구분. CBV 방식으로 사용
views.py : Django.views.generic 에서 UpdateView를 추가로 import. 내용은 기본적으로 포스트 작성을 위한 클래스와 유사하게.
class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'attachment', 'category', 'tags']
테스트 결과 : 작성자 외 유저로 수정 시도 시 status code가 404->200으로 변경.

즉, 현재로서는 작성자 식별 기능이 부재하다.

CBV에서 제공되는 dispatch 메서드를 이용하여 요청 방식을 판단할 수 있다.
요청 방식
- GET 방식 : 방문자가 서버에 들어옴. 이제 서버는 방문자에게 폼 페이지를 보내줘야.(CreateView나 UpdateView에서)
- POST 방식 : 방문자가 작성한 폼을 서버에게 보냄. 이제 서버는 그 폼이 유효한지 확인하고, 유효하다면 DB에 저장.
*이거 오늘 TIL로 하자.
디스패치 메서드에서, 요청이 유효한 유저에 의해 발생했다면 마저 수행한다.
그렇지 않다면 PermissionDenied로 403 오류메시지를 보낸다.

다음 할 일
포스트 상세 페이지에 포스트 수정 버튼 넣기 : 포스트 리스트 페이지의 new post 버튼 가져다가 권한이랑 링크, 텍스트 수정해서 post_detail 페이지 수정.
포스트 수정 페이지 제목을 Create Post - Blog 에서 Edit Post - Blog로 수정하기. : 기존 post_form 공유 대신 post_update_form.html 작성하기.
완료


## 29일차
태그 선택란 추가
현재 '수정'페이지에서는 태그 선택이 포함됨. 그러나, 기존 태그만 선택 가능.
텍스트를 입력해 원하는 태그를 작성하도록 하는 기능.

우선 현재의 폼 내용을 runserver 후 페이지 소스 보기로 확인한다.(html에서는 {{ form.as_p }}이라 구분이 안됨.)
```
<p>
  <label for="id_title">Title:</label>
  <input type="text" name="title" maxlength="50" required id="id_title">
</p>
<p>
  <label for="id_content">Content:</label>
  <textarea name="content" cols="40" rows="10" required id="id_content">
  </textarea>
</p>
<p>
  <label for="id_head_image">Head image:</label>
  <input type="file" name="head_image" accept="image/*" id="id_head_image">
</p>
<p>
  <label for="id_attachment">Attachment:</label>
  <input type="file" name="attachment" id="id_attachment">
</p>
<p>
  <label for="id_category">Category:</label>
  <select name="category" id="id_category">
    <option value="" selected>---------</option>
    <option value="1">게임 &amp; 취미</option>
    <option value="2">사담</option>
    <option value="3">프로그래밍</option>
  </select> 
</p>
```
교재에서는 <table>{{form}}</table>이고 내용물도 <table>과 <tr><th><td>를 사용
난 버전이 바뀌면서 gpt에 물어서 {{ form.as_p }}을 사용했고, 위의 테이블이 없어지고 그 부속 파트가 전부 <p>로 처리됨.
그 외 label, select, option 등의 태그는 기존 버전과 동일한 것으로 보인다.

교재 내 요청 사항 : {{form}} 바로 아래(<table></table>안에) 내용 추가.
```
<tr>
  <th><label for="id_tags_str">Tags:</label></th>
  <td><input type="text" name="tags_str" id="id_tags_str"></td>
</tr>
```
을 해당 위치에 삽입한다.

나의 경우, 해당 내용을 삽입하면 어떻게 변하는가?
일단 테이블이 없어서 정상 작동할지부터 문제.
*추가적으로 포스트 작성에는 태그 칸이 없어 사후 추가함.

해당 문제와 기존 as_p의 배치가 들쭉날쭉한 문제를 종합적으로 해결 가능한 수단을 찾음.
as_p대신 as_table로 하면 교재와 동일한 방식으로 작성할 수 있고, 작동 역시 동일하게 한다.
따라서 수정했음.

입력란 추가 및 삭제는 완료
이제 입력 기능을 넣어야 함.
1. 입력 기능을 넣은 후에 사용할 테스트 코드 만들기
2. 입력 기능을 넣기. : views.py의 form_valid 수정.
3. 테스트 및 runserver로 기능 시험해보기
4. 모두 통과 되었으므로, 저장.


## 30일차
포스트 수정 페이지를 위한 태그 기능 구현하기

포스트 수정 페이지는 '기존에 입력된 태그'를 확인하고, 수정할 수 있어야 한다.
또한 새로이 입력되는 태그를 추가하여야 한다.

1. 테스트 코드 작성하기
- test_update_post를 수정함.
- 시범 테스트
-   File "/Users/godayeong/Documents/GitHub/django_web_app/blog/tests.py", line 291, in test_update_post
    self.assertIn('파이썬 공부; python', tag_str_input.attrs['value'])
                                         ~~~~~~~~~~~~~~~~~~~^^^^^^^^^
    KeyError: 'value'
- 수정 페이지 들어가면, 원래 태그들이 Tags의 입력창에 미리 적혀있어야 함. 그 기존값들이 'value'값.
2. 코드 수정해 기능 넣기
- html파일에 태그 창 넣기는 이미 완료. value속성을 추가하고 default하기.
- views.py 수정하기. : get_context_data, form_valid 작성.
3. 테스트 : faild
- 왜? 어째서 edit 들어가면 기존 태그를 출력하는 기능이 작동하지 않는 것일까?

## 31일차
오류 원인 찾음.
사유 : views.py의 PostUpdate클래스 내 get_context_data 작성 중 오타 발생.
context['tag_str_default'] = '; '.join(tags_str_list)
tags_str_default가 맞다. s하나 빼먹어서 오류......
수정 후 test 진행하자 오류 발생

traceback (most recent call last):
  File "/Users/godayeong/Documents/GitHub/django_web_app/blog/tests.py", line 310, in test_update_post
    self.assertIn('파이썬 공부', main_area.text)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: '파이썬 공부' not found in (이하생략)

----------------------------------------------------------------------
Ran 6 tests in 6.545s

FAILED (failures=1)
그러나 runserver로 시험해보니 정상 작동.

오류가 tests.py에 있었음.
test_update_post에서 변수 tag_str_input = main_area.find('input', id='id_tags_str')와 
그 내부 포스트의 요소인 'tags_str' : '파이썬 공부; 한글 태그, some tag'을 혼동하여 후자도 tag_str로 작성.
이로 인하여 오류 발생.

test-OK

다음 단계
입력 폼 꾸미기
django-crispy-form 사용 예정. pip install 시행. settings.py INSTALLED_APPS에 등록. *이 때, 템플릿 팩 지정에 교재와 달리 bootstrap5사용.
post_form.html 수정해서 적용.

오류 발생.
부트스트랩 버전 4->5 넘어오고 crispy도 버전 2.0으로 넘어오면서 install부터 settings 적용까지 변화가 상당히 있었고, 따라서 나도 수정해야 함.
AI 내용을 바로 따라도 되는지 확인을 위해 crispy 문서 확인
https://newreleases.io/project/pypi/django-crispy-forms/release/2.0a1?utm_source=chatgpt.com
부트스트랩 2, 3, 4는 템플릿 제거 및 별도 패키지로 이동
부트스트랩5는 아예 외부 패키지(crispy-bootstrap5)로 제공
따라서 pip install crispy-bootstrap5 실행 후 CRISPY_TEMPLATE_PACK외에도 CRISPY_ALLOWED_TEMPLATE_PACK을 지정해서 보안 체크를 해야
참고 : https://github.com/django-crispy-forms/crispy-bootstrap5 내 README.md 의 Useage 파트.

페이지 전체로 바뀜. 작성완료 버튼 간격 추가 위해 중간에 <br/> 코드 삽입
그 외 main-area요소 전체가 상단 navbar와 하단 footer에 지나치게 붙음. 전체 div로 감싸고 마진 부여.
업데이트 폼도 마찬가지로 수정.

## 32일차

마크다운 적용하기

django-markdownx를 설치하여 포스트에 마크다운 문법을 적용하면 포스트에서 줄바꿈이 되지 않는 문제를 해결할 수 있다.
우선 공식 웹사이트를 보며 업데이트 상황과 변화를 확인하기.
(http://neutronx.github.io/django-markdownx/)


*Python Package Index(PyPI) : 파이썬 패키지를 업로드하고 배포하는 공식 저장소.*
공식 문서에 github이랑 나오길래 뭔지 검색해봄.

문서 권고와 교재의 단계가 다르다.
교재에서는 없는 단계인
and, don't forget to collect MarkdownX assets to your STATIC_ROOT. To do this, run:
```
python3 manage.py collectstatic
```
이 존재함. 이 차이가 AI한테 물어보니 프로젝트에 있는 모든 정적 파일(static files)을 한 곳(STATIC_ROOT)으로 모으는 명령어인데, 교재는 개발환경(runserver)를 쓰니까 불필요했던 것으로 추정된다고.
내 settings.py에는 static_root는 없는데, 작성하면 생기나?

즉, 배포 직전에 하면 충분함. 나는 이건 생략하고 최종 단계에서 사용을 고민할 것.

**배포 고려한다면 나중에 이 명령어 하기.**

blog/models.py 수정하기
포스트 모델의 콘텐츠를 textfield 대신 markdownxfield로 바꾸기. 이렇게 되면 포스트의 본문이 마크다운이 됨.
오랜만이라 당황스럽긴 한데 모델 수정하면 migration 필수
form 문서에 {{form.media }}추가

위치가 
    </form>
    {{ form.media }}
위치가 예상 밖이긴 한데 교재와 문서 모두 동일하게 요구

교재를 보고 패키지를 적용하는 것도 좋지만, 실무를 고려하면 이번처럼 각 패키지의 공식 페이지를 보며 사용법을 따라가는 것이 더 좋을듯 하다.

이 컨텐츠 값을 html로 반환하는 작업이 필요함.
이게 왜 필요한지랑 문서에 없는데 어떻게 사용해야하는지가 의문이네.


## 33일차
마크다운 적용 이어서.

지난 작업 : 
- blog/models.py를 수정
- Post모델에 get_content_markdown 메서드를 추가한다.
- 이 메서드는 content 필드의 내용물(텍스트)을 마크다운 문법을 적용해 html로 만든다.

이번 작업 : 
- post_detail.html을 수정
- 기존 <p>{{ post.content }}</p>를 바꾼다.
- <p>{{ post.get_content_markdown }}</p>
- html이스케이핑 방지용 필터 추가 (" | safe")

이상으로 포스트 상세페이지 마크다운 출력 성공

- post_list.html 수정
- 기존 <p class="card-text">{{ post_list.0.content }}</p> 와 <p class="card-text">{{ p.content | truncatewords:15}}</p> 수정.
- <p class="card-text">{{ p.content | truncatewords:50}}도.
- 후자는 {{ p.get_content_markdown | truncatewords_html : 숫자 | safe }}로
- 전자는 {{ p.get_content_markdown | safe }}로.
- 그 후, 교재 원문과 내 아이디어로 달라진 디자인에 적합한지 재확인.
- 각각 최신포스트, 헤드이미지 없는 일반포스트, 헤드이미지 있는 일반포스트.

결과 : 출력 시 일부에 무의미한 <p>태그 장착됨.
태그 입력 기능의 폼 코드를 문장 내에 작성했는데 실제 출력에서 코드가 아닌 태그 형태로 출력되는 현상.

{{ p.content | truncatewords:50}} 수정하며 safe 안 붙인 것 확인. 이를 수정함. : <p> 태그 등 사라짐.

실제 태그 입력폼이 출력되는 문제는?




현재 문제 분석
1. 포스트 내에 html 코드가 일부 삽입되었는데, 해당 코드가 해석되어 작동
2. &lt;등 html 엔티티가 삽입되었을 때, ``` 로 코드블럭을 생성하면 <등 기호 대신 &lt의 원문으로 출력된다. 하지만, 위의 html 코드에는 코드블럭이 안된다.
3. AI 에 현재 상황을 물어본 결과, 현재 구조 자체가 코드와 텍스트 혼합에 취약하다고. markdownx필터를 더 권장한다고 함.

문서가 잘 안읽혀.
우선 markdownx 필터를 테스트로 사용해보고, 문서에서 구체적인 정보를 추가로 찾자. 

## 34일차
markdownx필터 사용하자니 load하기 번거롭고 정상 작동 안함.
markdown 함수 대신 markdownify함수 사용하는 방식 선택.

포스트 리스트에서 일부 카드와 footer등이 다른 카드 안에 속하게 되는 문제 발생.
> 원인 : 포스트 내에 작성된 <tr>등으로 대표되는 일부 html 코드.
포스트를 수정하여 내용을 삭제하자 복구됨.

하지만 이런 문제를 방조할 수 없음. 결국 '포스트에 실제 html 태그를 작성하면 안됨.'을 요구할 게 아니라면 고쳐야 해.
어떻게 해야 하지?

AI 권장 : bleach 사용해서 마크다운에서 html을 일부 혹은 전부 차단하기.


## 35일차
bleach install
def get_content_markdown(self):
    html = markdownify(self.content)
    return bleach.clean(html, tags=[], strip=True)


결과 : html은 제거되고 텍스트만 남는다. 줄바꿈 함께 제거됨.
return bleach.clean(html, tags=[], strip=True).replace('\n', '<br>')
이걸로 엔터만 남겨두면?
결과 : 줄바꿈 정상 남음.

문제 : 우선 html을 없애는 게 아니라 문자열 형태로 이스케이프하고 싶음.
      그리고 줄바꿈은 유지하고
      마크다운 문법인 #이나 *만 남기기.
이해도 부족해서 일단 AI 내용 그대로 사용. 이제부터 분석해야 함.
```
import bleach
import html
from markdownx.utils import markdownify

def get_content_markdown(self):
    # 1. html 태그들을 텍스트로 변환(=이스케이프)
    #ex) <tr> -> &lt;tr&gt;
    escaped_content = html.escape(self.content)

    # 2. 마크다운 렌더링.
    # 마크다운 문법(#, * 등)을 html로(=태그) 변환
    html_content = markdownify(escaped_content)

    # 3. 필요한 HTML만 허용(정제)
    # 마크다운 문법 적절한 것만 허용.
    allowed_tags = [
        'p', 'br',
        'strong', 'em',
        'h1', 'h2', 'h3',
        'ul', 'ol', 'li',
        'blockquote',
        'code', 'pre'
    ]

    cleaned = bleach.clean(
        html_content,
        tags=allowed_tags,
        strip=True
    )

    return cleaned
```

이 경우, 내가 원하는 기능을 내는 것은 bleach 없이도 html과 markdownx만으로 충분해 보인다.
그 후 다시 bleach하는 이유는 최종 html 전체를 검증하는 2차 보안.
여기서 문제가 되는 게 링크 기능과 이미지 기능
![이미지](javascript:alert(1)) -> <img src="javascript:alert(1)">
이미지가 로딩되면 스크립트 실행됨?
혹은 
[링크](http://example.com" onclick="alert(1)) -><a href="http://example.com" onclick="alert(1)">링크</a>
클릭하면 JS 실행됨.여튼 이런 게 처리 과정에서 작동되면 악용될 수 있고 보안을 위협할 수 있는듯.
실제 이 링크 기능 이용한 취약점
[외부](http://example.com)
<a href="http://example.com" target="_blank">


그래서 지금 버전은 '링크', '이미지', '테이블', '취소선', '체크리스트' 기능 삭제됨. + h4~6은 없음(# 1개~3개는 유지) + 가로선 없음.

이미지는 헤더 이미지 삽입이나 이미지 첨부 기능을 삽입했으니 필요 x.
링크는 같은 블로그 내 링크는 허용하고 싶은데.

일단 기능적으로는 가능해도 보안이나 대상 글 삭제시의 오류 등을 가늠하기 어려우니 링크는 패스.

Q : 체크리스트는 왜 통제하에 진행되어야 하지?
A : input 요소가 포함되기 때문에. html로 <li><input type="checkbox" checked> 완료</li>임. 그런데 여기서 input이 허용된다는게 위험함. 
<input type="checkbox" onclick="alert(1)"> 이런거 넣으면 바로 클릭시 JS실행되는 XSS 공격 발생.
<input type="checkbox" style="position:fixed; top:0; left:0; width:100vw; height:100vh;"> 이런걸로 UI를 망가뜨린다던가
당장은 markdown기능 한계상 막힌 부분이겠지만 나중에 확장되면 문제가 될 수 있다.
그래서 input의 type, checked속성만 허용하는 조건 + 추가적인 필터링 등으로 강한 통제를 하는 게 좋다.
내 개인 블로그가 아니라 외부 노출용 블로그니 체크리스트는 불필요할지도.

나머지는 가능.

* 나중에 프로젝트 1단계 마무리하고 오리지널 수정 들어가면 미리보기 부분도 수정하고싶음.



## 36일차

회원가입과 로그인 기능 추가하기

1. allauth 설치하기
2. setting.py, urls.py 수정해서 allauth 정보 및 설정 추가하기
  - installed_apps에 allauth 코어와 그 아래의 앱(account, socialaccount, socialaccount.providers.google)을 모두 각각 등록해줘야 한다.
  - django는 하나의 프로젝트가 여러 사이트를 운영 가능하기에 django.contrib.sites가 '지금 요청이 어느 사이트에서 왔는지 구분'해준다. allauth는 이메일 인증 링크, 로그인/회원가입 url 등을 생성하고 리다이렉트 url을 처리하는 데 이걸 사용.
  - site_id=1은 'id=1번 사이트를 현재 프로젝트로 사용한다는 뜻
  - settings에 이메일 검증 비활성화함. 향후 실사용에서는 검증 활성화해야 한다.
  
  - ACCOUNT_EMAIL_VERIFICATION = "optional" 로 할 것을 AI에게 추천받음.
3. 이 외부 라이브러리를 DB에 반영하기 위해 migrate 하기
4. '구글 개발자 콘솔'에 회원가입 및 프로젝트 생성.
  - 연결하면 구글 계정으로 로그인 가능.
  - 클라이언트 ID, 클라이언트 보안 비밀번호 -> github에 공개되는 여기 적지 말고 별도로 기록.
5. 로그인 버튼 활성화
6. 로그인 후 리다이렉트 기능
7. 로그인 후 유저네임과 로그아웃 버튼 표기
8. 커밋

## 37일차
2. setting.py, urls.py 수정해서 allauth 정보 및 설정 추가하기
  - urls.py에 path 추가.
3. 이 외부 라이브러리를 DB에 반영하기 위해 migrate 하기
  - migrate만 하면 됨.
  - 오류 발생. MIDDLEWARE에 AccountMiddleware를 추가해야 한다고 함. migrate 실패?
  - 해당 요구는 교재에는 없다.allauth의 버전 변화로 인한 것으로 추정됨.
  - 다시 실패. installed app에서 providers 부분을 임시로 주석처리하자 정상 해결됨.
4. '구글 개발자 콘솔'에 회원가입 및 프로젝트 생성.
  - 연결하면 구글 계정으로 로그인 가능.
  - 클라이언트 ID, 클라이언트 보안 비밀번호 -> github에 공개되는 여기 적지 말고 별도로 기록.
  - 이게 tangball264@gmail.com 로그인 깃헙에 저장되었으니 api 연결도 이 계정 사용.
  - 프로젝트 생성 / OAuth 동의 화면에서 기초 정보 입력 / OAuth 클라이언트 ID 생성(이건 별도로 폰에 저장)
  - 승인된 javascript 원본, 승인된 리디렉션 URl 항목 입력.
  - 생성하자 한 번 시크릿이 정상 출력 및 다운 안되어서 id 삭제하고 새로 생성.
  - 실제 실행 확인 시도
  - 실패. providers 활성화하자 아까 migrate오류처럼 의존성 오류 발생. pip install "django-allauth[socialaccount]" 으로 해결.
  - 실행 시, admin창에 sites, social accounts 항목이 생성됨.
  - site에 example.com 확인.로컬 서버 경로에 맞추어 수정.
5. 로그인 버튼 활성화
  - 로그인 버튼을 유지하고, 로그인 모달을 작성(94페이지). 라이브 모달 방식. 구글로 로그인, 구글로 회원가입, 이메일로 로그인, 이메일로 회원가입 총 4가지 버튼
  - 모달 내 버튼 배치를 위해 grid방식을 적용. 아이콘과 텍스트 배치 완료.
  - 관리자 페이지에서 social applications 에서 add social application하기. 내 클라이언트 id와 보안 비밀번호 입력하여 연결.
  - 정상 접속 확인. 그러나, 계정 선택 창으로 다이렉트로 이어지지 않고 중간에 확인 페이지를 거침. 
6. 로그인 후 리다이렉트 기능
  - 리다이렉트 페이지 accounts/profile/ 대신 포스트 리스트 페이지로 연결하기. setting에 login redirect url 설정 작성.
7. 로그인 후 유저네임과 로그아웃 버튼 표기
  - navbar.html 파일 수정. 
  - 로그아웃 기능 넣기
  - 로그인 모달 버튼 조정.
8. 커밋

## 38일차
폼으로 댓글 기능 구현하기

1. Comment 모델 추가
  - 댓글이 작성된 포스트, 댓글 작성자, 댓글 내용, 댓글의 작성 날짜와 수정일자.
  - __str__로 작성자와 내용을 반환
  - 향후 따로 포스트+댓글번호를 pk삼고 모델을 수정하여 댓글번호를 기준으로 하는 대댓글 기능 추가할수 있으려나.
2. 데이터베이스에 반영
  - makemigrations와 migrate 수행.
3. admin 수정
  - admin.site.regester(Comment)
4. 확인
  - admin에 정상적으로 추가됨. 작성 가능.
5. 포스트 상세 페이지 댓글 구조 확인
  - 댓글 작성 폼 한칸(완료 버튼 없음). 작성자프로필아이콘+작성자이름+내용 출력. 댓글과 대댓글 모두 존재.
  - 우리 댓글 구조상 댓글 아래 댓글을 작성하는 건 어려울 거 같은데. 이 기능은 삭제하고 나중에 추가하던가 해야 할듯.
  - comment-area 섹션, 각 코멘트에는 구분 없이 div.ms-3
6. 포스트 상세 페이지의 댓글 테스트코드 작성
7. 포스트 상세 페이지 html 수정(댓글 출력)
8. 테스트
9. admin에 view on site 만들어서 댓글 작성 시 바로가기.

## 39일차
간만에 복귀
지난번에 38일차에 정리한 할일 중 5까지 했고, 6부터?

6. 댓글 테스트코드 작성하기
- setUp 함수에 댓글 추가하기.
- test_post_detail함수에 comment 확인 내용 추가하기.
- 테스트코드에서 확인할 요소의 명칭이 교재와 내 코드가 일치하는가?
- 각 코멘트에 id='comment-1'이 없음. 이건 post_detail 수정하면서 넣어야 할듯. 

7. post_detail.html 수정
교재 내용
{% if post.comment_set.exists %} 
  {% for comment in post.comment_set.iterator %} 
    <div class="media md-4" id="comment-{{comment.pk}}"> 
      <img class="d-vlex mr-3 rounded-circle" src="http://placehold.it/50x50" alt=""> 
      <div class="media-body"> 
        <h5 class="mt-0">{{ comment.author.username }} &nbsp;&nbsp;<small class="text-muted">{{ comment.created_at }}</small> 
        </h5> 
        <p>{{ comment.content | linebreaks }}</p> 
      </div> 
    </div> 
  {% endfor %} 
{% endif %}

내 디자인에 맞추어 수정하려면

전후의 if, for는 유지
 for comment in post.comment_set.iterator -> 이터레이터 대신 all 사용을 권고받음. 이유와 특성 파악할것
 django 템플릿은 기본적으로 템플릿 엔진이 내부적으로 자동 번복 처리. 이거 안써도 반복 가능.
 하지만 실무적 관점에서 '수천 개의 댓글'쯤 되면 이터레이터를 쓰는 게 맞다.
 테스트하며 이터레이터를 유지할 때와 없앨 시를 비교해보고 차이를 확인할 것. 동일하다면 지울 생각.
id comment-1은 <div class="d-flex">에. mb-4도 함께 적용. 왜?
프로필 이미지 파트는 아직 안건들것.
댓글 내용은 ms-3 유지.
작성자 부분은 fw-bold 안에 넣는 것 유지. created_at부분은 교재것 따올것.
본문은 내 것은 별도로 태그 없음. 교재 따와서 p로.
 본문의 linebreaks의 의미 : 텍스트의 줄바꿈을 html로 변환해 <p><br> 자동 생성.
 p중복 -> 바깥에 p를 지우거나, linebreaksbr로 수정.

8. 테스트

테스트-실패
social account가 테스트에서 문제를 일으킴. 
{% get_providers as socialaccount_providers %}

{% if socialaccount_providers %}
<a role="button" class="btn btn-sm btn-outline-dark w-100"
   href="{% provider_login_url 'google' %}">
   <i class="fa-brands fa-google"></i> Log in with Google
</a>
{% endif %}
이걸로 provider가 실제 존재할 때에만 그 앱을 적용한 파트를 허용.

테스트-실패
comment-area가 div아니고 section

테스트-실패
로그인 모달의 타이틀(Login)이 카테고리 페이지, 태그 페이지의 타이틀보다 위에 위치해서 인식 오류. 
로그인 모달 타이틀을 h5로 수정.
실제 텍스트 크기에는 변동 없음.(사유 : 부트스트랩5 공식 모달 타이틀은 h5)

테스트-성공


9. admin에 view on site 만들어서 댓글 작성 시 바로가기.
models에서 comment모델에 get_absolute_url함수 추가
그 함수 출력은 post모델의 get_absolute_url + #comment-pk

문제 발생 : view on site하면 다른 것들도 http//주소 로 나옴.
http://으로 나와야 정상인데.

admin-site에서 Site 도메인을 http://127.0.0.1:8000에서 http://을 제거.
원래 django에서 http://을 제공하기에 중복으로 오류 날 수 있다고.
도메인 이름 : 127.0.0.1:8000
이후 정상 작동.

포스트, 댓글 모두 view on site 정상 작동 확인.
댓글 작성도 정상 작동.

**단, 댓글 작성 폼에 '입력'버튼 없음**
입력버튼 만들고, 로그인 상태에서만 보여지도록 수정할 것.

## 40일차
댓글 작성 폼 구현하기

1. 댓글 작성 폼을 위한 테스트 코드 작성
- 셋업 함수에 댓글이 하나 존재.
- 로그인하지 않은 상태 : 
  댓글 영역에서, Log in and leave a comment 문구를 확인하고, form이 없는것을 확인
- 로그인한 상태 : 
  로그인한다.
  Log in and leave a comment 문구가 없고, 대신 댓글 폼이 존재. 그 안에 textarea가 있다.
  새 댓글을 작성해 서버에 보내고, 결과를 받는다. 댓글 수가 늘어난다. 리다이렉트를 확인한다. 가져온 댓글의 내용과 저자가 일치한다.
2. 로그인 상태에 따라 댓글 입력란 또는 로그인 버튼 나타내기
- 교재 내용과 부트스트랩 버전이 다름. 그에 따른 변화를 확인해야 한다.
- runserver 결과 로그인 상태에서는 입력란과 submit 버튼이 보인다.
  그러나, submit 시도 시 오류가 나온다(page not found(404))
  The current path, blog/18/new_comment/, didn’t match any of these.
  사실상 댓글 입력란만 구현하고 댓글 폼 구현은 아직인 탓으로 추정.
  버전차이는 우선 댓글 폼 구현을 마치고 확인하며 조정해야 할  것.
- 추가적으로는 디자인 차이 등도 있음.
3. 댓글 폼 구현
- blog/forms.py 파일을 만들어 필드를 추가할 것.
- forms가 뭔지, 왜 쓰는건지 확인해야겠어. 특히, 이전에 다른데서 form 쓴거는 왜 이렇게 안했는지, 무슨 차이가 있는지도.
- views.py수정.
- html 수정 + crispy 적용
- urls.py 수정해 경로 추가. path('<int:pk>/new_comment/', views.new_comment),
- views.py 수정해 new_comment()함수 구현 -> 교재 오타 추정. 닫는 괄호 하나의 위치 잘못됨(479p)
4. 테스트
- comment-area가 div가 아닌 section이라 생긴 오류-수정 완료.
- 테스트 성공
5. 저장
저장에 앞서 runserver하며 버전 오차 수정하고 디자인 정돈하기.
실제 런서버 결과 오류 발생.

Forbidden (403)
CSRF verification failed. Request aborted.
Help
Reason given for failure:
    CSRF token missing.
You can customize this page using the CSRF_FAILURE_VIEW setting.
따라서 post_detail의 form-group 앞에 csrf_token 넣기.
수정 마치자 댓글 작성됨.


ModelForm 사용 시:
모델 구조와 자동 연동
유효성 검사 자동 처리
.save()로 바로 DB 저장 가능



부트스트랩 변화로 인한 수정 사항
1. form-group 제거됨. 해당 내용 제거하거나, mb-3 등으로 조정하기
>Dropped form-specific layout classes for our grid system. Use our grid and utilities instead of .form-group, .form-row, or .form-inline.
>
> https://getbootstrap.com/docs/5.0/migration/#forms
 
2. btn-block 삭제됨. w-100등으로 수정할 것.
>Dropped .btn-block for utilities. Instead of using .btn-block on the .btn, wrap your buttons with .d-grid and a .gap-* utility to space them as needed. Switch to responsive classes for even more control over them.
>
> https://getbootstrap.com/docs/5.0/migration/#buttons
3. data-toggle, data-target 등 JS속성 네이밍 변경됨. data-bs-toggle, data-bs-target 등으로 수정하기
>Data attributes for all JavaScript plugins are now namespaced to help distinguish Bootstrap functionality from third parties and your own code. For example, we use data-bs-toggle instead of data-toggle.
>
> https://getbootstrap.com/docs/5.0/migration/#javascript

위의 3가지 전부 수정
댓글창의 card-header 추가.
댓글 입력창 혹은 로그인 버튼이 댓글과 너무 붙음. <br>로 처리
폼 상하 길이 조정
폼의 라벨 제거

## 41일차
댓글 수정 기능 구현하기

댓글 수정 기능 정의
1. 댓글 옆의 '수정'버튼을 클릭하면 수정 가능하다.
2. 해당 댓글의 '내용'란을 comment-form으로 바꾸고, 그 안에 여전히 '내용'이 작성되어있게 한다.
3. 또한 '저장', '취소'버튼을 생성한다.
4. 수정 버튼은 '로그인'상태에서, 'author'=나 인 댓글에만 생성된다.

구현 과정
1. test_comment_update 작성.
2. html수정 : 수정 버튼, if 제한.
- 우측 배치를 위해 float-right를 float-end로 수정.
- 그러나 부트스트랩5는 float보다 flex를 권장한다.
```
<div class="d-flex justify-content-end">
    <a>수정</a>
</div>
```
으로 수정 예정.

3. 테스트
- error 발생. 오타와 지역변수-전역변수 오류(self 사용)등이 원인.
- test-OK
4. 배치 수정
- 교재 내용에 따라 author name위로 버튼 관련 내용 이동.
- 해당 상위 컨테이너에 ms-3이 적혀 있음. 이 경우 margin-start(끝쪽-margin-에서 시작)이기에 우측에서부터 배치.
- 이렇게 하자 작성일자의 일부(시간)이 공간 부족으로 아래로 줄바꿈되는 문제 발생.
- 하여 해당 컨테이너를 flexbox로 만들자 ms-3이 적용이 안되는 문제 발생.
- 최종적으로 상위 컨테이너였던 ms-3의 컨테이너 다음에 새 컨테이너를 배치하고, 그 안에 버튼 작성.
- 그러자 프사-본문(작성자, 날짜, 내용)-수정버튼 이 한 열에 놓임.
- 버튼의 컨테이너에 ms-auto를 주어 수정 버튼을 칸의 제일 오른쪽으로 밀어둠. (https://getbootstrap.com/docs/5.0/utilities/flex/#auto-margins)

결과적으로 적절하게 완료됨.
이후 다른 부분에서 쓴 float도 flex로 수정할 수 있을 듯. 교재 내용 완료하고 수정해보자.

## 42일차
댓글 수정 페이지 만들기

1. test코드 수정하기
2. urls.py에 페이지 경로 추가
3. views.py에 CommentUpdate 클래스 추가
4. comment_form.html 작성

test-ok.
저장.
다른 페이지로 이동하지 않고 하는 법은 나중에. 
대댓글 추가와 함께 github의 오픈소스를 사용해볼 생각.

## 43일차
댓글 삭제 기능 구현하기
1. 기획 : delete 버튼 + 재확인 모달
2. 테스트 코드 : 로그인 전에는 삭제 버튼이 없다. 로그인 후에는 버튼이 생기며, 이를 실행하여 모달과 삭제 기능을 확인한다.
- 완료. 단, 이번에도 용어와 문구 일부를 한글로 치환함.
3. 실제 삭제 버튼과 모달을 만든다.(post_detail.html수정)
- test-failed. line 481 오류. /blog/delete_comment/2/로 갈 수 없음.
4. urls.py, views.py 수정하기.
- 수정은 정상으로 했는데 urls에서 쉼표 까먹어서 오류 한번, 꺽쇠괄호 하나 빼먹어서 또 오류.
5. 최종 테스트
- test.py를 모두 완료했으니, 결과물이 시각적으로 내 기준과 예상에 맞는지 runserver로 확인
- 정상 삭제 확인



 updated 날짜 출력을 수정된 댓글에만 하기.
created_at은 auto_now_add고 modified_at은 auto_now임.
이에 따라 마이크로초 가량의 차이가 발생하고, 결과적으로 컴퓨터는 둘을 다르다고 인식.
```
{% if comment.created_at != comment.modified_at %} 
  <p class="text-muted float-end"><small>Updated: {{ comment.modified_at }}</small></p> 
{% endif %}
```
이 부분이 모든 댓글에서 작동한다.
auto_now_add는 생성 순간을 기록.
auto now는 save된 시점의 시간 기록.

그리고 views의 new_comment함수를 보면 commit=false상태로 한번 save하고 이후 한 번 더 save한다. 그리고 modelform.save도 있고, auto_naw의 차이도 있어서 내부에서는 미약한 차이가 발생.

따라서 이를 수정하기 위한 방법
1. is_edited로 수정 여부를 별도로 기록하고 이에 따라 업데이트 시점을 표기
- 장점 : 가장 정확하고 확장성 좋음.
- 단점 : 모델 변경 필요. 데이터와 로직의 분리.
2. created_at과 modified_at의 차이가 1초 이상일 때에만 updated time을 표시한다.
- 장점 : 모델 수정 없고 구현이 간단.
- 단점 : 정확도 조금 부족. 환경에 따라 결과 차이날수도.
3. created_at과 modified_at이 사용자에게 보이는 기준으로 동일하면 업데이트 표기.
- 장점 : 구현 간단하고 사용자 관점에서 자연스럽다.
- 단점 : 포맷에 의존하여 포맷 변경에 로직이 영향받을 수 있음. 작성 직후 수정시 표시 안될수도. 

1번으로 진행할 것.

1. models.py수정
- Comment 모델에 is_edited 필드를 추가한다.
- 이를 마이그레이션 한다(makemigrations, migrate)
2. views.py를 수정한다.
- form_valid함수를 추가로 오버라이드 한다.
- 그 안에서 is_edited를 true로 설정하고, 나머지는 super로 진행.

실제 runserver로 확인하자 정상 출력됨.
단, 기존에 수정한 것까지 바뀌는 건 아니고, 이제 새로 수정 해서 edited 수정하면.

## 44일차
기타 편의 기능 구현하기
1. 포스트 페이지 여러 개로 나누기
2. 검색 기능 구현
3. 사용자 아바타(프로필사진) 추가 및 출력

일단 포스트 페이지 분리부터.
포스트 리스트의 <!-- Pagination--> 파트에 관련 디자인 있음
필요한 것.
1. 포스트 개수별 필요 페이지 수 도출 기능(페이지당 출력 포스트 : 5)
2. 그에 맞추어 페이지네이션 숫자 조정
3. 현재 페이지 표시, 그에 맞추어 페이지 이동 숫자 조정
4. 페이지 이동 기능 추가. 그에 따라 다른 포스트가 출력이 되는지
* 최신 포스트는 넓게 출력되니까 2페이지부터는 6개 출력되게 조정할지
* 교재는 '이전 페이지', '다음 페이지' 뿐이니까 나는 숫자 페이지로 출력 괜찮은지 검토.

교재 내용
1. 포스트 추가
- 포스트를 추가하던 중, admin에서 포스트의 content를 작성할 때, 반응형 웹 기준으로 70~100% 범위 가량의 크기일 때 content의 textarea가 비정상적으로 커지는 문제 확인
- admin에만 markdownx를 끄는 방식으로 해결 가능할 것으로 추정.
```
#admin.py에 추가.
from django.db import models
from django import forms

class PostAdmin(admin.ModelAdmin):
    # MarkdownxField(또는 TextField)를 관리자 페이지에서만 일반 Textarea로 변경
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea},
    }

# 기존의 admin.site.register(Post) 대신 아래와 같이 등록
admin.site.unregister(Post) # 이미 등록되어 있다면 해제 후 다시 등록
admin.site.register(Post, PostAdmin)
# 이 코드를 이용해 특정 필드 타입의 위젯을 원하는대로 조정.
```
- 실패. 일단 수정 시도내용을 삭제
```
from .models import Post
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget
from django.db import models

class PostAdmin(MarkdownxModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget(attrs={'style': 'width:100%; min-height:500px;'})},
    }

admin.site.register(Post, PostAdmin)
```
- 이걸로 css를 수정. 기본 높이가 조금 긴 편이지만 포스트 특성상 길어도 되고, 글자 줄에 맞추어 적절히 늘어나는 것도 확인함.
- 그리고 포스트 개수는 충분하다.
2.views의 포스트리스트 클래스에서 paginate_by = 5 지정
(리스트뷰가 기본 제공하는 기능)
3. order, newer 버튼 구상/만들기
* 이 부분에서 내 것과 차이가 큼. 그리고 1페이지가 최신이니 두 버튼 위치도 조정할 것.
- 나는 <-, 1, 2, 3, 4, 5 ,-> 이정도로 구상중.
- 기능 수정. 예를들어 1페이지일때는 [1] 2 3 4 5 대신 [1] 2 3 만 나오고 2페이지면 1 [2] 3 4 이렇게. 
4. html의 pagenation 수정. listview가 제공하는 page_obj 이용.
- 일단 기본 기능으로 <<와 >>를 추가. 실제 이동이 되는 것을 확인. if문으로 이미1페이지, 마지막페이지일경우 disabled처리.
- 구현 : 현재 페이지 수에 따라 1페이지부터 for문으로 수행(num)
        num이 '현재페이지(=number)'-2보다 크고 +2보다 작으면 버튼을 만든다.
        이 때, num==number면 버튼을 active로 만든다.


## 45일차
44일차에 고려한 페이지 숫자 버튼 완성 및 저장.

검색 기능
1. 위젯-검색창에 검색하기.(검색 버튼 or enter키)
2. 자바스크립트를 사용하여 enter키를 인식.

3. base.html수정 : 검색 창 내용을 서버로 전달(onclick조건으로)
- widgets 사용하는 줄 알았더니, base에 중복으로 존재하고, 그 쪽을 사용하고 있었음. 
- 따라서 일단 base를 수정하고, 나중에 이를 widgets로 분리하는 작업을 수행할 것.

원본 템플릿
```html
<div class="input-group">
  <input class="form-control" type="text" placeholder="Enter search term..." aria-label="Enter search term..." aria-describedby="button-search" />
  <button class="btn btn-primary" id="button-search" type="button">Go!</button>
</div>
```
교재와 다른 부분 : 
1. input태그에 aria-속성들로 시각장애인을 위한 정보를 제공(스크린 리더 기능) 없어도 되지만 있는 게 표준적.
2. input 태그에 구 표준인 XHTML/XML을 엄격히 적용하여 닫기 슬래시/를 붙임. 현 표준인 HTML5는 안 붙여도 인식하므로 지워도 됨. 나는 지금까지 내용의 통일성을 위해 지우기로 함.
3. span 태그가 없음. 교재엔 버튼 그룹인 span태그가 있는데, 현 부트스트랩에선 버튼 그룹이 사라졌으므로 없음.
4. 버튼 태그 id. 교재에는 없음. 삭제할 이유가 없어 그대로 유지할 것. 
5. 버튼 태그의 클래스가 세컨더리가 아니라 프라이머리 디자인 사용.

교재를 따라 이제 추가하는 부분 :
1. 인풋 태그의 id. input요소 안의 값을 가져와 검색하기 위해 search-input이라는 id를 부여.
2. button을 클릭하면 검색 창 내용을 서버로 전달하기 위해 onclick="searchPost();"를 추가.
3. 그리고 script 태그 안에 자바스크립트 함수 searchPost()를 작성한다.
- 함수 내용 : id가 search-input인 태그(입력창)의 안에 있는 값(value)를 앞뒤 공백 등을 제거하고(trim) 텍스트만 받아오기.
그리고 그 길이가 1자면 검색어가 짧다는 알림.
1자 초과시 location.href="블로그/서치/검색어/"로 주소 들어가기. 

*location.href : 현재 웹 브라우저의 주소창에 입력된 url을 가리킴. 여기에 새 주소를 대입하면 그 주소로 바로 이동. a href로 지시하는것과 같은 기능인데 자바스크립트에서 하는 법.*

검색어 길이 검사가 정상적으로 작동한다.

제대로 된 검색어로 다시 검색을 시도하면, 해당 주소가 아직 없기 때문에 성공적으로 오류 발생.

4. 자바스크립트 수정. enter로도 동일한 작동을 하도록.
5. 테스트코드 작성.
6. urls.py수정 및 views.py수정.


## 46일차
views에 들어가는 Q관련해서 조사하다가 45일차 끝남.

7. 테스트하기
- failed

>    self.assertIn('Search : 파이썬 (2)', main_area.text)
>
>                                       ^^^^^^^^^^^^^^
>
> AttributeError: 'NoneType' object has no attribute 'text'

html에 이 부분 출력을 아직 구현 안함.

search-info를 값으로 넘겨 받아 사용할 수 있게 하기.

h1 부분을 수정하여 삽입.

- failed
- 추가 오류 발견. 큰 오류가 아니라 자잘한 오타나 ''위치 실수 등. 수정함.


그래서 runserver로 테스트 플레이 했는데 정상적으로 나옴.

교재의 요구는 완료.

다만 검색어에 /를 붙이면 /가 주소의 일부로 인지되어서 404 not found 오류 발생. 이 부분을 해결해둬야 할 듯.


방법1 : encodeURIComponent()를 이용하여 searchValue의 특수문자를 특수 기호 코드로 인코딩.

결과  : 실패. 자동으로 다시 디코딩된 것으로 추정.

방법2 : url의 path를 <str:q>에서 <path:q>로 수정.

결과 : 성공.

커밋


사용자 아바타 보여주기
-> 개인 프로필 사진 출력

구글 로그인 시 구글의 아바타 이미지 출력. 이메일 로그인 시 식별 가능한 고유 아바타 출력.

단계
1. Comment 모델 수정 : get_avater_url함수 작성하기(일단 소셜 로그인 시만 설정.)
2. post_detail.html에서 출력 아바타를 get_avater_url사용히게 수정
3. 이메일 로그인에 회색 아바타 대신 고유 이미지 추가
- 외부에서 제공하는 서비스 사용
- 교재에서는 저자가 서비스 제공(doitdjango.com)
- 제공하는 사이트 들어가 이메일 주소에 따라 제공되는 랜덤아바타 확인. 이를 get_avater_url에 적용.
4. 로그인 시 navbar에 아바타 보여주기. navbar.html수정하여 추가.
5. 커밋

2까지 하고 확인
실패. alt가 나옴. 오탈자 세개. 수정 후 확인. 정상 출력.

내부 계정 테스트. 회색 정상적으로 나옴.

저자가 제공하는 사이트를 통해 avater api사이트를 이용이 가능한가?

서버의 보안 인증서가 279일 전에 만료되어 서버가 doitdjango.com임을 입증할 수 없습니다. 설정이 잘못되었거나 공격자가 연결을 가로채고 있기 때문일 수 있습니다. 현재 컴퓨터의 시간이 2026년 5월 21일 목요일로 설정되어 있습니다. 시간이 정확하지 않으면 시스템 시간을 수정하고 이 페이지를 새로고침하세요.

이에 따라 보안 경고가 뜸. 따라서 현재 사용가능한 아바타 api를 찾아 적용하기.

후보
1. unavatar.io : 무료도 0원 결재를 연결해두어야 하는 불편함. 그 외에는 기능상 좋아보임
2. Gravatar : 글로벌 프로필 이미지 통합 서비스. 사용자가 자기 이메일과 프사를 사전 등록 필요.
3. UI Avatars : 닉네임 이니셜로 간단한 텍스트형 프사 만드는 서비스. 회원가입/패키지 설치 불필요한 간단한 방식.
4. Dicebear : 닉네임, 이메일, id등으로 그래픽 일러스트 생성. 다양한 스타일의 이미지.

UI Avatars 사용할 것.

적용 완료. 한국어 사용 편의를 위해 한글자만. 컬러 랜덤이 새로고침마다 바뀔지 걱정했는데, 다행히 한 유저는 하나로 고정되는 것 같다. 

로그인 시 navbar에 출력.

완료됨. 마찬가지로 동일 컬러 유지 확인됨.


향후 유저 아바타를 회원정보안에 포함하는 방향성을 고려.

장점은 쿼리 생략의 이점과 회원들의 프사 변경 기능으로의 확장 가능성 등.

단점은 서비스 유연성 저하? 랑 회원정보 변경시 함께 아바타 업데이트 해주는 로직 등 필요.
+ 이미지 저장으로 인한 용량 저하.

## 47일차
대문 페이지 완성하기

싱글 페이지 앱으로 분리해 둔 부분. 

1. landing.html 꾸미기(부트스트랩, 자바스크립트 사용)
- blog/navbar.html을 include
- navbar가 '현재 페이지 표시' 못하는 중. 수정.
2. 부트스트랩 적용 확인
3. landing.css파일 추가 + 이미지 추가 -> 모양 다듬기

현재 페이지 표시 기능 만듦. 구체적 코드는 ai 참고해서.
footer표시.

## 48일차
한동안 집중 어려움.
landing.html에 적용할 자바스크립트 + bootstrap은 이제부터 해야 함. 로그인 버튼이 안 눌리는 것 확인.

1. 부트스트랩 연결 성공 : 교재 코드 그대로 가도 됨.static/blog는 추가로 안해도 경로 전에 static 있으니 인식된다.  오히려 static 넣었다가 부트스트랩 다 풀리고 엉망.
2. 폰트어썸 연결 : blog/base거 그대로 복사해옴.
3. js연결 : 이것도 버전 변하면서 필요량이 줄어들었다. j쿼리 어쩌고 하는 줄 빼고, jsdeliever인가랑 부트스트랩 js. 결과적으로 각종 기호 정상 출력됨.

다음 단계는 css추가와 이미지 삽입.

## 49일차

landing.css 추가하고 이미지 추가해서 모양 다듬기.

문제 : landing과 blog 페이지의 navbar가 다름.
css문제인가?

## 50일차
소개글과 디자인 수정하기.
- 글의 배치나 간격, 패딩 등. -> div class로 묶어서 해결.

대문에 최신 포스트 나타내기
- landing.html에 카드 추가.

Blog - 최근 게시글
포스트 제목 1
포스트 제목 2


여기에 추가로 하고 싶은 기능은 최근 게시글 카드를 클릭해 해당 포스트로 바로가기 기능.


## 51일차
최신 포스트 테스트 코드 작성하기
1. 테스트 코드 작성(TestView클래스의 setUp과 test_landing
2. views에서 landing을 수정해 recent_posts를 보내기.
3. html에서 받아 보이기.
- 부트스트랩 버전 변경에 따라 수정하기.
- 오류 발생. 정상적으로 출력 안됨.
- 버전 변경에 따른 수정에서 일부 누락됨. badge 부분 내용 수정
badge badge-pill badge-light float-right -> badge rounded-pill bg-light text-dark float-end
round로 오타 + text-dark 누락 등 일부 문제 발견 및 해결

test-ok


이후 추가하고 싶은 것
- 링크를 title이 아닌 card 전체에 걸기.


다음 단계

작성자의 아바타 추가하기 + 카드 배경 흐리게.
- blog/models.py에서 post모델에 comment모델에 쓴 get_avatar_url()함수를 복붙
- landing.html을 수정하여 이미지 넣기
- landing.css를 수정하여 card요소의 투명도(alpha) 조정.

## 52일차

get_avatar_url 함수 옮기기
landing.html수정

## 53일차
요 며칠 얼마 못해서 오늘은 집중하기.

포스트 카드 투명도 추가(landing.css 카드 rgba 255, 255, 255, 0.6 조정.)
-> 작동 안함.
-> 사유 : 이전 landing.html에서 ai 수정안으로 card class에 bg-white를 추가했었음.
해당 부분 삭제하자 정상적으로 작동하는 것 확인.

커밋

페이지의 navbar가 landing과 blog에서 약간 좌우로 움직임. 
-> 사유 : 옆에 스크롤 바가 없으면 총 면적이 달라서 배치상 차이가 발생함.
```
/* 두 페이지 간 스크롤바 유무로 인한 가로 위치 튐 현상 방지 */
html {
    overflow-y: scroll;
}
```
이와 같이 추가하자 정상적으로 작동.
```
html {
    scrollbar-gutter: stable;
} 
```
이것으로도 동일한 효과가 나오는지 확인
두 방법간에 출력상 차이는 없다
그러나 전자는 움직이지 않는'스크롤바'가 생기고, 후자는 '스크롤 바가 될 수 있는 공간'이 여백으로 미리 할당되어있는 상태.

커밋

자기소개 페이지 완성하기
1. 레이아웃 구성하기(about_me.html 수정)
2. about_me.css 파일 만들기
3. 자기소개 내용 추가
4. 포폴 섹션 내용 추가

## 54일차
레이아웃 구성
- 파비콘 및 내용 없는 메타 데이터 입력 태그 주석 처리(다른 html에도 불필요한 부분 주석 처리해야.)
- bootstrap.min.css파일과 about_me.css파일 링크 연결.
- 폰트어썸 연결 스크립트 태그 추가.
- navbar 연결
- 소개글 섹션(이미지 포함)과 포트폴리오 섹션 구분
- footer추가
- 포폴 섹션에 margin-for-footer 추가

about_me.css파일 생성
- css로 margin-bottom추가.

- 교재 버전은 landing과 about_me모두 푸터에 fixed-bottom을 부여함. -> 하지만 aboutme에서는 blog와 같은 방식이어도 괜찮을 것 같아서 고민된다.

자기소개 내용 추가
- 기존에 추가해둔 이력 데이터를 자기소개와 포폴로 분리해서 작성해야 함.
    <h2>이력</h2>
    <h3>제주대학교 졸업(2025.8)</h3>
    <h2>활동</h2>
    <h3>TOPCIT 시험 참여(422/1000점)</h3>
    <h3>TOPCIT 시험 참여(550/1000점 -상위 30%)</h3>
    <h3>공무원연금공단 강의 및 견학 프로그램 참여</h3>
    <h3>정보처리기사 자격증 취득</h3>
    <h3>Django 블로그 만들기(교재 참고)</h3>
    <h3>AICE Associate자격증 취득 도전</h3>
  제대 졸업과 학과 정보는 자기소개에
  취득 자격증도 여기
  토익 성적 정도만 간단히.(topcit은 성적받으려 본 게 아니니 빼자.)
  포폴에서는 내가 진행한 이 프로젝트. + 그 외에 학생 때 진행해본 프로젝트 간략 소개.

## 55일차
포폴 섹션 카드랑 내용 추가.
1은 지금 진행중인것
2는 학교에서 한 버스승차앱
3은 모바일게임 제작 팀플
간략하게 적었음.

향후 카드와 이미지의 길이 조절 필요.

다음 단계
모달 작성.(card의 모달id도 작성.)
위에 포폴 카드에 작성한 상세 활동 내역도 모달로 이동.

모달 파트는 상세 내용이 교재에 없고 github참고를 권고.
<div class="modal fade" id="pycon2017" tabindex="-1" role="dialog" aria-labelledby="pycon2017ModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="pycon2017ModalLabel">파이썬으로 통계업무 자동화하기</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <div class="row">
                    <div class="col-lg-7">
                        <img class="img-fluid" src="{% static 'single_pages/images/pycon_sy_2017.png' %}">
                    </div>
                    <div class="col-lg-5">
                        <p>Python, Django, Pandas, python-docx로 통계업무 자동화한 내용을 파이콘에서 발표했습니다.</p>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
        </div>
    </div>
</div>
따라서 위 코드를 복붙 후 수정할 것.

## 56일차
위 모달 코드 복붙 후 모달 id 등과 내용 수정.
추가로 data-dismiss는 현행 버전상 data-bs-dismiss로 수정.

삽입할 이미지 있으면 좋겠음.

일단은 현재 프로젝트만 적당히 캡쳐하고 나머지는 생략.

55일차에 말한 포폴 카드 사이즈 조절 시작.
AI활용.

문제
1. 이미지 크기가 제각각임.
2. 글자 길이도 제각각임.

이를 수정하기 위해서
1. 이미지들에 pf-card-img 클래스를 부여하고, css파일에서 크기와 배치 등을 조정한다.
2. card div에 class h-100을 추가.(그리고 col-lg-4대신 col을 쓰고, 대신 그 상위의 row에 div class="row row-cols-1 row-cols-lg-3 g-4">로 전가.)

각 역할 설명.
1. css에서 각 이미지의 가로와 세로 사이즈를 강제한다. height:200px, width:100%
2. 또한 사이즈에 맞추어 이미지가 스케일링되도록 한다. object-fit: contain;(cover로 하면 사이즈 맞춰서 이미지 잘림.)
3. 그리고 이미지를 가운데정렬한다. object-position: center;
4. html에서 카드의 분할을 부모 row에게 넘김으로써, flexbox매커니즘에 따르게 됨. 높이 동기화 위한 기초 환경 생성.
5. h-100클래스 추가. 카드 세로 높이는 그 부모인 col을 100% 채운다. 이렇게 하면 카드 세로 길이가 모두 가장 긴 쪽에 맞추어진다.
-> 이 때, 4에 해당하는 부분을 생략하면 어떻게 될까? : 의외로 정상 작동함. 하지만 ai주장에 따르면 향후 오류의 여지가 있고, 테스트 결과 모바일 사이즈에서 카드간의 상하 간격이 지나치게 붙는 등 시각적 차이가 발생하기 때문에, 생략하지 않고 진행하기로 함.

그 다음
모달에 github링크 연결.
원본에서 사용한 형식 찾기
-> button + 그 안에 icon사용.
아이콘을 깃헙 아이콘으로 변경. 그리고 링크 연결을 위해 button대신 a태그에 클래스가 btn
 target="_blank" rel="noopener noreferrer" 을 추가해 '새 탭에서 열기' + target사용시 필요한 '보안 기능'적용
>공식 문서 정보 : 
>참고 : target을 사용할 때, rel="noreferrer"를 추가해 window.opener API의 악의적인 사용을 방지하는걸 고려하세요.
>참고 : 최근의 브라우저(Firefox 79+ 등)에서는 target="_blank"를 지정하면 rel="noopener"를 적용한 것과 같은 동작을 합니다.

링크 연결 정상 진행을 확인하고, 저장소를 공개로 전환하여 실제 연결 성공.

커밋


다음 단계는 배포.
배포하는 방법
1. 가상화 사용 여부 확인
가상화개론 했던 노트북이니 당연히 가능할 것.
맥북은 윈도우와 달리 가상화 기능이 상시 on이고 끌 수 없다고 함.
2. 도커 사용
재학 중 다운받은 도커 도로 삭제했었음. 재설치
가상환경에서도 도커가 정상적으로 인식됨.

이제 도커를 이용해보자. -> 내 파일들을 도커로 이사시키자!
1. 모듈 리스트 만들기
- 지금 가상환경에 설치해둔 라이브러리들을 도커로 옮겨야 함.
- 그러니 뭐뭐 옮겨야 하는지 리스트(=모듈 리스트)를 만들 것
- 방법 : pip freeze > requirements.txt
- pip freeze하면 출력되는 현재 설치된 라이브러리 이름과 그 버전 리스트를 지정한 txt파일에(없으면 만들어서) 적는다(cat)
- 이거 그대로 하면 현재 위치(django_web_app파일)에 이 txt파일 생성됨.
2. 도커 설정 파일 만들기
- 지금까지 프로젝트 진행해온 로컬 환경과 동일한 컨테이너 이미지를 만들기 위하여 '도커에도 똑같이 적용할 환경설정' 기록물 정도.
- 파일명은 기본적으로 'Dockerfile'로 약속됨.(확장자 없음)
- 이를 프로젝트 폴터에 생성하고 지정된 내용을 작성.
- 지정된 내용 중 파이썬 버전에 대해서는 교재가 아닌 내 환경에 맞출 것.
- 내용 : 필요한 도커 이미지 불러오기(파이썬 설치됨) / 작업폴더 지정 / 파이썬 설정들 변경사항 / 모듈 리스트 설치하려면 필요한 거 설치 / 내 작업물 작업폴더로 옮기기 / 모듈리스트의 라이브러리 설치
3. 도커 컴포즈 파일 만들기
- 컨테이너 여러개를 한 번에 실행시키거나, 컨테이너 실행 시 옵션을 주는 등의 기능을 할 수 있음.
- 기본 파일명 : docker-compose.yml
- 일단은 간단하게 '실행'정도만.
- 내용 : 버전(현재는 생략가능) / 배포할 서비스는 : 서비스이름 : 빌드할 폴더/실행할 커맨드/로컬-도커 폴더 연결/사용포트/환경파일
4. settings.py 수정하고 개발환경 파일(.env.dev) 작성하기
- 기존 보안키(django가 기본 제공한 안전하지 않은(insecure) 보안키. 
- settings수정하고 .env.dev 만들어서 작성.
5. docker-compose build 명령어 실행.
- 실패. AI 주장으로는 '최신 버전에서 docker-compose 대신 docker compose ...로 바뀌었다.'
- https://docs.docker.com/compose/intro/history/
- https://docs.docker.com/compose/intro/compose-application-model/
- 컴포즈 파일 명칭도 compose.yml로 권장사항이 변경되었지만 기존 것도 사용가능.
- 나는 기존 것 유지.
- docker compose build 로 실행됨.
- 오류 : failed to solve: process "/bin/sh -c apk add postgresql-dev gcc python3-dev musl-dev slib-dev jpeg-dev" did not complete successfully: exit code: 1
- 도커 파일 중 해당 줄 오탈자로 오류 발생(slib->zlib수정함). 오타 수정해고 재시도.
- 완료됨
- docker compose up 실행.
- 정상 실행 확인. 127.0.0.1에서 접속 가능하고, control+c로 종료도 가능.
- 터미널로 docker compose up -d 입력해서 백그라운드에서 돌리기. 로그 안보여주지만 웹사이트는 정상 작동할 것.

## 57일차

터미널 키워드
>docker compose build : 이미지 만들기
>
>docker compose up : 컨테이너 실행
>
>docker compose up -d : 컨테이너 실행(백그라운드). 
>
>docker image ls : 도커 이미지 목록 보기
>
>docker container ls : 도커 컨테이너(실행중) 목록 보기
>
>docker compose exec web python manage.py test : web컨테이너에서 python manage.py test 명령을 실행
>
>docker compose down : 실행중인 컨테이너 종료

docker image ls하자 총 5개 이미지 확인. django_web_app-web 빼고는 기본 제공되는 관리용 이미지임.
container ls에서 django_web_app-web-1 컨테이너 확인.
테스트 명령 실행 : ok. 이게 컨테이너 실행중에만 가능한 명령인듯(컨테이너 이름도 필요하니까.)
down : 컨테이너 종료됨.
이후 container ls에서는 컨테이너 없음. image ls에서는 여전히 이미지 존재. 위의 '테스트 명령'에서는 service "web" is not running 으로 실패하는 것이 정상적으로 확인됨.

커밋

DB(PostgreSQL)사용하기
기존에는 장고 기본제공인 db.sqlite3 사용 -> 프로젝트 규모 확장 or 웹사이트 방문자 증가에 따라 성능 저하 위험.
오픈 소스로 활용 가능한 PostgreSQL 사용 권장.

사용법(도커 없을시)
1. 로컬 컴퓨터(내 맥북)에 PostgreSQL 설치
2. 서버에서 다시 설치/설정 작업
-> 그러나 도커 사용시 매우 단순화됨.

사용 설정 방법
1. compose파일 수정.
> depends_on 항목에 db 넣고, web과 나란히 db서비스를 추가.

## 58일차

db 적용 이어서.
지난번에 compose파일 수정 마쳤으니 settings.py와 .env.dev 수정.

settings.py
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```
이 부분에 디폴트 안쪽 내용을 대대적으로 수정.
엔진, 이름, 유저, 암호, 호스트, 포트 총 6줄.
전부 os.environ.get이용할 것.
기존에 있던 것도 활용하되 os.environ.get을 이용하네.
이 부분의 의미는 별도로 알아보면 좋을듯.

그리고.env.dev파일 업데이트. 위에서 지정한 SQL_이하생략 각각 지정해주기. 채우는 내용은 settings.py와compose파일의 것들로.

빌드=실행.
결과 : ERR_CONNECTION_RESET
교재에서 말한 페이지가 작동하지 않습니다랑 같은건가?

오류 찾아보기
db-1  | 2026-06-18 07:05:58.597 UTC [1] LOG:  database system is ready to accept connections
>따라서 db-1은 문제없이 작동.
web-1  | django.core.exceptions.ImproperlyConfigured: Error loading psycopg2 or psycopg module
>psycopg2혹은 psycopg모듈을 로딩하는 부분에서 오류 발생.

따라서 교재와 같은 오류고 같은 방식으로 해소할 수 있음을 확인
psycopg검색해보기
>The most popular PostgreSQL adapter for Python
>
>A complete implementation of the Python DB API 2.0 specification, built on top of the official PostgreSQL client library, with many extensions giving access to the full power of modern Python and PostgreSQL.

교재와 같이 pycopg2로 설치. 현재 가상환경에 pip install psycopg2
그리고 requirements.txt에 설치 결과를 반영.

다시 빌드-실행.
결과는 오류(programming error)나와야 정상이다.
실행 후 ProgrammingError at / 확인. 정상적으로 실패했다.

오류 원인 : 데이터베이스 테이블 없음
데이터베이스를 변경하고서 마이그레이션을 한 번도 하지 않아 DB테이블이 생성되지 않은 상태
따라서 web컨테이너에 접속하여 마이그레이션 한다.

터미널1
>docker compose up
터미널2(새로 튼다.)
>source venv/bin/activate (가상환경 실행)
>django_web_app % docker compose exec web python manage.py migrate
도커로 만든 web컨테이너에 접속해 python manage.py migrate를 실행.

기존 테스트용 포스트가 다 날아갔음.
관리자 계정과 기타 계정들도 존재하지 않게 됨.

새 관리자 계정 만들기
>docker compose exec web python manage.py createsuperuser
>james
>james@doitdjango.com
>비번은 이전과 같이

왜 로그인 시 email로 로그인만 뜨지?
구글로 로그인이 같이 떠야 하는데?

일단 테스트 결과
1. blog에서 로그인 가능. 단, modal에서 구글로 로그인/sign in버튼 사라짐.
2. blog에서 포스트 작성 및 댓글 작성 가능.
3. admin에서 포스트 작성 가능. view on site 연결 안됨.
4. site를 example.com에서 127.0.0.1:8000으로 수정한 후 연결됨.
5. 컨테이너 껐다 켜도 데이터 유지됨.
6. 그러나, 여전히 구글로그인 기능 적용 안됨.

## 59일차

장고 명령어 runserver대신 전문적인 웹 서버 소프트웨어를 이용해 웹 사이트를 실행하기.

즉, nginx 사용
+ 장고와 nginx연결을 위해 gunicorn사용


1. 컴포즈 파일 command 변경 -> gunicorn으로
```
gunicorn do_it_django_prj.wsgi:application --bind 0.0.0.0:8000
```
2. pip로 gunicorn설치 + requirements 업데이트 + 이미지 빌드(와 실행까지 연속으로)
- 실제 빌드+실행결과 작동 안함.
- 사유는 do_it_django_prj라는 모듈이 없기 때문에.
- 이 모듈명이 settings에 있는 것으로 확인됨.(github에서 이 교재 파일 찾음)
- WSGI_APPLICATION = "django_web_app.wsgi.application"
- 따라서 나는 django_web_app.wsgi:application을 사용.
- 결과 : 
  1. 이미지 파일 로딩 안됨(단, blog-post_list에서 최신 포스트에 제공한 무작위 이미지 제외)
  2. 일부 아이콘 로딩 안됨(예를 들어, 태그 아이콘 중 하나는 로딩되고 하나는 안됨.)->이건 최신 포스트와 그 외 포스트 카드 양식에서 사용한 태그 아이콘이 달라서 생긴 문제로 추정. 통일함.
  3. 일부 css설정 적용 안됨.(ex, 싱글 페이지의 fixed되고 margin주어진 footer부분이 기능 적용 안되어서 포트폴리오 카드 일부를 가리는 등)
  4. 교재와 달리 일부는 적용됨(bootstrap 쪽 css는 정상 적용된듯?)
3. settings.py의 STATIC_ROOT경로 지정.(STATIC_ROOT = os.path.join(BASE_DIR, '_static'))
4. urls.py에서도 이것이 처리되도록 urlpatterns 추가문을 작성.(
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
5. 명령어 python manage.py collectstatic으로 스태틱 파일을 복사함.(신규 static폴더 생성해서 거기에 모든 스태틱 복사)
6. 새로 빌드.
- 정상적으로 로딩되는 것 확인함.
- 단, 일부 aboutme이미지 등 재업 시 어떻게 처리될지 알 수 없다.

그리고 github에 커밋