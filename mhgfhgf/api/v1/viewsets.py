from rest_framework import authentication
from mhgfhgf.models import Fgfdngfdj
from .serializers import FgfdngfdjSerializer
from rest_framework import viewsets


class FgfdngfdjViewSet(viewsets.ModelViewSet):
    serializer_class = FgfdngfdjSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Fgfdngfdj.objects.all()
