import os
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):#데이터베이스 테이블로 이 데이터들을 관리하겠다 -> models.Model
    title = models.CharField(max_length = 50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) #현재는 '유저 삭제 시 포스트 함께 삭제.'
    created_at = models.DateTimeField(auto_now_add=True) #필드가 생성될 때 한번만 현재시간 작성.
    changed_at = models.DateTimeField(auto_now=True) #필드 저장시마다 현재시간으로 갱신.
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/',blank=True)#헤드 이미지. 이미지 필드를 사용. blog/images/연도(4자리)/월/일로 폴더 만들어 분류해 업로드. 안 올려도 됨.
    #%y는 2자리 연도. %M은 분. %D는 미국식 날짜(일/월/두자리 년도).
    attachment = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

#admin에서 포스트 이름, 넘버 확인 편하게 하기 위해 str 함수 이용.
    def __str__(self): #str 함수 : 객체를 문자열로 표현할 때, 어떤 문자열로 보여줄 지 정할 수 있다. __str__(obj) 형식의 파이선의 특수 메서드(예약어)
        return f'[{self.pk}]{self.title} :: {self.author}'#pk는 모델 생성시 붙는 각 레코드의 고유값. 일종의 인덱스나 포스트 생성 넘버로 이용.
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    #첨부파일 이름, 확장자 찾기
    def get_file_name(self):
        return os.path.basename(self.attachment.name)
    
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]