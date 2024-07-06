from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('auth/oauth', views.oauth, name='oauth'),
    path('game/schulte/save', views.schulte_save, name='schulte_save'),
    path('auth/login', views.login, name='login'),
    path('game/save_game_data', views.save_game_data, name='save_game_data'),
]