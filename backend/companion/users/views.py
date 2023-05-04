from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Profile
from .serializers import ProfileSerializer

class ProfileListAPI(viewsets.ModelViewSet):
    model = Profile
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]