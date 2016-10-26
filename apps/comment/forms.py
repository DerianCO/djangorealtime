from django import forms
from apps.comment.models import Comment

class FormComment(forms.ModelForm):
    class Meta:
        model = Comment

        fields = [
            'author',
            'comment',
        ]

        labels = {
            'author' : 'author',
            'comment' : 'comment',
        }

        widgets = {
            'author' : forms.TextInput(),
            'comment' : forms.TextInput(),
        }
