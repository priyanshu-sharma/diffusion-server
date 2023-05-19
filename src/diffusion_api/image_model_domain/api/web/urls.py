from rest_framework.routers import DefaultRouter
from django.urls import re_path, include
from image_model_domain.api.web.viewsets import RandomDiffusionViewset

router = DefaultRouter()
router.register(
    r"random_diffusion", RandomDiffusionViewset, basename="random_diffusion",
)

urlpatterns = [
    re_path("", include(router.urls)),
]
