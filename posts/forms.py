from django import forms
from .models import Posts


class PostsForm(forms.ModelForm):

    class Meta:
        model = Posts
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Your Post Title'}),
        }