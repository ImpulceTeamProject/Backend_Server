from rest_framework.serializers import ModelSerializer
from .models import Trainer


class TrainerSerializer(ModelSerializer):
    class Meta:
        model = Trainer
        fields = ('id', 'name', 'surname', 'patronymic', 'date_of_birth', 'avatar', 'phone', 'email', 'vk_link', 'instagram_link', 'telegram_link')