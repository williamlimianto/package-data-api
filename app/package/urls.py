from django.urls import path, include
from rest_framework.routers import DefaultRouter

from package import views

router = DefaultRouter()
router.register('locations', views.LocationViewSet)
router.register('organizations', views.OrganizationViewSet)
router.register('customers', views.CustomerViewSet)

app_name = 'package'

urlpatterns = [
    path('', include(router.urls))
]
