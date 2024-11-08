from django.db import models

# Create your models here.
# notes/models.py
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
