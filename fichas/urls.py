from django.urls import path

from fichas import views

app_name = "fichas"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:ficha_id>/', views.ficha_view, name='ficha'),
    path('<int:ficha_id>/experiencia', views.experiencia, name='experiencia'),
    path('nueva/', views.new, name='new'),
]
