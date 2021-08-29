from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from appointments import views

router = DefaultRouter()
router.register('', views.AppointmentViewSet)
app_name = 'appointments'
urlpatterns = [
    path('', include(router.urls))
]
