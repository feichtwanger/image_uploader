from rest_framework import viewsets
from .models import Image
from .serializers import ImageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .tasks import process_image

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    @action(detail=True, methods=['post'])
    def start_processing(self, request, pk=None):
        image = self.get_object()
        process_image.delay(image.id)
        return Response({'status': 'processing started'})