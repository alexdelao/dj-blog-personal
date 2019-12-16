from django import forms 
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content','image',  'author',  'slug',]
        widgets = {
                'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titulo'}),
                'subtitle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'subtitulo'}),
                'content': forms.Textarea(attrs={'class':'form-control', 'rows': 3, 'placeholder':'Escribe tu mensaje'}), 
                'image': forms.ClearableFileInput(attrs={'class':'form-control'}),
                'author': forms.Select(attrs={'class':'form-control'}),
                'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'slug'})
            }