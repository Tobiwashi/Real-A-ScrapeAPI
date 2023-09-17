from django.http import JsonResponse
from rest_framework.response import Response
from .models import Estate
from .serializers import EstateSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST', 'DELETE'])
def estate_list(request):
    if request.method == 'GET':
        estates = Estate.objects.all()
        serializer = EstateSerializer(estates, many=True)
        return Response({"estates": serializer.data})
    if request.method == 'POST':
        serializer = EstateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        estates= Estate.objects.all()
        estates.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def estate_detail(request, id):
    
    estate = Estate.objects.get(pk=id)
    
    if request.method == "GET":
       serializer = EstateSerializer(estate) 
       return Response(serializer.data) 
    elif request.method == "PUT":
        serializer = EstateSerializer(estate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        estate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)