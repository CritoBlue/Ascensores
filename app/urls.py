from django.urls import path

from . import views

urlpatterns = [
    #path('', views.IndexView.as_view(), name='home'),
    path('', views.index, name='home'),
    path('base/', views.base, name='base'),
    path('cliente/', views.cliente, name='cliente'),
    path('orden/', views.orden, name='orden'),
]