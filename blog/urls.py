from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('finches/', views.Finches.as_view(), name='finches')
]