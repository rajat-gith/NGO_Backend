from rest_framework.decorators import api_view
from src import serializer
from src.models import Ngo
from src.serializer import NgoSerializer
from rest_framework.response import Response

@api_view(['GET'])
def getNgos(request):
    ngos=Ngo.objects.all()
    serializer=NgoSerializer(ngos,many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def getNgo(request,pk):
    ngo=Ngo.objects.get(_id=pk)
    serializer=NgoSerializer(ngo,many=False)
    return Response(serializer.data)

