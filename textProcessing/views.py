from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from .serializers import Serializer
from .textProcessing import text_cleaned
from django.shortcuts import render

class API (views.APIView):
    def post(self, request):
        input = request.data
        data = text_cleaned(input)
        serializer = Serializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
