from django.shortcuts import render
from dogapi.models import Dog
from dogapi.models import Breed
from dogapi.serializers import DogSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

class BreedList(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = DogSerializer


class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = DogSerializer

class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

@api_view(['GET'])
def rest_get_dog(request, dog_id):
    try:
        dog = Dog.objects.get(pk=dog_id)
        serializer = DogSerializer(dog)
        return Response(serializer.data)
    except Dog.DoesNotExist:
        return Response({'error': 'Dog not found.'}, status=status.HTTP_404_NOT_FOUND)