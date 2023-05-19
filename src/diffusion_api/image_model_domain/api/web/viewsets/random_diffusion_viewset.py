from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import JsonResponse

class RandomDiffusionViewset(viewsets.ViewSet):
    """
    A viewset for Random Diffusion API
    """

    @action(detail=True, methods=['post'])
    def initialize_diffusion(self, request):
        # user = self.get_object()
        # serializer = PasswordSerializer(data=request.DATA)
        # if serializer.is_valid():
        #     user.set_password(serializer.data['password'])
        #     user.save()
        #     return Response({'status': 'password set'})
        # else:
        #     return Response(serializer.errors,
        #                     status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(request.data, status=status.HTTP_200_OK)