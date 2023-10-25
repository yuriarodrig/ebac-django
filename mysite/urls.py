from django.urls import path
from mysite.views.post_view import PostView, PostDetail
from mysite import views


urlpatterns = [
    path("", views.PostView.as_view(), name="home"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail")
]
