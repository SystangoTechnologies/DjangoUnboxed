from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Projects(models.Model):
    project_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
