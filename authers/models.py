from django.db import models

# Create your models here.

class Auther(models.Model):
    name =models.CharField(max_length=100)
    image = models.ImageField(upload_to='bookstore/images' , null=True, blank=True)
    birthdate =models.DateField(auto_now_add=True, null=True,blank=True)
    created_at =models.DateField(auto_now_add=True, null=True,blank=True)
    updated_at=models.DateField(auto_now_add=True, null=True,blank=True)


    def __str__(self):
        return self.name