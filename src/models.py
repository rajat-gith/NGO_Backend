# from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class Ngo(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    name=models.CharField(max_length=200,null=True,blank=True)
    location=models.CharField(max_length=200,null=True,blank=True)
    desc=models.TextField(null=True,blank=True)
    ngo_owner=models.CharField(max_length=200,null=True,blank=True)
    startedAt=models.DateTimeField(auto_now_add=True)
    tagline=models.CharField(max_length=200,null=True,blank=True)
    contact=models.CharField(max_length=200,null=True,blank=True)

    
    def __str__(self):
        return self.name


class User(AbstractUser):
    # donor=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    dob=models.DateField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    city=models.CharField(max_length=200,blank=True,null=True)
    state=models.CharField(max_length=200,blank=True,null=True)
    pincode=models.IntegerField(blank=True,null=True)
    father_s_name=models.CharField(max_length=200,null=True,blank=True)
    mother_s_name=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.email


class Ngo_Owner(User):
    active=models.CharField(max_length=200,null=True,blank=True)
    def __int__(self):
        return self._id

class user_donation(models.Model):
    ngo_user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="ngo_donate")
    ngo_donated=models.ManyToManyField(Ngo,related_name="ngo_donated")
    ngo_member=models.ManyToManyField(Ngo,related_name="ngo_member")
    amount_donated=models.IntegerField(blank=True,null=True)
    _id=models.AutoField(primary_key=True,editable=False)
    
    def __str__(self):
        return str(self.ngo_user)
