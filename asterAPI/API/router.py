from rest_framework import routers
from .views import CdrViewSet

router = routers.DefaultRouter()
router.register(prefix='cdr', viewset=CdrViewSet, basename='Cdr')