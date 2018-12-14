from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url, include
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'ordenes', views.OTViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
	path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')), 
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path(r'', include('app.urls')),
	path('', include('pwa.urls')),
]