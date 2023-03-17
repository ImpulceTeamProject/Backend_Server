from rest_framework.serializers import ModelSerializer
from .models import Photo


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'title', 'description', 'image', 'small_image', 'created_at', 'updated_at')