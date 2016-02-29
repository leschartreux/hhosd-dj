from django.db import models

# Create your models here.
class User(models.Model):
    idusr = models.CharField(max_length=120,blank=True,null=True)
    pwdusr = models.CharField(max_length = 20,blank=True,null=True)
    
    def __str__(self):
        return self.id,self.pwd
    
class Computer(models.Model):
    idComp = models.IntegerField(blank=True,null=True,unique=True)
    nameComp = models.CharField(max_length=150,blank=True,null=True)
    ipAdress = models.CharField(max_length=16,blank=True,null=True)
    netmask = models.CharField(max_length=16,blank=True,null=True)
    compState = models.CharField(max_length=20,blank=True,null=True)
    
    def __str__(self):
        return self.idComp,self.nameComp,self.ipAdress,self.netmask,self.compState