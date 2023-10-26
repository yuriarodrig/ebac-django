from django.contrib import admin
from .models import post, agenda, Comment

class adminAgenda(admin.ModelAdmin):
    list_display = ["titulo", "local", "descricao", "data_agenda", "data_criacao"]
    list_filter = ["user", "local", "data_agenda"]


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "status", "created_on"]
    list_filter = ["status"]
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title", )}


@admin.register(Comment)#Ja consegue fazer o registro de comentario sem o admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "body", "post", "created_on", "active"]
    list_filter = ["active", "created_on"]
    search_fields = ["name", "email", "body"]
    actions = ["approve_comments"]


    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(agenda.Agenda, adminAgenda)
admin.site.register(post.Post, PostAdmin)