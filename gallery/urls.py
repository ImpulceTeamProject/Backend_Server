from rest_framework import routers
from gallery.views import PhotoViewSet

photosRouter = routers.SimpleRouter()
photosRouter.register(r'photos', PhotoViewSet)