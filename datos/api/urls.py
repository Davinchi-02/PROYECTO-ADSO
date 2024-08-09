from rest_framework import routers
from .api import UsuariosViewSet

router = routers.DefaultRouter()

router.register('api/usuario',UsuariosViewSet, 'usuario')

urlpatterns = router.urls