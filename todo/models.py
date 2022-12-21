from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed_date = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    #This i show we can use a Foreign key.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #This allows us to automatically create a field called 'created_date' which is READONLY
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title