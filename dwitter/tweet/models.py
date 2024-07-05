from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tweet (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo= models.ImageField(upload_to='photos/',blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return f"{self.user.username} - {self.text[:10]}"
    # auto_now_add=True - Sets the field to the current date and time when the object is first created. It will not change on subsequent updates.

    # auto_now=True - Sets the field to the current date and time every time the object is saved, meaning it updates on both creation and subsequent updates.

    # default= timezone.now - Sets the field to the current date and time when the object is created if no other value is provided. This value does not change unless explicitly set again.