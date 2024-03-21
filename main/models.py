from django.db import models

gender = [
    ("m", "male"),
    ("fem", "female"),
]

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255, unique= True)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=3, choices=gender)
    auth_token = models.CharField(max_length=100, blank=True, null=True)

class Thkr(models.Model):
    thkr = models.TextField(max_length=255)
    repeat = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    