from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import JsonResponse
from image_model_domain.api.web.schemas import RandomDiffusionSchema

class RandomDiffusionViewset(viewsets.ViewSet):
    """
    A viewset for Random Diffusion API
    """

    @action(detail=True, methods=['post'])
    def initialize_diffusion(self, request, pk=None):
        try:
            data = request.data
            random_diffusion_schema = RandomDiffusionSchema()
            serialied_data = random_diffusion_schema.load(data)
            print(serialied_data)
            prompt_list = serialied_data.get('prompt_list')
            random_diffusion = RandomDiffusion(prompt_list)
            return JsonResponse({"Result": random_diffusion}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"Error Message": str(e)}, status=status.HTTP_400_BAD_REQUEST)