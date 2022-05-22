from django.db import models

from django.contrib.auth.models import User

class Chef(models.Model):
    body = models.CharField(max_length=255)

    created_by = models.ForeignKey(User, related_name='Chefs',on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =('-created_at',)


# Create your models here.
