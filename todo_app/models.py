from django.db import models

class Note(models.Model):
    title = models.CharField(name='title', max_length=128)
    text = models.CharField(name='text', max_length=1024)
    user = models.CharField(name='user', max_length=128)
