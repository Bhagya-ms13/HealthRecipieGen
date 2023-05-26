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
    # preptime = forms.DecimalField(
        
    #     label='Add prep time in min',
    #     decimal_places= 0,

        
    # )
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
        fields = ['body', 'title','ingredients', 'diet', 'course']

