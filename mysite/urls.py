from django.urls import path
from mysite import views

urlpatterns = [
    path("", views.PostView.as_view(), name="home"),
]
