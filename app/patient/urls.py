from django.urls import path
from django.urls import include
from django.urls.resolvers import URLPattern
from rest_framework.routers import DefaultRouter
from patient import views

router = DefaultRouter()
router.register('', views.PatientViewSet)
app_name = 'patient'
urlpatterns = [
    path('', include(router.urls))
]
