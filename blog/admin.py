from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)
#이건 기본. post 모델을 관리자 페이지에서 그대로 볼 수 있음.
#class PostAdmin(admin.modeladmin) 해서 일부 데이터만 보이도록 할 수 있음.

