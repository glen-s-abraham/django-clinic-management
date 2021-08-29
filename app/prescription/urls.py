from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from prescription import views

router = DefaultRouter()
router.register('', views.PrescriptionViewSet)
app_name = 'prescription'
urlpatterns = [
    path('', include(router.urls))
]
