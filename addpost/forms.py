from django import forms
from .models import Blog


    
class BlogForm(forms.ModelForm):
    title = forms.CharField(
        
        label='',
        widget=forms.Textarea(attrs={
        'class' : 'blogtitle',
        'rows' : '1',
        'placeholder': 'Add Title'
        })
    )
    ingredients = forms.CharField(
        
        label='',
        widget=forms.Textarea(attrs={
        'class' : 'blogingred',
        'rows' : '9',
        'placeholder': 'Add Ingredients'
        })
    )
    preptime = forms.CharField(
        
        label='',
        widget=forms.Textarea(attrs={
        'class' : 'blogtime',
        'rows' : '2',
        'placeholder': 'Prep time in min'
        })
    )
    body = forms.CharField(
        
        label='',
        widget=forms.Textarea(attrs={
        'class' : 'blogcontent',
        'rows' : '15',
        'placeholder': 'Write about the process'
        })
    )
    
   

    class Meta:
        model = Blog
        fields = ['body', 'title']

