from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):#Criando um modelo de formulario do meu banco de dados models
    class Meta:
        model = Comment#Meu bd
        fields = ['name', 'email', 'body']
        