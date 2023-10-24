from django.db import  models
from django.contrib.auth.models import User

class Agenda(models.Model):
    
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    descricao = models.TextField(max_length=244, verbose_name="Descricao")
    
    data_criacao = models.DateField(auto_now_add=True, verbose_name="Data de Criação")
    data_agenda = models.DateTimeField(verbose_name="Data da Agenda")
    
    local = models.CharField(max_length=150, verbose_name="Local da Agenda")
    
    class Meta:
        ordering = ['-data_agenda']
        
    def __str__(self):
        return self.titulo