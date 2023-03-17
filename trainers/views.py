from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Trainer
from .serializers import TrainerSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class TrainerViewSet(ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

