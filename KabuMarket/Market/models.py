from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    bio = models.TextField(null=True) 
    wlink = models.TextField(null=True)
    phone = models.IntegerField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")


    def __str__(self):
        return self.user.username
        


class Category(models.Model):
    Category = models.CharField(max_length=50)



    def __str__(self):
        return self.Category



class Product(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    description = models.TextField(null=True)
    price = models.IntegerField(default=0)

    
    def __str__(self):
        return self.title


    


