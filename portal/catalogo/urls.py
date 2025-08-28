from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns =[
    path('', views.produto, name='lista'),
    path('categoria/<slug:categoria_slug>/',views.produto, name='por_categoria'),
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato', views.contato, name='contato')
]