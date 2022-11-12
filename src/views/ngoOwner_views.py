from rest_framework.decorators import api_view
# from src import serializer
from src.serializer import OwnerSerializerWithToken,OwnerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from src.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = OwnerSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        print("attrs=>",attrs)

        return data


class MyTokenObtainPairViewOwner(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerOwner(request):
    data = request.data
    owner = Ngo_Owner.objects.create(
        first_name=data['name'],
        username=data['email'],
        email=data['email'],
        password=make_password(data['password'])
    )
    print((data['name']))
    serializer = OwnerSerializerWithToken(owner, many=False)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def getOwners(request):
    ngos=Ngo_Owner.objects.all()
    serializer=OwnerSerializer(ngos,many=True)
    return Response(serializer.data)

# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def updateOwnerProfile(request):
#     owner = request.owner
#     serializer = UserSerializerWithToken(owner, many=False)

#     data = request.data
#     owner.first_name = data['name']
#     owner.username = data['email']
#     owner.email = data['email']

#     if data['password'] != '':
#         owner.password = make_password(data['password'])

#     owner.save()
#     return Response(serializer.data)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getUserProfile(request):
#     user = request.user
#     serializer = UserSerializer(user, many=False)
#     return Response(serializer.data)



# @api_view(['DELETE'])
# @permission_classes([IsAdminUser])
# def deleteUser(request, pk):
#     userForDeletion = updateOwnerProfile.objects.get(id=pk)
#     userForDeletion.delete()
#     return Response('User was deleted')

