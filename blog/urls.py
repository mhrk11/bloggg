from django.urls import path
from .views import HomePageView, BlogPageView, BlogCreateView, BlogUpdate, BlogDelete

urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('blogpost/<int:pk>/', BlogPageView.as_view(), name='post_detail'),
    path('blogpost/new/', BlogCreateView.as_view(), name='post_new'),
    path('blogpost/<int:pk>/edit/', BlogUpdate.as_view(), name='post_edit'),
    path('blogpost/<int:pk>/delete/', BlogDelete.as_view(), name='post_delete'),
    ]


