from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True,max_length=30)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now=True)

class Chairman(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=15)

