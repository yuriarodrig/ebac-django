from django.contrib import admin

# Register your models here.
from .models import post, agenda

class adminAgenda(admin.ModelAdmin):
    list_display = ["titulo", "local", "descricao", "data_agenda", "data_criacao"]
    list_filter = ["user", "local", "data_agenda"]

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "status", "created_on"]
    list_filter = ["status"]
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title", )}
    
admin.site.register(agenda.Agenda, adminAgenda)
admin.site.register(post.Post, PostAdmin)