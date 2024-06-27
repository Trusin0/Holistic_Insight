from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('login/oauth', views.oauth, name='oauth'),
]