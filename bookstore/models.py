from django.db import models
from authers.models import Auther
from django.urls import reverse

# Create your models here.
class All_books(models.Model):
    name=models.CharField(max_length=100)
    num_of_pages=models.IntegerField(default=50 , null=True, blank=True)
   # cover=models.CharField(max_length=100 , null=True , blank=True)
    price=models.IntegerField(default=100 , null=True, blank=True)
    #auther=models.CharField(max_length=100 , null=True, blank=True)
    auther=models.ForeignKey(Auther,on_delete=models.SET_NULL,related_name='bookstore',null=True,blank=True)
    cover=models.ImageField(upload_to='bookstore/images' , null=True, blank=True)


    def __str__(self):
        return self.name