from django.urls import path
from rest_framework import routers

from .views import ProfileListAPI

profiles_router = routers.DefaultRouter()
profiles_router.register("profiles", viewset=ProfileListAPI, basename="profiles")

urlpatterns = [
    path('profiles/', ProfileListAPI.as_view({'get': 'list'}), name='profiles_list_view')
]