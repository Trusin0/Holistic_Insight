from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('auth/oauth', views.oauth, name='oauth'),
    path('auth/login', views.login, name='login'),
    path('auth/login_status', views.get_login_status, name='login_status'),
    path('game/save_game_data', views.save_game_data, name='save_game_data'),
    path('game/schulte/save', views.schulte_save, name='schulte_save'),
    path('check_session/', views.check_session, name='check_session'),
    path('plot/<str:test_type>/<int:user_id>/', views.plot_reaction_time, name='plot_test_data'),
]
