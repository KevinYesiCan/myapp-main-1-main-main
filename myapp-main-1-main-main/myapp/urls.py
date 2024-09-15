from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('movie/<int:id>/', views.toppick, name='toppick'),
    path('coming-soon/<int:id>/', views.coming_soon_detail, name='coming_soon_detail'),
    path('celebrity/<int:id>/', views.celebrity_detail, name='celebrity_detail'),
    path('news/<int:id>/', views.news_detail, name='news_detail'),
]
