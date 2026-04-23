from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ('content',)
        # 혹은 exclude = ('post', 'author', 'created_at', 'modified_at',) 으로 입력받지 않을 필드를 고를 수도.
        labels = {
            'content': ''
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3})
        }