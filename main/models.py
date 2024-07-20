from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TODO(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    is_completed = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title