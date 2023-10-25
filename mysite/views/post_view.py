from django.http import HttpResponse
from django.views import generic
from mysite.models.post import Post

class PostView(generic.ListView):
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
