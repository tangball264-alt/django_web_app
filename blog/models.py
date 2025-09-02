from django.db import models

# Create your models here.
class Post(models.Model):#데이터베이스 테이블로 이 데이터들을 관리하겠다 -> models.Model
    title = models.CharField(max_length = 50)
    content = models.TextField()
    # auther = models.CharField(max_length=10) #이건 나중에 한대. 아직 작성자는 블로그 주인뿐이니까
    created_at = models.DateTimeField(auto_now_add=True) #필드가 생성될 때 한번만 현재시간 작성.
    changed_at = models.DateTimeField(auto_now=True) #필드 저장시마다 현재시간으로 갱신.

#admin에서 포스트 이름, 넘버 확인 편하게 하기 위해 str 함수 이용.
    def __str__(self): #str 함수 : 객체를 문자열로 표현할 때, 어떤 문자열로 보여줄 지 정할 수 있다. __str__(obj) 형식의 파이선의 특수 메서드(예약어)
        return f'[{self.pk}]{self.title}'#pk는 모델 생성시 붙는 각 레코드의 고유값. 일종의 인덱스나 포스트 생성 넘버로 이용.