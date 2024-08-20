from .models import post
from rest_framework import viewsets,permissions
from .serializers import PubliSerializer
class PostViewSet(viewsets.ModelViewSet):
    queryset= post.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class = PubliSerializer