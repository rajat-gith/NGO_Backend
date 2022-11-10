from rest_framework.decorators import api_view
# from src import serializer
from src.serializer import UserSerializer,UserSerializerWithToken,DonorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import responses
from src.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status
import pdb


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        print("attrs=>",attrs)

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):
    data = request.data
    print((data['name']))
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)

    data = request.data
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']

    if data['password'] != '':
        user.password = make_password(data['password'])

    user.save()
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    print("Serializer=>",serializer)
    return Response(serializer.data)

@api_view(['PUT'])
#@permission_classes([IsAuthenticated])
def updateUser(request, pk):
    user = User.objects.get(id=pk)

    data = request.data

    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    user.is_staff = data['isAdmin']

    user.save()

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request, pk):
    userForDeletion = User.objects.get(id=pk)
    userForDeletion.delete()
    return Response('User was deleted')

@api_view(['GET'])
def getDonors(request):
    user_donations = user_donation.objects.all()
    serializer = DonorSerializer(user_donations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getDonorInfo(request,pk):
    user_donations = user_donation.objects.get(_id=pk)
    serializer = DonorSerializer(user_donations, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registerDonorInfo(request):
    user=request.user
    # print(user)
    data=request.data
    # print(1)
    new_user_donation = user_donation.objects.create(
            ngo_user=user,
            amount_donated=data['amount'],   
    )
    # pdb.set_trace()
    for ngo_donated in data['ngo_donated']['_id']:
        print(ngo_donated)
        pdb.set_trace()
        ngo_donated_obj=Ngo.objects.get(_id=ngo_donated)
        new_user_donation.ngo_donated.add(ngo_donated_obj)
        print(ngo_donated)

    for ngo_member in data['ngo_member']['_id']:
        ngo_member_obj=Ngo.objects.get(_id=ngo_member)
        new_user_donation.ngo_member.add(ngo_member_obj)

    serializer = DonorSerializer(new_user_donation, many=False)
    return Response(serializer.data)
        