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


