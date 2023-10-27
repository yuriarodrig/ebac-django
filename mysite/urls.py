from django.urls import path
from mysite.views.post_view import PostView, post_detail
from mysite import views


urlpatterns = [
    path("", views.PostView.as_view(), name="home"),
    #path("<slug:slug>/", post_detail.as_view(), name="post_detail")
    path("<slug:slug>/", views.post_detail, name="post_detail")
]
