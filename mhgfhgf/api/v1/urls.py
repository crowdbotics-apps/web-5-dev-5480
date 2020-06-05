from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FgfdngfdjViewSet

router = DefaultRouter()
router.register("fgfdngfdj", FgfdngfdjViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
