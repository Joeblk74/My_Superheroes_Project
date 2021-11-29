from django.urls import path

from . import views

app_name = 'superheroes'
urlpatterns = [
    path('', views.hero_list, name='hero_list'),
    path('new', views.hero_create, name='hero_create'),
    path('<int:hero_id>/', views.hero_detail, name='hero_detail'),
    path('<int:hero_id>/edit', views.hero_edit, name='hero_edit'),
    path('<int:hero_id>/delete', views.hero_delete, name='hero_delete'),
]