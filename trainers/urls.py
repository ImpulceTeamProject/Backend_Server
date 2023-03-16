from rest_framework.routers import SimpleRouter
from .views import TrainerViewSet

trainers_router = SimpleRouter()

trainers_router.register(r'trainers', TrainerViewSet, basename='trainer')