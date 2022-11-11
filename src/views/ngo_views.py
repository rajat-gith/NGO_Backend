from rest_framework.decorators import api_view,permission_classes
from src import serializer
from src.models import Ngo
from src.serializer import NgoSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def addNgo(request):
    data=request.data
    ngoObject= Ngo.objects.create(
        name=data['name'],
        location=data['location'],
        desc=data['desc'],
        ngo_owner=data['ngo_owner'],
        tagline=data['tagline']
    )

    serializer=NgoSerializer(ngoObject,many=False)
    return Response(serializer.data)


