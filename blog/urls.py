from django.urls import path
from .views import HomePageView, BlogPageView, BlogCreateView

urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('blogpost/<int:pk>/', BlogPageView.as_view(), name='post_detail'),
    path('blogpost/new/', BlogCreateView.as_view(), name='post_new')
    ]
