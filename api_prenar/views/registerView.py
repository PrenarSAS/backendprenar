from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_prenar.serializers.userSerializers import UserSerializer

class Register(APIView):
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

