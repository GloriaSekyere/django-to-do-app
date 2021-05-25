from django.db import models
from django.contrib.auth.models import User 

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.content[:20]