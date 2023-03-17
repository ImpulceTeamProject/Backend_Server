from rest_framework import viewsets
from rest_framework.response import Response
from gallery.models import Photo
from .serializers import PhotoSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.
class PhotoViewSet(viewsets.ModelViewSet):
    """
    Этот класс представляет интерфейс для взаимодействия с фотографиями.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        """Получение списка фотографий"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """Создание фотографии"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        """Получение одной фотографии"""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
