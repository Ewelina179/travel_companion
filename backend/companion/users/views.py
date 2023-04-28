from rest_framework import viewsets

from .models import Profile
from .serializers import ProfileSerializer

class ProfileListAPI(viewsets.ModelViewSet):
    model = Profile
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()