from mysite.forms import CommentForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from mysite.models.post import Post

class PostView(generic.ListView):
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'index.html'

#class PostDetail(generic.DetailView):
#    model = Post
#    template_name = 'post_detail.html'


def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)#Vai procurar o post que vamos comentar para salvar o post
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        
        
        if comment_form.is_valid():
            
            #Create comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            
            #Assign the current post to the comment
            new_comment.post = post
            
            #Save the comment to the database
            new_comment.save()
            
    else:
        comment_form = CommentForm
        
    
    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )