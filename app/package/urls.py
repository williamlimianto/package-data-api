from django.urls import path, include
from rest_framework.routers import DefaultRouter

from package import views

router = DefaultRouter()
router.register('locations', views.LocationViewSet)

app_name = 'package'

urlpatterns = [
    path('', include(router.urls))
]
