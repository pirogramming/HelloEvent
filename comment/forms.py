from django import forms
from .models import Comment, Recomment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text','comment_photo',]

        widgets = {
            'comment_text': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 80%', 'style': 'margin:0 auto',
                       'placeholder': '댓글을 입력하세요'}
            ),

        }
        labels = {
            'comment_text': '',
            'comment_photo': '',
        }

class RecommentForm(forms.ModelForm):
    class Meta:
        model = Recomment
        fields = ['recomment_text','recomment_photo',]
        
        widgets = {
            'recomment_text': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 80%', 'style': 'margin:0 auto',
                    'placeholder': '대댓글을 입력하세요'}
            ),

        }
        labels = {
            'recomment_text': '',
            'recomment_photo': '',
        }