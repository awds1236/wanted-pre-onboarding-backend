from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['post_title', 'post_content']  # 'post_image'를 추가하세요.
        
        widgets = {
            'post_title': forms.TextInput(
                attrs={
                    'id': 'post_title',
                    'placeholder': '제목을 입력하세요.'
                    }),
            'post_content': forms.TextInput(
                attrs={
                    'id': 'post_content',
                    'placeholder': '신고할 내용을 작성하세요.'
                    }),
        }

