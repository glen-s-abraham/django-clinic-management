from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from diagnosis import views

router = DefaultRouter()
router.register('', views.DiagnosisViewSet)
app_name = 'diagnosis'
urlpatterns = [
    path('', include(router.urls))
]
