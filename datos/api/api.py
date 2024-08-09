from .models import usuarios
from rest_framework import viewsets,permissions
from .serializers import UsuarioSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = usuarios.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer