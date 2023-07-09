from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
    