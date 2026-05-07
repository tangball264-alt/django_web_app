from django.contrib import admin
from .models import Post, Category, Tag, Comment
from .models import Post
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget
from django.db import models

class PostAdmin(MarkdownxModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget(attrs={'style': 'width:100%; min-height:500px;'})},
    }

admin.site.register(Post, PostAdmin)

# Register your models here.

admin.site.register(Comment)
#이건 기본. post 모델을 관리자 페이지에서 그대로 볼 수 있음.
#class PostAdmin(admin.modeladmin) 해서 일부 데이터만 보이도록 할 수 있음.

#admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)} # slug값이 name 입력되면 자동으로 생성됨.

admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)} # slug값이 name 입력되면 자동으로 생성됨.

admin.site.register(Tag, TagAdmin)
