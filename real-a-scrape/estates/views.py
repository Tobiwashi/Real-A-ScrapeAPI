from django.http import JsonResponse
from .models import Estate
from .serializers import EstateSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def estate_list(request):

    estates = Estate.objects.all()
    serializer = EstateSerializer(estates, many=True)
    return JsonResponse({"estates": serializer.data}, safe=False)

