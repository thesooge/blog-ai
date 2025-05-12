from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        labels = {
            'body': 'Comment',
        }
        help_texts = {
            'body': 'Enter your comment here.',
        }
        error_messages = {
            'body': {
                'required': 'This field is required.',
                'max_length': 'This field is too long.',
            },
        }