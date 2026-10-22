from django.urls import path
from . import views

app_name = "animais"

urlpatterns = [
    path('', views.renderizar_index, name='renderizar_index'),
    path('adotar/', views.renderizar_adotar, name='renderizar_adotar'),
    path('abrigar/', views.renderizar_abrigar, name='renderizar_abrigar'),
]
