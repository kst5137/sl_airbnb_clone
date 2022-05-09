from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    writer = models.CharField(max_length=20, null=True)
    create_date = models.DateTimeField(auto_now_add=True)