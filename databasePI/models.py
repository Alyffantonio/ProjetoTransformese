from django.contrib.auth.hashers import make_password, check_password
from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password) # criptograph password

    def check_password(self, raw_password):
        return check_password(raw_password, self.password) #check password

class ChatbotSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_start = models.DateTimeField(auto_now_add=True)
    session_end = models.DateTimeField(null=True)


class UserTips(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tip = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class ChatbotOption(models.Model):
    opition_text = models.CharField(max_length=600)
    create_at = models.DateTimeField(auto_now_add=True)

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    option = models.CharField(max_length=255)
    response_date = models.DateTimeField(auto_now_add=True)
