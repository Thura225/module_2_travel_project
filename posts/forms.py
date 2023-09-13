from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    title = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','name':'title'}))
    content = forms.CharField(required=True,widget=forms.Textarea(attrs={'class':'form-control','name':'content','style':'height:136px;'}))
    image = forms.ImageField(required=False,widget=forms.FileInput(attrs={'class':'form-control','name':'image'}))
    class Meta:
        model = Posts
        fields = ['title','content','image']


class CommentForm(forms.Form):
    content = forms.CharField(label="Comment",required=True,widget=forms.Textarea(attrs={'class':'form-control','name':'comment','style':'height:100px;'}))