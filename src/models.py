from django.contrib.auth.models import User
from django.db import models

class Ngo(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    name=models.CharField(max_length=200,null=True,blank=True)
    location=models.CharField(max_length=200,null=True,blank=True)
    desc=models.TextField(null=True,blank=True)
    ngo_owner=models.CharField(max_length=200,null=True,blank=True)
    startedAt=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class donor(models.Model):
    donor=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    ngo_donated=models.ForeignKey(Ngo,on_delete=models.SET_NULL,null=True,related_name="donated")
    ngo_member=models.ForeignKey(Ngo,on_delete=models.SET_NULL,null=True,related_name="member")
    name=models.CharField(max_length=200,blank=True,null=True)
    dob=models.DateField(blank=True)
    address=models.TextField(null=True,blank=True)
    city=models.CharField(max_length=200,blank=True,null=True)
    state=models.CharField(max_length=200,blank=True,null=True)
    pincode=models.IntegerField(blank=True,null=True)
    amount_donated=models.IntegerField(blank=True,null=True)
    father_s_name=models.CharField(max_length=200,null=True,blank=True)
    mother_s_name=models.CharField(max_length=200,null=True,blank=True)
    donation_message=models.CharField(max_length=200,null=True,blank=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.name


    
