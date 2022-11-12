from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from src.models import *
import pdb

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id','_id', 'username', 'email', 'name', 'isAdmin','first_name','last_name','date_joined','dob',
                    'address','city','state','pincode','father_s_name','mother_s_name'
        ]

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        print("Object is=> ",obj.first_name)
        name = obj.first_name
        if name == '':
            name = obj.email

        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'isAdmin','first_name','last_name','date_joined','dob',
                    'address','city','state','pincode','father_s_name','mother_s_name','token'
                ]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class OwnerSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Ngo_Owner
        fields = ['_id', 'username', 'email', 'name']

    def get__id(self, obj):
        return obj.id

    def get_name(self, obj):
        print("Object is=> ",obj.first_name)
        name = obj.first_name
        if name == '':
            name = obj.email

        return name

class OwnerSerializerWithToken(OwnerSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Ngo_Owner
        fields = fields = ['_id', 'username', 'email', 'name','token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class NgoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ngo
        fields= '__all__'

    
class DonorSerializer(serializers.ModelSerializer):

    ngo_donated=NgoSerializer(many=True)
    ngo_member=NgoSerializer(many=True)
    ngo_user=UserSerializer(many=False)
    class Meta:
        model=user_donation
        fields="__all__"


        